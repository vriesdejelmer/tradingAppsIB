# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIComps/QTGeneration/StockPositionWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.position_button = QtWidgets.QPushButton(self.centralwidget)
        self.position_button.setObjectName("position_button")
        self.horizontalLayout_2.addWidget(self.position_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.option_value_label = QtWidgets.QLabel(self.tab)
        self.option_value_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.option_value_label.setObjectName("option_value_label")
        self.gridLayout_2.addWidget(self.option_value_label, 5, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 7, 2, 1, 1)
        self.short_value_label = QtWidgets.QLabel(self.tab)
        self.short_value_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.short_value_label.setObjectName("short_value_label")
        self.gridLayout_2.addWidget(self.short_value_label, 1, 8, 1, 1)
        self.short_dpnl_label = QtWidgets.QLabel(self.tab)
        self.short_dpnl_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.short_dpnl_label.setObjectName("short_dpnl_label")
        self.gridLayout_2.addWidget(self.short_dpnl_label, 3, 8, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 8, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 2, 1, 1)
        self.long_dpnl_label = QtWidgets.QLabel(self.tab)
        self.long_dpnl_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.long_dpnl_label.setObjectName("long_dpnl_label")
        self.gridLayout_2.addWidget(self.long_dpnl_label, 3, 3, 1, 1)
        self.overall_upnl_label = QtWidgets.QLabel(self.tab)
        self.overall_upnl_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.overall_upnl_label.setObjectName("overall_upnl_label")
        self.gridLayout_2.addWidget(self.overall_upnl_label, 13, 8, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 7, 1, 1)
        self.short_upnl_label = QtWidgets.QLabel(self.tab)
        self.short_upnl_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.short_upnl_label.setObjectName("short_upnl_label")
        self.gridLayout_2.addWidget(self.short_upnl_label, 2, 8, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 5, 5, 1, 1)
        self.overall_dpnl_label = QtWidgets.QLabel(self.tab)
        self.overall_dpnl_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.overall_dpnl_label.setObjectName("overall_dpnl_label")
        self.gridLayout_2.addWidget(self.overall_dpnl_label, 14, 8, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 12, 5, 1, 1)
        self.hodl_dpnl_label = QtWidgets.QLabel(self.tab)
        self.hodl_dpnl_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hodl_dpnl_label.setObjectName("hodl_dpnl_label")
        self.gridLayout_2.addWidget(self.hodl_dpnl_label, 8, 8, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 3, 2, 1, 1)
        self.hodl_upnl_label = QtWidgets.QLabel(self.tab)
        self.hodl_upnl_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hodl_upnl_label.setObjectName("hodl_upnl_label")
        self.gridLayout_2.addWidget(self.hodl_upnl_label, 7, 8, 1, 1)
        self.hodl_value_label = QtWidgets.QLabel(self.tab)
        self.hodl_value_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hodl_value_label.setObjectName("hodl_value_label")
        self.gridLayout_2.addWidget(self.hodl_value_label, 5, 8, 1, 1)
        self.long_upnl_label = QtWidgets.QLabel(self.tab)
        self.long_upnl_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.long_upnl_label.setObjectName("long_upnl_label")
        self.gridLayout_2.addWidget(self.long_upnl_label, 2, 3, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 7, 7, 1, 1)
        self.long_value_label = QtWidgets.QLabel(self.tab)
        self.long_value_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.long_value_label.setObjectName("long_value_label")
        self.gridLayout_2.addWidget(self.long_value_label, 1, 3, 1, 1)
        self.option_upnl_label = QtWidgets.QLabel(self.tab)
        self.option_upnl_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.option_upnl_label.setObjectName("option_upnl_label")
        self.gridLayout_2.addWidget(self.option_upnl_label, 7, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 11, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.tab)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 13, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 7, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 5, 7, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 14, 7, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.ratio_label = QtWidgets.QLabel(self.tab)
        self.ratio_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ratio_label.setObjectName("ratio_label")
        self.gridLayout_2.addWidget(self.ratio_label, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 5, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 12, 7, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 8, 7, 1, 1)
        self.account_value_label = QtWidgets.QLabel(self.tab)
        self.account_value_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.account_value_label.setObjectName("account_value_label")
        self.gridLayout_2.addWidget(self.account_value_label, 12, 8, 1, 1)
        self.option_dpnl_label = QtWidgets.QLabel(self.tab)
        self.option_dpnl_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.option_dpnl_label.setObjectName("option_dpnl_label")
        self.gridLayout_2.addWidget(self.option_dpnl_label, 8, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 3, 7, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 6, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.position_button.setText(_translate("MainWindow", "Positions"))
        self.option_value_label.setText(_translate("MainWindow", "0.0"))
        self.label_24.setText(_translate("MainWindow", "UPNL"))
        self.short_value_label.setText(_translate("MainWindow", "0.0"))
        self.short_dpnl_label.setText(_translate("MainWindow", "0.0"))
        self.label_23.setText(_translate("MainWindow", "Daily PNL"))
        self.label_5.setText(_translate("MainWindow", "Long Trades"))
        self.label_2.setText(_translate("MainWindow", "UPNL"))
        self.long_dpnl_label.setText(_translate("MainWindow", "0.0"))
        self.overall_upnl_label.setText(_translate("MainWindow", "0.0"))
        self.label_7.setText(_translate("MainWindow", "UPNL"))
        self.short_upnl_label.setText(_translate("MainWindow", "0.0"))
        self.label_13.setText(_translate("MainWindow", "Hodl"))
        self.overall_dpnl_label.setText(_translate("MainWindow", "0.0"))
        self.label_14.setText(_translate("MainWindow", "Account"))
        self.hodl_dpnl_label.setText(_translate("MainWindow", "0.0"))
        self.label_18.setText(_translate("MainWindow", "Daily PNL"))
        self.hodl_upnl_label.setText(_translate("MainWindow", "0.0"))
        self.hodl_value_label.setText(_translate("MainWindow", "0.0"))
        self.long_upnl_label.setText(_translate("MainWindow", "0.0"))
        self.label_26.setText(_translate("MainWindow", "UPNL"))
        self.long_value_label.setText(_translate("MainWindow", "0.0"))
        self.option_upnl_label.setText(_translate("MainWindow", "0.0"))
        self.label_30.setText(_translate("MainWindow", "UPNL"))
        self.label_3.setText(_translate("MainWindow", "Value"))
        self.label_11.setText(_translate("MainWindow", "Value"))
        self.label_31.setText(_translate("MainWindow", "Daily PNL"))
        self.ratio_label.setText(_translate("MainWindow", "Option Trades"))
        self.label_4.setText(_translate("MainWindow", "Short Trades"))
        self.label_16.setText(_translate("MainWindow", "Value"))
        self.label.setText(_translate("MainWindow", "Value"))
        self.label_27.setText(_translate("MainWindow", "Daily PNL"))
        self.account_value_label.setText(_translate("MainWindow", "0.0"))
        self.option_dpnl_label.setText(_translate("MainWindow", "0.0"))
        self.label_6.setText(_translate("MainWindow", "Value"))
        self.label_20.setText(_translate("MainWindow", "Daily PNL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Overview"))
