# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weekly_add_input_dialoq.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class WeeklyAddInputDialoq(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(721, 380)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 9, 721, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.message_lb = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.message_lb.setFont(font)
        self.message_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.message_lb.setObjectName("message_lb")
        self.verticalLayout.addWidget(self.message_lb)
        self.name_lb = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name_lb.setObjectName("name_lb")
        self.verticalLayout.addWidget(self.name_lb)
        self.name_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.name_le.setObjectName("name_le")
        self.verticalLayout.addWidget(self.name_le)
        self.links_lb = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.links_lb.setObjectName("links_lb")
        self.verticalLayout.addWidget(self.links_lb)
        self.links_lw = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.links_lw.setObjectName("links_lw")
        self.verticalLayout.addWidget(self.links_lw)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancel_bt.setObjectName("cancel_bt")
        self.horizontalLayout.addWidget(self.cancel_bt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.accept_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.accept_bt.setObjectName("accept_bt")
        self.horizontalLayout.addWidget(self.accept_bt)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.message_lb.setText(_translate("Form", "DummyText"))
        self.name_lb.setText(_translate("Form", "Name"))
        self.links_lb.setText(_translate("Form", "Links"))
        self.cancel_bt.setText(_translate("Form", "Cancel"))
        self.accept_bt.setText(_translate("Form", "Accept"))

