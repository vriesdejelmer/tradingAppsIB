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
from uiComps.qtGeneration.DataDownloader_UI import Ui_MainWindow as DataDownloader_UI
import sys
from dataComps.Constants import OrderType, Constants

from generalFunctionality.SymbolFinderImpl import SymbolFinderImplementation
from generalFunctionality.UIFunctions import findRowForValue, AlignDelegate, PercAlignDelegate

from math import log10


class DataDownloaderWindow(QMainWindow, DataDownloader_UI, SymbolFinderImplementation):

    bar_types = ["1 min", "2 mins", "3 mins", "5 mins", "15 mins", "30 mins", "1 hour", "1 day"]

    current_selection = None

    def __init__(self):
        QMainWindow.__init__(self)
        DataDownloader_UI.__init__(self)
        SymbolFinderImplementation.__init__(self)

        self.setupUi(self)
        self.forceUpperCase()
        self.connectSearchField()
        self.connectActions()
        self.fillOutFields()

    def connectActions(self):
        self.fetch_button.clicked.connect(self.fetchHistoricalData)

    def fillOutFields(self):
        self.bar_combobox.addItems(self.bar_types)

        self.bar_combobox.setCurrentIndex(self.bar_combobox.count()-1)
    
    def dataUpdate(self, signal):
        print(f"DataDownloaderWindow.dataUpdate: {signal}")
        self.contractUpdate(signal)

