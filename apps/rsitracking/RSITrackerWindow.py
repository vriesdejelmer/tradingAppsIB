# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionsGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import numpy as np
from uiComps.qtGeneration.Stairstep_UI import Ui_MainWindow as Stairstep_UI
import sys
from dataComps.Constants import OrderType, Constants
from dataComps.UserDataManagement import getStockListNames
from generalFunctionality.UIFunctions import findRowForValue
from math import log10
from generalFunctionality.UIFunctions import getNumericItem, AlignDelegate, BigNumberAlignDelegate, PercAlignDelegate

class RSITrackerWindow(QMainWindow, Stairstep_UI):

    def __init__(self):
        QMainWindow.__init__(self)
        Stairstep_UI.__init__(self)

        self.setupUi(self)

        self.populateBoxes()
        self.setupActions()
#        self.setupAlignment()
        # self.stock_table.setSortingEnabled(True)
        # self.stock_table.cellClicked.connect(self.cellClicked)

        
    def setupActions(self):
        self.fetch_button.clicked.connect(self.fetchStocks)        
        self.list_selector.currentIndexChanged.connect(self.listSelection)


    def populateBoxes(self):
        self.stock_lists = getStockListNames()
        for file_name, list_name in self.stock_lists:
            self.list_selector.addItem(list_name)

    # def setupAlignment(self):

    #     alignDelegate = AlignDelegate(self.stock_table)
    #     percAlignDelegate = PercAlignDelegate(self.stock_table)
    #     bigNumAlignDelegate = BigNumberAlignDelegate(self.stock_table)
    #     self.stock_table.setItemDelegateForColumn(1, alignDelegate)
    #     self.stock_table.setItemDelegateForColumn(2, alignDelegate)
    #     self.stock_table.setItemDelegateForColumn(3, percAlignDelegate)
    #     self.stock_table.setItemDelegateForColumn(4, alignDelegate)
    #     self.stock_table.setItemDelegateForColumn(5, percAlignDelegate)
    #     self.stock_table.setItemDelegateForColumn(6, percAlignDelegate)
    #     self.stock_table.setItemDelegateForColumn(7, bigNumAlignDelegate)


    def setData(self, stock_ids, rsi_values):

        print(rsi_values)

        self.bull_table.clearContents()
        self.bull_table.setRowCount(rsi_values.shape[0])
        
        for index, stock_id in enumerate(stock_ids):
            self.bull_table.setItem(index, 0, QTableWidgetItem(self.stock_list[stock_id]['symbol']))

        for row_index in range(rsi_values.shape[0]):
            for column_index in range(rsi_values.shape[1]):
                # intensity = 5 * (low_counts[row_index, column_index] + low_moves[row_index, column_index])
                item = QTableWidgetItem(f"{rsi_values[row_index, column_index]:.1f}")
                # item.setBackground(QBrush(QColor(255, 255, max(255-intensity,0))))
                self.bull_table.setItem(row_index, column_index+1, item)

        
    # def setPriceForID(self, price, uid):
    #     row_index = findRowForValue(self.stock_table, uid, 8)

    #     price_fmt = "${:.2f}".format(price)

    #     self.stock_table.setItem(row_index, 1, QTableWidgetItem(price_fmt))
        
    #     move_from_low = (price - self.stock_df.loc[uid].MIN)/self.stock_df.loc[uid].MIN*100
    #     self.stock_table.setItem(row_index, 3, getNumericItem(move_from_low))

    #     move_from_high = (self.stock_df.loc[uid].MAX-price)/self.stock_df.loc[uid].MAX*100
    #     self.stock_table.setItem(row_index, 5, getNumericItem(move_from_high))

    # def fillOutPrices(self):
    #     price_dict = self.data_management.getPriceData()
    #     for key, value in price_dict.items():
    #         self.setPriceForID(value, key)
    

