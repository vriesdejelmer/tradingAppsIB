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
from uiComps.qtGeneration.ListEditor_UI import Ui_MainWindow as ListEditor_UI
import sys
from dataComps.Constants import OrderType, Constants

from generalFunctionality.SymbolFinderImpl import SymbolFinderImplementation
from generalFunctionality.UIFunctions import findRowForValue, AlignDelegate, PercAlignDelegate

from math import log10


class ListManagerWindow(QMainWindow, ListEditor_UI, SymbolFinderImplementation):

    current_selection = None

    def __init__(self):
        QMainWindow.__init__(self)
        ListEditor_UI.__init__(self)
        SymbolFinderImplementation.__init__(self)

        self.setupUi(self)
        self.forceUpperCase()
        self.connectSearchField()
        self.connectActions()

        self.setTableProperties()

        self.stock_list = dict()


    def setTableProperties(self):
        header = self.stock_table.horizontalHeader()
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

    def connectActions(self):
        self.save_button.clicked.connect(self.saveStockList)
        self.add_list_button.clicked.connect(self.createNewList)
        self.list_selector.currentIndexChanged.connect(self.listSelection)


    def selectedContract(self, contractDetails):
        self.current_selection = contractDetails

    def returnSelection(self):
        if self.current_selection is not None:
            numeric_id = str(self.current_selection.numeric_id)
            self.stock_list[numeric_id] = {'symbol': self.current_selection.symbol, 'long_name': self.current_selection.long_name, 'exchange': self.current_selection.exchange}

            current_count = self.stock_table.rowCount()
            self.addRowAt(current_count, numeric_id, self.stock_list[numeric_id])
       
            self.current_selection = None

            self.search_field.clear()

    def addRowAt(self, index, numeric_id, details):
        
        current_count = self.stock_table.rowCount()
        if index >= current_count:
            self.stock_table.setRowCount(index+1)

        self.stock_table.setItem(index, 0, QTableWidgetItem(numeric_id))
        self.stock_table.setItem(index, 1, QTableWidgetItem(details['symbol']))
        self.stock_table.setItem(index, 2, QTableWidgetItem(details['long_name']))
        self.stock_table.setItem(index, 3, QTableWidgetItem(details['exchange']))

        delete_button = QtWidgets.QPushButton()
        delete_button.setObjectName(numeric_id)
        delete_button.setText("-")
        delete_button.clicked.connect(lambda: self.deleteClicked(numeric_id))
        self.stock_table.setCellWidget(index, 4, delete_button)
    
    def deleteClicked(self, numeric_id):
        print(f"Here we get a different id {numeric_id}")
        del self.stock_list[numeric_id]
        row_index = findRowForValue(self.stock_table, numeric_id, 0)
        self.stock_table.removeRow(row_index)


    def dataUpdate(self, signal):
        print(f"ListManagerWindow.dataUpdate: {signal}")
        self.contractUpdate(signal)
