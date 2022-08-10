from PyQt5.QtCore import QThread, pyqtSignal

from ibapi.contract import Contract, ComboLeg

from dataComps.Constants import Constants
from datetime import datetime

import numpy as np
import pandas as pd

from uiComps.Logging import Logger

import sys

from dataComps.IBConnectivity import IBConnectivity

class DataManager(QThread):

    data_updater = pyqtSignal(str)

    snapshot = False
    priceReqIsActive = False

    previous_price = 0.0
    price = 0.0
    
    def __init__(self, call_back = None, ib_interface = None, printer=None):
        super().__init__() 

        if call_back is not None:
            self.data_updater.connect(call_back)

        if ib_interface is not None:
            self.ib_interface = ib_interface
            self.ib_interface.delegate = self

        if printer is not None:
            self.printer = printer


    def openConnection(self, local_address, trading_socket, client_id = 0):
        self.ib_interface = IBConnectivity(self, self.printer)
        self.ib_interface.connect(local_address, trading_socket, client_id) 
        
    def run(self):
        self.ib_interface.run()


    def connectionIsOpen(self):
        return self.ib_interface.connection_status == Constants.CONNECTION_OPEN


    def requestMarketData(self, contractDetails):
        if self.priceReqIsActive:
            self.ib_interface.cancelMktData(Constants.STK_PRICE_REQID)

        contract = Contract()
        contract.symbol = contractDetails.symbol
        if contractDetails.numeric_id != 0:
            contract.conId = contractDetails.numeric_id
        else:
            contract.currency = "USD"
            print("If there is no exchange or conID we throw in currency, we need to improve this")
        contract.secType = "STK"
        if contractDetails.exchange != "":
            contract.primaryExchange = contractDetails.exchange
        else:
            contract.currency = "USD"
            print("If there is no exchange or conID we throw in currency, we need to improve this")
        contract.exchange = "SMART"
        self.ib_interface.reqMarketDataType(1)
        print(f"We request the price here for {contract.symbol}")
        self.ib_interface.reqMktData(Constants.STK_PRICE_REQID,contract,"",self.snapshot,False,[])
        self.priceReqIsActive = True
   

    def returnLatestPrice(self, latest_price):
        self.previous_price = self.price

        self.price = latest_price
        self.data_updater.emit(Constants.UNDERLYING_PRICE_UPDATE)


    def relayConnectionStatus(self):
        self.data_updater.emit(Constants.CONNECTION_STATUS_CHANGED)


class SymbolDataManager(DataManager):

    _item_list = set()

    def relayContractDetails(self, details):
        self._item_list.add(details)
        self.data_updater.emit(Constants.CONTRACT_DETAILS_RETRIEVED)


    def contractDetailFetchComplete(self):
        self.data_updater.emit(Constants.CONTRACT_DETAILS_FINISHED)


    def requestContractDetails(self, symbol_name):
        contract = Contract()
        contract.symbol = symbol_name
        contract.secType = "STK"
        contract.exchange = "SMART"
        self.ib_interface.reqContractDetails(Constants.SYMBOL_SEARCH_REQID, contract)


    def hasNewItem(self):
        return len(self._item_list) != 0

    def getLatestItem(self):
        if self.hasNewItem():
            return self._item_list.pop()
        else:
            return None


