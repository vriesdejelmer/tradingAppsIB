from PyQt5.QtCore import QThread, pyqtSignal

from ibapi.contract import Contract

from dataComps.Constants import Constants
import numpy as np
import pandas as pd

from math import ceil
from datetime import datetime, date
from numpy import datetime64
from dateutil.relativedelta import relativedelta

import sys
import time


from uiComps.Logging import Logger

from dataComps.dataManagement import DataManager
from dataComps.IBConnectivity import IBConnectivity


class HistoricalDataManager(DataManager):

    _stock_data_frame = None
    _stocks = []
    _uid_by_req = dict()
    _price_dict = dict()
    _bar_type_by_req = dict()

    
    def fetchHistoricalDataFor(self, stocks, period):
        self._stocks = stocks
        keys = stocks.keys()
        self._stock_data_frame = pd.DataFrame( {'MAX': pd.Series(dtype='float'), 'MAX_DATE': pd.Series(dtype='datetime64[ns]'), 'MIN': pd.Series(dtype='float'), 'MIN_DATE': pd.Series(dtype='datetime64[ns]')}, index=list(keys))
        self._stock_data_frame['SYMBOL'] = [stocks[key]["symbol"] for key in keys]
        self._stock_data_frame['MAX'] = sys.float_info.min
        self._stock_data_frame['MIN'] = sys.float_info.max

        contract = Contract()
        contract.exchange = "SMART"
        contract.secType = "STK"

        for index, (uid, stock_tuple) in enumerate(stocks.items()):
            contract.symbol = stock_tuple["symbol"]
            contract.conId = uid
            contract.primaryExchange = stock_tuple["exchange"]
            reqId = Constants.BASE_HIST_MIN_MAX_REQID + index
            self._uid_by_req[reqId] = uid
            self.ib_interface.reqHistoricalData(reqId, contract, "",period , "1 day", "TRADES", 0, 1, False, [])
        
    def fetchAndStoreBars(self, contract_details, start_date, end_date, bar_type, delay=15):
        self.historicalDF = pd.DataFrame(columns=['Open', 'High', 'Low', 'Close', 'Volume'])

        years = int(relativedelta(end_date, start_date).years)
        months = int(relativedelta(end_date, start_date).months)     
        days = relativedelta(end_date, start_date).days
        days = int(ceil(5*days/7))


        contract = Contract()
        contract.exchange = "SMART"
        contract.secType = "STK"
        contract.symbol = contract_details.symbol
        contract.conId = contract_details.numeric_id
        contract.primaryExchange = contract_details.exchange

        for year in range(years):
            end_date_string = end_date.replace(year = end_date.year - year).strftime("%Y%m%d %H:%M:%S")
            req_id = Constants.BASE_HIST_DATA_REQID + year
            self.ib_interface.reqHistoricalData(req_id, contract, end_date_string, "1 Y", bar_type, "TRADES", 0, 1, False, [])
            time.sleep(delay)

        if months > 0:
            end_date_string = end_date.replace(year = end_date.year - years).strftime("%Y%m%d %H:%M:%S")
            req_id = Constants.BASE_HIST_DATA_REQID + years            
            self.ib_interface.reqHistoricalData(req_id, contract, end_date_string, f"{months} M", bar_type, "TRADES", 0, 1, False, [])
            time.sleep(delay)

        if days > 0:
            end_date_string = end_date.replace(year = end_date.year - years, month = end_date.month - months).strftime("%Y%m%d %H:%M:%S")
            req_id = Constants.BASE_HIST_DATA_REQID + years + 1
            self.ib_interface.reqHistoricalData(req_id, contract, end_date_string, f"{days} D", bar_type, "TRADES", 0, 1, False, [])
            

    def getBars(self, stocks):

        self.historicalDF = pd.DataFrame(columns=['Date', 'UID', 'BarType', 'Open', 'High', 'Low', 'Close', 'Volume'])

        bar_types = ['5 mins', '15 mins', '1 hour', '4 hours', '8 hours', '1 day', '1 week'] #, '1 month']
        bar_type_duration = {'5 mins': '5 D', '15 mins': '5 D', '1 hour': '4 D', '4 hours': '10 D', '8 hours': '20 D', '1 day': '40 D', '1 week': '4 M'} #, '1 month': '15 M'

        self._bar_type_by_req = dict()
        self._uid_by_req = dict()

        contract = Contract()
        contract.exchange = "SMART"
        contract.secType = "STK"

        index = 0
        for stock_index, (uid, stock_tuple) in enumerate(stocks.items()):
            contract.symbol = stock_tuple["symbol"]
            contract.conId = uid
            contract.primaryExchange = stock_tuple["exchange"]

            for bar_type in bar_types:
                print(f"We make a request for {contract.symbol} for the {bar_type}")
                req_id = Constants.BASE_HIST_BARS_REQID + index
                self._bar_type_by_req[req_id] = bar_type
                self._uid_by_req[req_id] = uid
                self.ib_interface.reqHistoricalData(req_id, contract, "", bar_type_duration[bar_type], bar_type, "TRADES", 0, 1, False, [])
                index += 1


    def relayBarData(self, reqId, bar):
        self.historicalDF.loc[pd.to_datetime(bar.date)] = {"Open": bar.open, "High": bar.high, "Low": bar.low, "Close": bar.close, "Volume": bar.volume}
        

    def relayStepBarData(self, reqId, bar):
        self.historicalDF.loc[len(self.historicalDF.index)] = {"Date": pd.to_datetime(bar.date), "UID": self._uid_by_req[reqId], "BarType": self._bar_type_by_req[reqId], "Open": bar.open, "High": bar.high, "Low": bar.low, "Close": bar.close, "Volume": bar.volume}
    

    def relayHistoricalMinMax(self, reqId, bar):
        uid = self._uid_by_req[reqId]

        if bar.high > self._stock_data_frame.loc[uid].MAX:
            self._stock_data_frame.loc[uid,"MAX"] = bar.high
            self._stock_data_frame.loc[uid,"MAX_DATE"] = bar.date

        if bar.low < self._stock_data_frame.loc[uid].MIN:
            self._stock_data_frame.loc[uid,"MIN"] = bar.low
            self._stock_data_frame.loc[uid,"MIN_DATE"] = bar.date


    def signalHistoryMinMaxComplete(self):
        self.data_updater.emit(Constants.HISTORICAL_MIN_MAX_FETCH_COMPLETE)


    def signalHistoryDataComplete(self):
        self.data_updater.emit(Constants.HISTORICAL_DATA_FETCH_COMPLETE)


    def signalPricesComplete(self):
        self.data_updater.emit(Constants.PRICE_COLLECTION_COMPLETE)


    def fetchPricesFor(self, stock_list):
        self.ib_interface.reqMarketDataType(1)
        self._price_dict = dict()
        self._uid_by_req = dict()

        contract = Contract()
        contract.exchange = "SMART"
        contract.secType = "STK"

        for index, (uid, stock_tuple) in enumerate(stock_list.items()):
            contract.symbol = stock_tuple["symbol"]
            contract.conId = uid
            contract.primaryExchange = stock_tuple["exchange"]
            reqId = Constants.BASE_MKT_STOCK_REQID + index
            self._uid_by_req[reqId] = uid
            self.ib_interface.reqMktData(reqId, contract, "", True, False, [])
    

    def relayMktData(self, reqId, price, tick_type):
        if tick_type == "LAST":
            self._price_dict[self._uid_by_req[reqId]] = price
        elif not self._uid_by_req[reqId] in self._price_dict:
            self._price_dict[self._uid_by_req[reqId]] = price


    def getStockData(self):    
        return self._stock_data_frame

    def getPriceData(self):    
        return self._price_dict