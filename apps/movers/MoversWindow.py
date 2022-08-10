# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionsGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import numpy as np
from uiComps.qtGeneration.Movers_UI import Ui_MainWindow as Movers_UI
import sys
from dataComps.Constants import OrderType, Constants
from dataComps.UserDataManagement import getStockListNames
from generalFunctionality.UIFunctions import findRowForValue
from math import log10
from generalFunctionality.UIFunctions import getNumericItem, AlignDelegate, BigNumberAlignDelegate, PercAlignDelegate

class MoversWindow(QMainWindow, Movers_UI):

    period_options = {"Week": "1 W", "2 Weeks": "2 W", "Month": "1 M", "2 Months": "2 M", "6 Months": "6 M", "1 Year": "12 M"}
    list_options = ["Volatile Defined", "Custom List"]

    def __init__(self):
        QMainWindow.__init__(self)
        Movers_UI.__init__(self)

        self.setupUi(self)

        self.populateBoxes()
        self.setupActions()
        self.setupAlignment()
        self.stock_table.setSortingEnabled(True)
        self.stock_table.cellClicked.connect(self.cellClicked)
        
    def setupActions(self):
        self.fetch_button.clicked.connect(self.fetchStocks)        
        self.period_selector.currentTextChanged.connect(self.periodSelection)
        self.list_selector.currentIndexChanged.connect(self.listSelection)


    def populateBoxes(self):
        self.stock_lists = getStockListNames()
        for file_name, list_name in self.stock_lists:
            self.list_selector.addItem(list_name)

        for item in self.period_options.keys():
            self.period_selector.addItem(item)

    def setupAlignment(self):

        alignDelegate = AlignDelegate(self.stock_table)
        percAlignDelegate = PercAlignDelegate(self.stock_table)
        bigNumAlignDelegate = BigNumberAlignDelegate(self.stock_table)
        self.stock_table.setItemDelegateForColumn(1, alignDelegate)
        self.stock_table.setItemDelegateForColumn(2, alignDelegate)
        self.stock_table.setItemDelegateForColumn(3, percAlignDelegate)
        self.stock_table.setItemDelegateForColumn(4, alignDelegate)
        self.stock_table.setItemDelegateForColumn(5, percAlignDelegate)
        self.stock_table.setItemDelegateForColumn(6, percAlignDelegate)
        self.stock_table.setItemDelegateForColumn(7, bigNumAlignDelegate)


    def setData(self, stock_df, fee_rate, short_availability):

        self.stock_table.clearContents()
        self.stock_table.setRowCount(len(stock_df.index))
        
        for index, (uid, stock) in enumerate(stock_df.iterrows()):
            
            self.stock_table.setItem(index, 0, QTableWidgetItem(stock['SYMBOL']))
            self.stock_table.setItem(index, 2, getNumericItem(stock['MIN']))
            self.stock_table.setItem(index, 4, getNumericItem(stock['MAX']))
            self.stock_table.setItem(index, 6, getNumericItem(fee_rate[index]))
            self.stock_table.setItem(index, 7, QTableWidgetItem(short_availability[index]))
            self.stock_table.setItem(index, 8, QTableWidgetItem(uid))
                    

    def setPriceForID(self, price, uid):
        row_index = findRowForValue(self.stock_table, uid, 8)

        price_fmt = "${:.2f}".format(price)

        self.stock_table.setItem(row_index, 1, QTableWidgetItem(price_fmt))
        
        move_from_low = (price - self.stock_df.loc[uid].MIN)/self.stock_df.loc[uid].MIN*100
        self.stock_table.setItem(row_index, 3, getNumericItem(move_from_low))

        move_from_high = (self.stock_df.loc[uid].MAX-price)/self.stock_df.loc[uid].MAX*100
        self.stock_table.setItem(row_index, 5, getNumericItem(move_from_high))

    def fillOutPrices(self):
        price_dict = self.data_management.getPriceData()
        for key, value in price_dict.items():
            self.setPriceForID(value, key)
    

