# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionsGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QCheckBox
import numpy as np
from uiComps.qtGeneration.OptionsTab_UI import Ui_Form as OptionsTab
from uiComps.qtGeneration.SpecOptionsTab_UI import Ui_Form as SpecOptionsTab
import pandas as pd
from datetime import datetime
from dataComps.Constants import Constants

from generalFunctionality.UIFunctions import getNumericItem, AlignDelegate, PriceAlignDelegate


class OptionTabWidget(QWidget):

    individual = False
    tab_name = ""

    def __init__(self):
        super().__init__()
        
        self.setupUi()
        self.setupAlignment()
        self.options_table.setSortingEnabled(True)

        header = self.options_table.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)


    def setupUi(self):
        print("OptionsTab.setupUI")
        new_form = OptionsTab() 
        new_form.setupUi(self)
        self.getFormReferences(new_form)  

    def getFormReferences(self, new_form):
        self.options_table = new_form.options_table

    def setData(self, positions):

        self.options_table.clearContents()
        self.options_table.setRowCount(len(positions.index))
        
        index = 0
        
        for _, position in positions.iterrows():
            
            mkt_value = position['PRICE'] * position['MULTIPLIER'] * position['COUNT']

            self.options_table.setItem(index, 0, QTableWidgetItem(position['INSTRUMENT']))
            self.options_table.setItem(index, 1, QTableWidgetItem(position['TYPE']))

            datetime_obj = datetime.strptime(position['EXPIRATION'], '%Y%m%d')
            expiration = datetime_obj.date().strftime("%d %B %Y")
            self.options_table.setItem(index, 2, QTableWidgetItem(expiration))
            self.options_table.setItem(index, 3, getNumericItem(position['STRIKE']))
            self.options_table.setItem(index, 4, getNumericItem(position['COUNT']))
            self.options_table.setItem(index, 5, getNumericItem(position['PRICE']))
            self.options_table.setItem(index, 6, getNumericItem(mkt_value))
            self.options_table.setItem(index, 7, getNumericItem(position['UNREALIZED_PNL']))
            
            index += 1


    def setupAlignment(self):

        delegate = AlignDelegate(self.options_table)
        price_delegate = PriceAlignDelegate(self.options_table)
        self.options_table.setItemDelegateForColumn(2, delegate)
        self.options_table.setItemDelegateForColumn(3, delegate)
        self.options_table.setItemDelegateForColumn(4, delegate)
        self.options_table.setItemDelegateForColumn(5, price_delegate)
        self.options_table.setItemDelegateForColumn(6, price_delegate)   
        self.options_table.setItemDelegateForColumn(7, price_delegate)   
        

class OptionTabWidgetExt(OptionTabWidget):


    def __init__(self):
        super().__init__()

        self.options_table.insertColumn(8)
        self.options_table.setHorizontalHeaderItem(8, QTableWidgetItem('DPNL'))
        
        
    def setData(self, positions):
        super().setData(positions)
        self.options_table.setRowCount(len(positions.index))
        
        index = 0
        
        for _, position in positions.iterrows():
            
            self.options_table.setItem(index, 7, getNumericItem(position['UPNL']))
            self.options_table.setItem(index, 8, getNumericItem(position['DPNL']))            
            index += 1


    def setupAlignment(self):
        super().setupAlignment()
        delegate = PriceAlignDelegate(self.options_table)
        self.options_table.setItemDelegateForColumn(7, delegate)
        self.options_table.setItemDelegateForColumn(8, delegate)   
    

class SpecOptionTabWidget(OptionTabWidget):

    previous_price = 0.0
    total_value = 0.0
    text_updater = pyqtSignal(str)
    days_to_expiration = float("inf")

    def setupUi(self):
        new_form = SpecOptionsTab() 
        new_form.setupUi(self)
        self.getFormReferences(new_form)   
        self.individual = True     
        self.notes_window.textChanged.connect(self.textChanged)

    def textChanged(self):
        self.text_updater.emit(self.tab_name)

    def getNotesText(self):
        return self.notes_window.toPlainText()

    def getFormReferences(self, new_form):
        super().getFormReferences(new_form)
        self.days_till_label = new_form.days_till_label
        self.total_value_label = new_form.total_value_label
        self.unrealized_pnl_label = new_form.unrealized_pnl_label
        self.underlying_price_label = new_form.underlying_price_label
        self.notes_window = new_form.notes_window

    def setData(self, positions):
        super().setData(positions)

        unrealized_pnl = 0.0
        
        for _, position in positions.iterrows():
            unrealized_pnl += position['UNREALIZED_PNL']
            mkt_value = position['PRICE'] * position['MULTIPLIER'] * position['COUNT']
            self.total_value += mkt_value            

            datetime_obj = datetime.strptime(position['EXPIRATION'], '%Y%m%d')
            today = datetime.today()
            days_delta = (datetime_obj - today).days
            if days_delta < self.days_to_expiration:
                self.days_to_expiration = days_delta
        
        self.days_till_label.setText(str(self.days_to_expiration))
        self.total_value_label.setText("{:.2f}".format(self.total_value))
        self.setPNLPosition(unrealized_pnl)

        

    def setPrice(self, price):
        if self.previous_price != 0.0:
            if self.previous_price > price:
                self.underlying_price_label.setText('<font color="red">' + str(price) + '</font>')
            else:
                self.underlying_price_label.setText('<font color="green">' + str(price) + '</font>')
        else:
            self.underlying_price_label.setText(str(price))
        self.previous_price = price


    def setPNLPosition(self, unrealized_pnl):
        if unrealized_pnl > 0:
            self.unrealized_pnl_label.setText('<font color="green">' + "{:.2f}".format(unrealized_pnl) + '</font>')
        else:
            self.unrealized_pnl_label.setText('<font color="red">' + "{:.2f}".format(unrealized_pnl) + '</font>')
        