class OptionChainManager(DataManager):

    _expirations = []
    _strikes = np.array([])
    _contract_ids = np.array([])
    _exp_selection = 0
    _selected_strike = 0

    def fetchContractsFor(self, contractDetails):
        self.contractDetails = contractDetails
        self.ib_interface.reqSecDefOptParams(1, contractDetails.symbol, "", "STK", contractDetails.numeric_id)


    def getDataFrames(self):
        return (self._strike_data_frame, self._exp_data_frame)


    def returnOptionPrice(self, reqId, tick_type, option_price):
        if option_price != -1.0:
            if tick_type == "BID" or tick_type == "ASK" or tick_type == "CLOSE":
                if reqId > Constants.BASE_OPTION_EXP_REQID:
                    index = reqId-Constants.BASE_OPTION_EXP_REQID
                    self._exp_data_frame.loc[index, tick_type] = option_price
                else:
                    index = reqId-Constants.BASE_OPTION_STRIKE_REQID
                    self._strike_data_frame.loc[index, tick_type] = option_price
                    
                self.data_updater.emit(Constants.OPTION_PRICE_UPDATE)


    _strike_data_frame = None
    _exp_data_frame = None

    option_type = Constants.CALL_TYPE


    def fetchContractsIds(self, strike_count, exp_count):
        contract = Contract()
        contract.symbol = self.contractDetails.symbol
        contract.secType = "OPT"
        contract.multiplier = "100"
        contract.right = self.option_type
        contract.exchange = "CBOE"
        self.ib_interface.reqContractDetails(Constants.OPTION_CONTRACT_REQID, contract)
        self._contract_ids = np.empty((strike_count, exp_count), dtype=int)
        self._contract_ids[:] = -1
        

    def reportBackExpirations(self, expiration_set, strike_set):
        if len(self._expirations) != 0:
            self.ib_interface.killOptionDataRequests()

        self.fetchContractsIds(len(strike_set), len(expiration_set))

        self._expirations = []
        self._strikes = np.empty(len(strike_set), dtype=float)

        for exp in sorted(expiration_set):
            self._expirations.append(exp)

        for index, strike in enumerate(sorted(strike_set)):
            self._strikes[index] = strike 

        self.data_updater.emit(Constants.OPTION_INFO_LOADED)

        self.requestMarketData(self.contractDetails)

    def getStrikes(self):
        return self._strikes

    def getExpirations(self):
        return self._expirations


    def getExpirationAt(self, index):
        return self._expirations[index]

    def expirationsLoaded(self):
        return len(self._expirations) !=0

    def optionStyleChangedTo(self, option_type):
        self.option_type = option_type
        if self.expirationsLoaded():
            self.ib_interface.killOptionDataRequests()
            self.fetchContractsFor(self.contractDetails)

    def getExpirationStrings(self):
        string_list = []
        for exp in self._expirations:
            datetime_obj = datetime.strptime(exp, '%Y%m%d')
            string_list.append(datetime_obj.date().strftime("%d %B %Y"))
        return string_list


    def getDaysTillExpiration(self):
        count_list = np.empty(len(self._expirations))
        for index, exp in enumerate(self._expirations):
            datetime_obj = datetime.strptime(exp, '%Y%m%d')
            today = datetime.today()
            count_list[index] = (datetime_obj - today).days
        return count_list

    def setExpirationSelection(self, value):
        if self.expirationsLoaded() and self.newExpSelection(value):
            self._exp_selection = value
            self.ib_interface.killOptionDataRequests()
            self.requestOptionData(self.option_type)

    def newExpSelection(self, value):
        return (value != self._exp_selection) and value >= 0


    def requestOptionData(self, option_type):

        self._strike_data_frame = pd.DataFrame( {'BID': pd.Series(dtype='float'), 'ASK': pd.Series(dtype='float'), 'CLOSE': pd.Series(dtype='float')}, index=range(len(self._strikes)) )
        self._strike_data_frame['STRIKE'] = self._strikes

        contract = Contract()
        contract.symbol = self.contractDetails.symbol
        contract.secType = "OPT"
        contract.lastTradeDateOrContractMonth = self.getExpirationAt(self._exp_selection)
        contract.multiplier = "100"
        contract.right = self.option_type
        contract.exchange = "SMART"
            
        for index, strike in enumerate(self._strikes):
            contract.strike = strike
            reqId = index+Constants.BASE_OPTION_STRIKE_REQID
            self.ib_interface.reqMktData(reqId,contract,"",self.snapshot,False,[])
    

    def relayOptionContractID(self, contract): 
        strikeIndex = self.findStrikeIndex(contract.strike)
        expIndex = self.findExpirationIndex(contract.lastTradeDateOrContractMonth)
        if strikeIndex != -1 and expIndex != -1:
            self._contract_ids[strikeIndex][expIndex] = contract.conId
        

    def findStrikeIndex(self, strike):
        result = np.where(self._strikes == strike)
        return result[0][0]

    def findExpirationIndex(self, expiration):
        try:
            return self._expirations.index(expiration)
        except ValueError:
            return -1


    def updateStrikeSelection(self, selected_strike):

        self.ib_interface.killOptionDataRequests(type=Constants.OPTION_DATA_EXP)
        self._selected_strike = selected_strike

        self._exp_data_frame = pd.DataFrame( {'BID': pd.Series(dtype='float'), 'ASK': pd.Series(dtype='float'), 'CLOSE': pd.Series(dtype='float')}, index=range(len(self._expirations)) )
        self._exp_data_frame['EXPIRATIONS'] = self._expirations
        self._exp_data_frame['NAMES'] = self.getExpirationStrings()
        self._exp_data_frame['DAYS_TILL_EXP'] = self.getDaysTillExpiration()

        print("THE strike is: ", str(self._selected_strike))
        contract = Contract()
        contract.symbol = self.contractDetails.symbol
        contract.secType = "OPT"
        contract.multiplier = "100"
        contract.right = self.option_type
        contract.exchange = "SMART"
        contract.strike = self._selected_strike
        for index, expiration in enumerate(self._expirations):
            print("We fetch for: ", str(expiration))
            contract.lastTradeDateOrContractMonth = expiration
            reqId = index+Constants.BASE_OPTION_EXP_REQID
            self.ib_interface.reqMktData(reqId,contract,"",self.snapshot,False,[])

    def fetchSpreads(self):
        print("We go fetch spreads")

        self.ib_interface.killOptionDataRequests(type=Constants.OPTION_DATA_EXP)

        self._exp_data_frame = pd.DataFrame( {'BID': pd.Series(dtype='float'), 'ASK': pd.Series(dtype='float'), 'CLOSE': pd.Series(dtype='float')}, index=range(len(self._expirations)) )
        self._exp_data_frame['EXPIRATIONS'] = self._expirations
        self._exp_data_frame['DAYS_TILL_EXP'] = self.getDaysTillExpiration()

        contract = Contract()
        contract.symbol = self.contractDetails.symbol
        contract.secType = "BAG"
        contract.exchange = "CBOE"

        strike_index = self.findStrikeIndex(self._selected_strike)

        for exp_index, expiration in enumerate(self._expirations):
            
            first_id = self._contract_ids[strike_index][exp_index]
            counter = 1
            second_id = self._contract_ids[strike_index+counter][exp_index]
            while second_id == -1 and counter < len(self._expirations):
                second_id = self._contract_ids[strike_index+counter][exp_index]
                counter += 1

            print("For the exp ", self._expirations[exp_index] , " we get the spread for: ", str(self._strikes[strike_index]), " and ", str(self._strikes[strike_index+counter]))

            if first_id != -1 and second_id != -1:

                leg1 = ComboLeg()
                leg1.conId = first_id
                leg1.ratio = 1
                leg1.action = "BUY"
                leg1.exchange = "CBOE"
                leg2 = ComboLeg()
                leg2.conId = second_id
                leg2.ratio = 1
                leg2.action = "SELL"
                leg2.exchange = "CBOE"

                contract.comboLegs = []
                contract.comboLegs.append(leg1)
                contract.comboLegs.append(leg2)
                reqId = Constants.BASE_OPTION_EXP_REQID + exp_index
                print("We request: ")
                print(contract.comboLegs)
                self.ib_interface.reqMktData(reqId,contract,"",self.snapshot,False,[])



