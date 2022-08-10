# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionsGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QCompleter, QTableWidgetItem
import numpy as np
from dataComps.Constants import Constants, OrderType
from .MoversWindow import MoversWindow
import sys, threading
import pandas as pd

from uiComps.Logging import Logger
import webbrowser

from dataComps.UserDataManagement import readStockList
from dataComps.ibFTPdata import getShortDataFor
from dataComps.HistoricalDataManagement import HistoricalDataManager

class MoversList(MoversWindow):

    time_period = "Month"

    def __init__(self, history_manager):
        super().__init__()

        self.data_management = history_manager
        self.data_management.data_updater.connect(self.dataUpdate)
        
        file_name, _ = self.stock_lists[0]
        self.stock_list = readStockList(file_name)
        self.fetchShortRates()
        self.period_selector.setCurrentText(self.time_period)


    def periodSelection(self, value):
        self.time_period = value

    def listSelection(self, value):
        self.stock_table.clearContents()
        self.stock_table.setRowCount(0)
        file_name, _ = self.stock_lists[value]
        self.stock_list = readStockList(file_name)
        self.fetchShortRates()

    def priceUpdate(self):
        self.data_management.fetchPricesFor(self.stock_list)

    def dataUpdate(self, signal):
        print(f"MoversList.dataUpdate: {signal}")
        if signal == Constants.HISTORICAL_MIN_MAX_FETCH_COMPLETE:
            self.fillOutTable()
            self.priceUpdate()
        elif signal == Constants.PRICE_COLLECTION_COMPLETE:
            self.fillOutPrices()
            self.fetch_button.setEnabled(True)

        
    def fillOutTable(self):
        self.stock_df = self.data_management.getStockData()
        self.setData(self.stock_df, self.fee_rates, self.short_availability)

    def fetchStocks(self):
        self.fetch_button.setEnabled(False)
        self.data_management.fetchHistoricalDataFor(self.stock_list, self.period_options[self.time_period])


    def fetchShortRates(self):
        self.fee_rates = np.ones((len(self.stock_list))) * 500
        self.short_availability = [""] * len(self.stock_list)
        for index, stock in enumerate(self.stock_list):
            short_data = getShortDataFor(stock)
            print(f"For {stock} we found {short_data}")
            if len(short_data) != 0:
                self.fee_rates[index] = float(short_data[6])
                self.short_availability[index] = short_data[7]


    def cellClicked(self, row, column):
        
        if column == 2 or column == 4:
            item_key = self.stock_table.item(row, 8).data(QtCore.Qt.DisplayRole)

            QtWidgets.QToolTip.hideText()
            r = self.stock_table.visualItemRect(self.stock_table.item(row, column))
            p = self.stock_table.viewport().mapToGlobal(QtCore.QPoint(r.center().x(), r.top()))

            print(type(self.stock_df.loc[item_key].MIN_DATE))
            if column == 2: QtWidgets.QToolTip.showText(p, self.stock_df.loc[item_key].MIN_DATE.strftime('%Y.%m.%d'))
            if column == 4: QtWidgets.QToolTip.showText(p, self.stock_df.loc[item_key].MAX_DATE.strftime('%Y.%m.%d'))

        elif column == 0:
            item_key = self.stock_table.item(row, 8).data(QtCore.Qt.DisplayRole)            
            item = self.stock_list[item_key]
            webbrowser.open(f"https://www.tradingview.com/chart/?symbol={item['exchange']}%3A{item['symbol']}", new=2)



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    window = MoversList()
    window.show()
    app.exec_()



