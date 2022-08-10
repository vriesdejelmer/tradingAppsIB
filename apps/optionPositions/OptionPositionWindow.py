# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionsGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import numpy as np
from uiComps.qtGeneration.Position_UI import Ui_MainWindow as Position_UI
import sys
from dataComps.Constants import OrderType, Constants
from uiComps.QHelper import Validator, find_nearest


class OptionPositionWindow(QMainWindow, Position_UI):

    def __init__(self):
        QMainWindow.__init__(self)
        Position_UI.__init__(self)

        self.setupUi(self)

        # self.populateBoxes()
        # self.setupGraphs()
        self.setupActions()
        # self.disableInterface() 
        
    def setupActions(self):
        self.position_button.clicked.connect(self.fetchPositions)
        self.expiration_button.clicked.connect(self.orderExpiration)
        self.value_button.clicked.connect(self.orderValue)
        self.type_button.clicked.connect(self.orderExpiration)


