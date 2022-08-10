# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIComps/OptionWindow.ui'
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
        self.search_field = QtWidgets.QLineEdit(self.centralwidget)
        self.search_field.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.search_field.setClearButtonEnabled(True)
        self.search_field.setObjectName("search_field")
        self.gridLayout.addWidget(self.search_field, 1, 0, 1, 1)
        self.lower_box = StrikeSpinBox(self.centralwidget)
        self.lower_box.setMaximum(10)
        self.lower_box.setObjectName("lower_box")
        self.gridLayout.addWidget(self.lower_box, 1, 2, 1, 1)
        self.upper_box = StrikeSpinBox(self.centralwidget)
        self.upper_box.setObjectName("upper_box")
        self.gridLayout.addWidget(self.upper_box, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.upper_label = QtWidgets.QLabel(self.centralwidget)
        self.upper_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.upper_label.setObjectName("upper_label")
        self.gridLayout.addWidget(self.upper_label, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.percentage_label = QtWidgets.QLabel(self.centralwidget)
        self.percentage_label.setObjectName("percentage_label")
        self.gridLayout.addWidget(self.percentage_label, 7, 3, 1, 1)
        self.search_label = QtWidgets.QLabel(self.centralwidget)
        self.search_label.setObjectName("search_label")
        self.gridLayout.addWidget(self.search_label, 0, 0, 1, 1)
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setObjectName("connect_button")
        self.gridLayout.addWidget(self.connect_button, 0, 3, 1, 1)
        self.price_label = QtWidgets.QLabel(self.centralwidget)
        self.price_label.setObjectName("price_label")
        self.gridLayout.addWidget(self.price_label, 7, 2, 1, 1)
        self.structure_type = QtWidgets.QComboBox(self.centralwidget)
        self.structure_type.setObjectName("structure_type")
        self.gridLayout.addWidget(self.structure_type, 3, 0, 1, 1)
        self.expiration_box = QtWidgets.QComboBox(self.centralwidget)
        self.expiration_box.setObjectName("expiration_box")
        self.gridLayout.addWidget(self.expiration_box, 0, 2, 1, 1)
        self.lower_label = QtWidgets.QLabel(self.centralwidget)
        self.lower_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lower_label.setObjectName("lower_label")
        self.gridLayout.addWidget(self.lower_label, 1, 1, 1, 1)
        self.paper_trading_button = QtWidgets.QCheckBox(self.centralwidget)
        self.paper_trading_button.setObjectName("paper_trading_button")
        self.gridLayout.addWidget(self.paper_trading_button, 1, 3, 1, 1)
        self.middle_box = StrikeSpinBox(self.centralwidget)
        self.middle_box.setObjectName("middle_box")
        self.gridLayout.addWidget(self.middle_box, 2, 2, 1, 1)
        self.symbol_label = QtWidgets.QLabel(self.centralwidget)
        self.symbol_label.setObjectName("symbol_label")
        self.gridLayout.addWidget(self.symbol_label, 7, 0, 1, 1)
        self.expiration_label = QtWidgets.QLabel(self.centralwidget)
        self.expiration_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.expiration_label.setObjectName("expiration_label")
        self.gridLayout.addWidget(self.expiration_label, 0, 1, 1, 1)
        self.middle_label = QtWidgets.QLabel(self.centralwidget)
        self.middle_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.middle_label.setObjectName("middle_label")
        self.gridLayout.addWidget(self.middle_label, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.call_button = QtWidgets.QRadioButton(self.centralwidget)
        self.call_button.setObjectName("call_button")
        self.call_put_group = QtWidgets.QButtonGroup(MainWindow)
        self.call_put_group.setObjectName("call_put_group")
        self.call_put_group.addButton(self.call_button)
        self.horizontalLayout.addWidget(self.call_button)
        self.put_button = QtWidgets.QRadioButton(self.centralwidget)
        self.put_button.setObjectName("put_button")
        self.call_put_group.addButton(self.put_button)
        self.horizontalLayout.addWidget(self.put_button)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 3, 1, 1)
        self.snapshot_button = QtWidgets.QCheckBox(self.centralwidget)
        self.snapshot_button.setObjectName("snapshot_button")
        self.gridLayout.addWidget(self.snapshot_button, 3, 3, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.verticalLayout.addLayout(self.gridLayout)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Structure:"))
        self.upper_label.setText(_translate("MainWindow", "Upper"))
        self.percentage_label.setText(_translate("MainWindow", "%"))
        self.search_label.setText(_translate("MainWindow", "Symbol"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.price_label.setText(_translate("MainWindow", "PRICE"))
        self.lower_label.setText(_translate("MainWindow", "Lower"))
        self.paper_trading_button.setText(_translate("MainWindow", "Paper Trading"))
        self.symbol_label.setText(_translate("MainWindow", "SYMBOL"))
        self.expiration_label.setText(_translate("MainWindow", "Expiration"))
        self.middle_label.setText(_translate("MainWindow", "Middle"))
        self.call_button.setText(_translate("MainWindow", "Call"))
        self.put_button.setText(_translate("MainWindow", "Put"))
        self.snapshot_button.setText(_translate("MainWindow", "Snapshot"))
from UIComps.CustomWidgets.StrikeSpinBox import StrikeSpinBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())