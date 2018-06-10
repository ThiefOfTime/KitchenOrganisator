# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventory.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Inventory(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(669, 443)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 671, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.win_lb = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.win_lb.setFont(font)
        self.win_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.win_lb.setObjectName("win_lb")
        self.verticalLayout.addWidget(self.win_lb)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bar_c_lb = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.bar_c_lb.setObjectName("bar_c_lb")
        self.horizontalLayout.addWidget(self.bar_c_lb)
        self.code_ed = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.code_ed.setObjectName("code_ed")
        self.horizontalLayout.addWidget(self.code_ed)
        self.add_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_bt.setObjectName("add_bt")
        self.horizontalLayout.addWidget(self.add_bt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.code_tbl = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.code_tbl.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.code_tbl.setObjectName("code_tbl")
        self.code_tbl.setColumnCount(0)
        self.code_tbl.setRowCount(0)
        self.verticalLayout.addWidget(self.code_tbl)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancel_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancel_bt.setObjectName("cancel_bt")
        self.horizontalLayout_2.addWidget(self.cancel_bt)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.save_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_bt.setObjectName("save_bt")
        self.horizontalLayout_2.addWidget(self.save_bt)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.win_lb.setText(_translate("Form", "Inventory"))
        self.bar_c_lb.setText(_translate("Form", "Bar Code: "))
        self.code_ed.setPlaceholderText(_translate("Form", "Please enter a barcode ...."))
        self.add_bt.setText(_translate("Form", "Add"))
        self.cancel_bt.setText(_translate("Form", "Cancel"))
        self.save_bt.setText(_translate("Form", "Save"))

