
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum

import time
from dataComps.DataStructures import DetailObject
from dataComps.Constants import Constants

from uiComps.Logging import Logger

class IBConnectivity(EClient, EWrapper):

    _open_option_reqs = set()
    _hist_min_max_reqs = set()
    _hist_data_reqs = set()
    _hist_bars_reqs = set()
    _mkt_data_reqs = set()
    _pnl_data_reqs = set()
    pacing_break = 0.02
    price_returned = False

    connection_status = Constants.CONNECTION_CLOSED

    def __init__(self, delegate, printer = None):
        
        EClient.__init__(self, self)

        self.printer = printer
        self.delegate = delegate
        
    
    def tickPrice(self, reqId, tickType, price, attrib):
        tick_type_str = TickTypeEnum.to_str(tickType)
        self.printer.addLine(f"We receive {tick_type_str} for {reqId} with a price of {price}")
        if self.isPriceRequest(reqId) and (tick_type_str == "LAST" or tick_type_str == "CLOSE"  or tick_type_str == "ASK"):
            print(f"We get a close for {reqId}")
            self.delegate.relayMktData(reqId, price, tick_type=tick_type_str)

            if reqId in self._mkt_data_reqs:
                self._mkt_data_reqs.remove(reqId)

            self.printer.addLine(f"We have {len(self._mkt_data_reqs)} left")
            if len(self._mkt_data_reqs) == 0:
                print("But we should come here more than once?!?!?!?")
                self.delegate.signalPricesComplete()
        elif self.isOptionRequest(reqId):
            self.delegate.returnOptionPrice(reqId, tick_type_str, price)
            if self.isExpType(reqId):
                self.printer.addLine("reqId: ", str(reqId), ", ", tick_type_str, ", ", str(price))
        elif reqId == Constants.STK_PRICE_REQID and tick_type_str == "LAST":
            self.price_returned = True
            self.delegate.returnLatestPrice(price)
        elif not self.price_returned and reqId == Constants.STK_PRICE_REQID and tick_type_str == "CLOSE":
            self.delegate.returnLatestPrice(price)

    def tickString(self, reqId, tickType, value):
        super().tickString(reqId, tickType, value)
        tick_type_str = TickTypeEnum.to_str(tickType)


    def tickGeneric(self, reqId, tickType, value):
        super().tickGeneric(reqId, tickType, value)
        tick_type_str = TickTypeEnum.to_str(tickType)

    
    def error(self, reqId, errorCode, errorString):
        if reqId == -1:    
            self.printer.addLine(f"Base message: {errorString}")
        else:
            self.printer.addLine(f'Error: {reqId}, code: {errorCode}, message: {errorString}, reqId: {reqId}')
            if errorCode == 200:
                if self.isOptionRequest(reqId) and reqId in self._open_option_reqs:
                    self._open_option_reqs.remove(reqId)
                elif self.isPriceRequest(reqId) and reqId in self._mkt_data_reqs:
                    self._mkt_data_reqs.remove(reqId)
                elif self.isHistMinMaxRequest(reqId) and reqId in self._hist_min_max_reqs:
                    self._hist_min_max_reqs.remove(reqId)
                elif (self.isHistDataRequest(reqId) or self.isHistBarsRequest(reqId)) and reqId in self._hist_data_reqs:
                    self._hist_data_reqs.remove(reqId)

        
    def connectAck(self):
        super().connectAck()
        self.connection_status = Constants.CONNECTION_OPEN
        self.delegate.relayConnectionStatus()

    def connectionClosed(self):
        super().connectionClosed()
        self.connection_status = Constants.CONNECTION_CLOSED
        self.delegate.relayConnectionStatus()

    def contractDetails(self, reqId, contractDetails):
        if reqId == Constants.OPTION_CONTRACT_REQID:
            self.delegate.relayOptionContractID(contractDetails.contract)
        else:
            ctr = contractDetails.contract
            detailObject = DetailObject(symbol=ctr.symbol, exchange=ctr.primaryExchange, long_name=contractDetails.longName, numeric_id=ctr.conId)
            self.delegate.relayContractDetails(detailObject)
        
    def contractDetailsEnd(self, reqId: int):
        super().contractDetailsEnd(reqId)
        self.delegate.contractDetailFetchComplete()

    def addContractListener(self, listener):
        self.contractListener = listener

    def reqMktData(self, reqId, contract: Contract,
                    genericTickList: str, snapshot: bool, regulatorySnapshot: bool,
                    mktDataOptions):
        super().reqMktData(reqId, contract, genericTickList, snapshot, regulatorySnapshot, mktDataOptions)
        self.paceRequests()

        if self.isOptionRequest(reqId):
            self._open_option_reqs.add(reqId)
        elif self.isPriceRequest(reqId):
            self.price_returned = False
            self._mkt_data_reqs.add(reqId)
        
    def reqHistoricalData(self, reqId, contract, endDateTime, durationStr, barSizeSetting, whatToShow, useRTH, formatDate, keepUpToDate, chartOptions):
        super().reqHistoricalData(reqId, contract, endDateTime, durationStr, barSizeSetting, whatToShow, useRTH, formatDate, keepUpToDate, chartOptions)
        self.paceRequests(0.5)
        self.printer.addLine(f"Req Id: {reqId} for HIST-DATA. Symbol: {contract.symbol}, Enddate: {endDateTime}, Duration: {durationStr}, Bars: {barSizeSetting} ")
        if self.isHistMinMaxRequest(reqId):
            self._hist_min_max_reqs.add(reqId)
        elif self.isHistDataRequest(reqId) or self.isHistBarsRequest(reqId):
            self._hist_data_reqs.add(reqId)
        

    def killOptionDataRequests(self, type=None):
        while self._open_option_reqs:
            index_to_kill = self._open_option_reqs.pop()
            if type == None or (type == Constants.OPTION_DATA_STRIKE and self.isStrikeType(index_to_kill)) or (type == Constants.OPTION_DATA_EXP and self.isExpType(index_to_kill)):
                self.cancelMktData(index_to_kill)
                self.paceRequests()

    def paceRequests(self, pacing_break=None):
        if pacing_break is not None:
            time.sleep(pacing_break)
        else:
            time.sleep(self.pacing_break)
    def isStrikeType(self, reqId):
        return (reqId >= Constants.BASE_OPTION_STRIKE_REQID and reqId < (Constants.BASE_OPTION_STRIKE_REQID + Constants.REQID_STEP))

    def isExpType(self, reqId):
        return (reqId >= Constants.BASE_OPTION_EXP_REQID and reqId < (Constants.BASE_OPTION_EXP_REQID + Constants.REQID_STEP))

    def isOptionRequest(self, reqId):
        return self.isExpType(reqId) or self.isStrikeType(reqId)

    def isPriceRequest(self, reqId):
        return (reqId >= Constants.BASE_MKT_STOCK_REQID and reqId < (Constants.BASE_MKT_STOCK_REQID + Constants.REQID_STEP))

    def isHistDataRequest(self, reqId):
        return (reqId >= Constants.BASE_HIST_DATA_REQID and reqId < (Constants.BASE_HIST_DATA_REQID + Constants.REQID_STEP))

    def isHistBarsRequest(self, reqId):
        return (reqId >= Constants.BASE_HIST_BARS_REQID and reqId < (Constants.BASE_HIST_BARS_REQID + Constants.REQID_STEP))

    def isHistMinMaxRequest(self, reqId):
        return (reqId >= Constants.BASE_HIST_MIN_MAX_REQID and reqId < (Constants.BASE_HIST_MIN_MAX_REQID + Constants.REQID_STEP))


    def securityDefinitionOptionParameter(self, reqId: int, exchange: str,
                                          underlyingConId: int, tradingClass: str, multiplier: str,
                                          expirations, strikes):
        super().securityDefinitionOptionParameter(reqId, exchange,
                                                  underlyingConId, tradingClass, multiplier, expirations, strikes)
        if exchange == "CBOE":
            self.delegate.reportBackExpirations(expirations, strikes)
    # ! [securityDefinitionOptionParameter]


    def updateAccountValue(self, key: str, val: str, currency: str, accountName: str):
        super().updateAccountValue(key, val, currency, accountName)


    def updatePortfolio(self, contract: Contract, position, marketPrice, marketValue, averageCost, unrealizedPNL, realizedPNL, accountName):
        super().updatePortfolio(contract, position, marketPrice, marketValue, averageCost, unrealizedPNL, realizedPNL, accountName)
        self.delegate.returnPosition(contract, position, marketPrice, unrealizedPNL)
        

    def updateAccountTime(self, timeStamp: str):
        super().updateAccountTime(timeStamp)


    def accountDownloadEnd(self, accountName: str):
        super().accountDownloadEnd(accountName)
        self.delegate.positionsFetched()


    def historicalData(self, reqId, bar):
        super().historicalData(reqId, bar)
        if self.isHistMinMaxRequest(reqId):
            self.delegate.relayHistoricalMinMax(reqId, bar)
        elif self.isHistDataRequest(reqId):
            self.delegate.relayBarData(reqId, bar)
        elif self.isHistBarsRequest(reqId):
            self.delegate.relayStepBarData(reqId, bar)
                

    def historicalDataEnd(self, reqId: int, start: str, end: str):
        super().historicalDataEnd(reqId, start, end)
        print("we completed " + str(reqId) + " start: " + str(start) + " end: " + str(end))

        if reqId in self._hist_min_max_reqs:
            self._hist_min_max_reqs.remove(reqId)
            if len(self._hist_min_max_reqs) == 0:
                self.delegate.signalHistoryMinMaxComplete()
        elif reqId in self._hist_data_reqs:
            self._hist_data_reqs.remove(reqId)
            print(f"We have {len(self._hist_data_reqs)}")
            if len(self._hist_data_reqs) == 0:
                self.delegate.signalHistoryDataComplete()


        # print("Historical data (reqId:", reqId, ") fetched from: ", start, ", to: ", end,sep="")
        # if reqId in self.completedIds:
        #     print('Carefull duplicate ReqIDs are not a good idea')
        # else:
        #     self.completedIds.append(reqId)
        # self.completed = True
        # self.executing = False
        
    # def __init__(self):
    #     EClient.__init__(self, self)
        
    #     self.completedIds = []
    #     self.executing = False
    #     self.completed = False
    #     self.historicalDF = pd.DataFrame(columns=['Open', 'High', 'Low', 'Close', 'Volume'])
        
    # def error(self, reqId, errorCode, errorString):
    #     print("Error: ", reqId, " ", errorCode, " ", errorString)

    # def initiateFetch(self, contract, reqId, queryTime="", period="1 Y", bar_type="1 day", RTH=1):
    #     app.reqHistoricalData(reqId, contract, queryTime, period, bar_type, "TRADES", RTH, 1, False, [])
        
    # def historicalData(self, reqId, bar):
    #     if self.executing == False: self.executing = True
    
        
    # def historicalDataEnd(self, reqId: int, start: str, end: str):
    #     super().historicalDataEnd(reqId, start, end)
    #     print("Historical data (reqId:", reqId, ") fetched from: ", start, ", to: ", end,sep="")
    #     if reqId in self.completedIds:
    #         print('Carefull duplicate ReqIDs are not a good idea')
    #     else:
    #         self.completedIds.append(reqId)
    #     self.completed = True
    #     self.executing = False

    def reqPnL(self, reqId: int, account: str, modelCode: str):
        super().reqPnL(reqId, account, modelCode)
        
    def reqPnLSingle(self, reqId: int, account: str, modelCode: str, conId: int):
        super().reqPnLSingle(reqId, account, modelCode, conId)
        self._pnl_data_reqs.add(reqId)

    def pnl(self, reqId: int, dailyPnL: float, unrealizedPnL: float, realizedPnL: float):
        super().pnl(reqId, dailyPnL, unrealizedPnL, realizedPnL)
        self.delegate.updatePNL(reqId, dailyPnL, unrealizedPnL)
        print("Daily PnL. ReqId: ", reqId, "DailyPnL: ", str(dailyPnL), "UnrealizedPnL: ", str(unrealizedPnL), "RealizedPnL: ", str(realizedPnL))
        self.cancelPnL(reqId)

    def pnlSingle(self, reqId: int, pos: float, dailyPnL: float, unrealizedPnL: float, realizedPnL: float, value: float):
        super().pnlSingle(reqId, pos, dailyPnL, unrealizedPnL, realizedPnL, value)
        self.delegate.updateSinglePNL(reqId, dailyPnL, unrealizedPnL)
        print("Daily PnL Single. ReqId:", reqId, "Position:", str(pos), "DailyPnL:", str(dailyPnL), "UnrealizedPnL:", str(unrealizedPnL), "RealizedPnL:", str(realizedPnL), "Value:", str(value))
        if reqId in self._pnl_data_reqs:
            self._pnl_data_reqs.remove(reqId)
            self.cancelPnLSingle(reqId)

        if len(self._pnl_data_reqs) == 0: self.delegate.pnlRequestsComplete()

    def accountSummary(self, reqId: int, account: str, tag: str, value: str, currency: str):
        super().accountSummary(reqId, account, tag, value, currency)
        self.delegate.returnAccount(account)
        print("AccountSummary. ReqId:", reqId, "Account:", account, "Tag: ", tag, "Value:", value, "Currency:", currency)

    def accountSummaryEnd(self, reqId: int):
        super().accountSummaryEnd(reqId)
        print("AccountSummaryEnd. ReqId:", reqId)