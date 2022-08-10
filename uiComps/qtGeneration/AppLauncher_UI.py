# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIComps/QTGeneration/AppLauncher.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 649)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(20, 20, 20, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(132, 132, 132, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_2.setPalette(palette)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.socket_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.socket_line.sizePolicy().hasHeightForWidth())
        self.socket_line.setSizePolicy(sizePolicy)
        self.socket_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.socket_line.setObjectName("socket_line")
        self.gridLayout.addWidget(self.socket_line, 2, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.open_downloader = QtWidgets.QPushButton(self.centralwidget)
        self.open_downloader.setObjectName("open_downloader")
        self.app_group = QtWidgets.QButtonGroup(MainWindow)
        self.app_group.setObjectName("app_group")
        self.app_group.addButton(self.open_downloader)
        self.gridLayout.addWidget(self.open_downloader, 4, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.real_button = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.real_button.sizePolicy().hasHeightForWidth())
        self.real_button.setSizePolicy(sizePolicy)
        self.real_button.setObjectName("real_button")
        self.trading_type_group = QtWidgets.QButtonGroup(MainWindow)
        self.trading_type_group.setObjectName("trading_type_group")
        self.trading_type_group.addButton(self.real_button)
        self.horizontalLayout.addWidget(self.real_button)
        self.paper_button = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paper_button.sizePolicy().hasHeightForWidth())
        self.paper_button.setSizePolicy(sizePolicy)
        self.paper_button.setObjectName("paper_button")
        self.trading_type_group.addButton(self.paper_button)
        self.horizontalLayout.addWidget(self.paper_button)
        self.custom_button = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_button.sizePolicy().hasHeightForWidth())
        self.custom_button.setSizePolicy(sizePolicy)
        self.custom_button.setObjectName("custom_button")
        self.trading_type_group.addButton(self.custom_button)
        self.horizontalLayout.addWidget(self.custom_button)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(132, 132, 132, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label.setPalette(palette)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.open_stocks = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_stocks.sizePolicy().hasHeightForWidth())
        self.open_stocks.setSizePolicy(sizePolicy)
        self.open_stocks.setObjectName("open_stocks")
        self.app_group.addButton(self.open_stocks)
        self.gridLayout.addWidget(self.open_stocks, 1, 0, 1, 1)
        self.open_options = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_options.sizePolicy().hasHeightForWidth())
        self.open_options.setSizePolicy(sizePolicy)
        self.open_options.setObjectName("open_options")
        self.app_group.addButton(self.open_options)
        self.gridLayout.addWidget(self.open_options, 2, 0, 1, 1)
        self.open_movers = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_movers.sizePolicy().hasHeightForWidth())
        self.open_movers.setSizePolicy(sizePolicy)
        self.open_movers.setObjectName("open_movers")
        self.app_group.addButton(self.open_movers)
        self.gridLayout.addWidget(self.open_movers, 3, 0, 1, 1)
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setObjectName("address_label")
        self.gridLayout.addWidget(self.address_label, 1, 3, 1, 1)
        self.open_symbol = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_symbol.sizePolicy().hasHeightForWidth())
        self.open_symbol.setSizePolicy(sizePolicy)
        self.open_symbol.setObjectName("open_symbol")
        self.app_group.addButton(self.open_symbol)
        self.gridLayout.addWidget(self.open_symbol, 4, 0, 1, 1)
        self.socket_label = QtWidgets.QLabel(self.centralwidget)
        self.socket_label.setObjectName("socket_label")
        self.gridLayout.addWidget(self.socket_label, 2, 3, 1, 1)
        self.address_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.address_line.sizePolicy().hasHeightForWidth())
        self.address_line.setSizePolicy(sizePolicy)
        self.address_line.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.address_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.address_line.setClearButtonEnabled(True)
        self.address_line.setObjectName("address_line")
        self.gridLayout.addWidget(self.address_line, 1, 5, 1, 1)
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connect_button.sizePolicy().hasHeightForWidth())
        self.connect_button.setSizePolicy(sizePolicy)
        self.connect_button.setObjectName("connect_button")
        self.gridLayout.addWidget(self.connect_button, 3, 5, 1, 1)
        self.fetch_rates = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fetch_rates.sizePolicy().hasHeightForWidth())
        self.fetch_rates.setSizePolicy(sizePolicy)
        self.fetch_rates.setObjectName("fetch_rates")
        self.gridLayout.addWidget(self.fetch_rates, 3, 3, 1, 1)
        self.open_stepper = QtWidgets.QPushButton(self.centralwidget)
        self.open_stepper.setObjectName("open_stepper")
        self.app_group.addButton(self.open_stepper)
        self.gridLayout.addWidget(self.open_stepper, 3, 1, 1, 1)
        self.open_rsi_tracker = QtWidgets.QPushButton(self.centralwidget)
        self.open_rsi_tracker.setObjectName("open_rsi_tracker")
        self.app_group.addButton(self.open_rsi_tracker)
        self.gridLayout.addWidget(self.open_rsi_tracker, 2, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(5, 2)
        self.gridLayout.setRowStretch(0, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.log_window = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.log_window.setObjectName("log_window")
        self.verticalLayout.addWidget(self.log_window)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Launch Manager"))
        self.label_2.setText(_translate("MainWindow", "Connection:"))
        self.open_downloader.setText(_translate("MainWindow", "Data Downloader"))
        self.real_button.setText(_translate("MainWindow", "Real"))
        self.paper_button.setText(_translate("MainWindow", "Paper"))
        self.custom_button.setText(_translate("MainWindow", "Custom"))
        self.label.setText(_translate("MainWindow", "Apps:"))
        self.open_stocks.setText(_translate("MainWindow", "Stock Positions"))
        self.open_options.setText(_translate("MainWindow", "Option Positions"))
        self.open_movers.setText(_translate("MainWindow", "Movers"))
        self.address_label.setText(_translate("MainWindow", "Local Address"))
        self.open_symbol.setText(_translate("MainWindow", "List Manager"))
        self.socket_label.setText(_translate("MainWindow", "Socket"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.fetch_rates.setText(_translate("MainWindow", "Fetch Short Rates"))
        self.open_stepper.setText(_translate("MainWindow", "StairStepper"))
        self.open_rsi_tracker.setText(_translate("MainWindow", "RSI Tracker"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
