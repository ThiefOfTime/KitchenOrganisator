# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

try:
    from PySide import QtCore, QtGui
except ImportError:
    from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NewRecipe(object):
    def setupUi(self, MainWindow):

        # MainWindow setup
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(856, 700)

        # setting Size Policy
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        # QWidget instanz
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        # setting first layouts
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 841, 641))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        # Adress Edit line
        self.adress_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adress_edit.sizePolicy().hasHeightForWidth())
        self.adress_edit.setSizePolicy(sizePolicy)
        self.adress_edit.setObjectName(_fromUtf8("adress_edit"))
        self.horizontalLayout.addWidget(self.adress_edit)

        # Search Button
        self.start_search_button = QtGui.QToolButton(self.verticalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_search_button.setIcon(icon)
        self.start_search_button.setIconSize(QtCore.QSize(32, 32))
        self.start_search_button.setObjectName(_fromUtf8("start_search_button"))
        self.horizontalLayout.addWidget(self.start_search_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # Tab Widget
        self.tabWidget = QtGui.QTabWidget(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.rec_tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rec_tab.sizePolicy().hasHeightForWidth())
        self.rec_tab.setSizePolicy(sizePolicy)
        self.rec_tab.setObjectName(_fromUtf8("rec_tab"))

        # Tab1 (rec_tab) Layouts
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.rec_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 821, 506))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        # Recipe options Radio Buttons
        self.pos1_rb = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.pos1_rb.setObjectName(_fromUtf8("pos1_rb"))
        self.horizontalLayout_2.addWidget(self.pos1_rb)
        self.pos2_rb = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.pos2_rb.setObjectName(_fromUtf8("pos2_rb"))
        self.horizontalLayout_2.addWidget(self.pos2_rb)
        self.pos3_rb = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.pos3_rb.setObjectName(_fromUtf8("pos3_rb"))
        self.horizontalLayout_2.addWidget(self.pos3_rb)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        # Tab1 internal Layout
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))

        # Recipe Text Field
        self.rec_text = QtGui.QTextBrowser(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rec_text.sizePolicy().hasHeightForWidth())
        self.rec_text.setSizePolicy(sizePolicy)
        self.rec_text.setObjectName(_fromUtf8("rec_text"))
        self.horizontalLayout_5.addWidget(self.rec_text)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))

        # Portion Edit Text Field
        self.portion_edit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portion_edit.sizePolicy().hasHeightForWidth())
        self.portion_edit.setSizePolicy(sizePolicy)
        self.portion_edit.setObjectName(_fromUtf8("portion_edit"))
        self.verticalLayout_4.addWidget(self.portion_edit)

        self.line = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)

        # Preparation time stuff
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        # Preparation check box
        self.prep_check = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.prep_check.setText(_fromUtf8(""))
        self.prep_check.setObjectName(_fromUtf8("prep_check"))
        self.horizontalLayout_6.addWidget(self.prep_check)
        # Preparation Text edit
        self.prep_edit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prep_edit.sizePolicy().hasHeightForWidth())
        self.prep_edit.setSizePolicy(sizePolicy)
        self.prep_edit.setObjectName(_fromUtf8("prep_edit"))
        self.horizontalLayout_6.addWidget(self.prep_edit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_4.addWidget(self.line_2)

        # Cooking time stuff
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        # Cooking check box
        self.cook_check = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.cook_check.setText(_fromUtf8(""))
        self.cook_check.setObjectName(_fromUtf8("cook_check"))
        self.horizontalLayout_7.addWidget(self.cook_check)
        self.cook_edit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cook_edit.sizePolicy().hasHeightForWidth())
        self.cook_edit.setSizePolicy(sizePolicy)
        # Cooking edit
        self.cook_edit.setObjectName(_fromUtf8("cook_edit"))
        self.horizontalLayout_7.addWidget(self.cook_edit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.line_3 = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_4.addWidget(self.line_3)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_2)

        # Baking time stuff
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        # Baking check box
        self.baking_check = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.baking_check.setText(_fromUtf8(""))
        self.baking_check.setObjectName(_fromUtf8("baking_check"))
        self.horizontalLayout_8.addWidget(self.baking_check)
        self.baking_edit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baking_edit.sizePolicy().hasHeightForWidth())
        # Baking Text Edit
        self.baking_edit.setSizePolicy(sizePolicy)
        self.baking_edit.setObjectName(_fromUtf8("baking_edit"))
        self.horizontalLayout_8.addWidget(self.baking_edit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.line_4 = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_4.addWidget(self.line_4)

        # Resting time stuff
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        # Resting time check box
        self.rest_check = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.rest_check.setText(_fromUtf8(""))
        self.rest_check.setObjectName(_fromUtf8("rest_check"))
        self.horizontalLayout_9.addWidget(self.rest_check)
        self.rest_edit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rest_edit.sizePolicy().hasHeightForWidth())
        # Resting text edit
        self.rest_edit.setSizePolicy(sizePolicy)
        self.rest_edit.setObjectName(_fromUtf8("rest_edit"))
        self.horizontalLayout_9.addWidget(self.rest_edit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.line_5 = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_4.addWidget(self.line_5)

        # Cooling time stuff
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        # Cooling check box
        self.cool_check = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.cool_check.setText(_fromUtf8(""))
        self.cool_check.setObjectName(_fromUtf8("cool_check"))
        self.horizontalLayout_10.addWidget(self.cool_check)
        self.cool_edit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cool_edit.sizePolicy().hasHeightForWidth())
        # Cooling text edit
        self.cool_edit.setSizePolicy(sizePolicy)
        self.cool_edit.setObjectName(_fromUtf8("cool_edit"))
        self.horizontalLayout_10.addWidget(self.cool_edit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.line_6 = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_4.addWidget(self.line_6)

        # Freezing time stuff
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        # Freezing check box
        self.freeze_check = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.freeze_check.setText(_fromUtf8(""))
        self.freeze_check.setObjectName(_fromUtf8("freeze_check"))
        self.horizontalLayout_11.addWidget(self.freeze_check)
        self.freeze_edit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freeze_edit.sizePolicy().hasHeightForWidth())
        # Freezing text edit
        self.freeze_edit.setSizePolicy(sizePolicy)
        self.freeze_edit.setObjectName(_fromUtf8("freeze_edit"))
        self.horizontalLayout_11.addWidget(self.freeze_edit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.rec_tab, _fromUtf8(""))

        # Ingredients Tab
        self.ingr_tab = QtGui.QWidget()
        self.ingr_tab.setObjectName(_fromUtf8("ingr_tab"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.ingr_tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 831, 501))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))

        # Tab2 options radio buttons
        self.pos1_irb = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.pos1_irb.setObjectName(_fromUtf8("pos1_irb"))
        self.horizontalLayout_4.addWidget(self.pos1_irb)
        self.pos2_irb = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.pos2_irb.setObjectName(_fromUtf8("pos2_irb"))
        self.horizontalLayout_4.addWidget(self.pos2_irb)
        self.pos3_irb = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.pos3_irb.setObjectName(_fromUtf8("pos3_irb"))
        self.horizontalLayout_4.addWidget(self.pos3_irb)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.ingr_text = QtGui.QTextBrowser(self.verticalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ingr_text.sizePolicy().hasHeightForWidth())

        # Tab2 Ingredients Text
        self.ingr_text.setSizePolicy(sizePolicy)
        self.ingr_text.setObjectName(_fromUtf8("ingr_text"))
        self.verticalLayout_3.addWidget(self.ingr_text)
        self.tabWidget.addTab(self.ingr_tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))

        # Cancel Button
        self.cancel_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout_3.addWidget(self.cancel_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)

        # Recipe Name edit
        self.name_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.name_edit.setObjectName(_fromUtf8("name_edit"))
        self.horizontalLayout_3.addWidget(self.name_edit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)

        # Save Button
        self.save_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.horizontalLayout_3.addWidget(self.save_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.adress_edit.setPlaceholderText(_translate("MainWindow", "Insert the recipe link here", None))
        self.start_search_button.setText(_translate("MainWindow", "...", None))
        self.pos1_rb.setText(_translate("MainWindow", "Option 1", None))
        self.pos2_rb.setText(_translate("MainWindow", "Option 2", None))
        self.pos3_rb.setText(_translate("MainWindow", "Option 3", None))
        self.portion_edit.setPlaceholderText(_translate("MainWindow", "Number of Portions", None))
        self.label.setText(_translate("MainWindow", "Preparation Time", None))
        self.prep_edit.setPlaceholderText(_translate("MainWindow", "None", None))
        self.label_2.setText(_translate("MainWindow", "Cooking Time", None))
        self.cook_edit.setPlaceholderText(_translate("MainWindow", "None", None))
        self.label_3.setText(_translate("MainWindow", "Baking Time", None))
        self.baking_edit.setPlaceholderText(_translate("MainWindow", "None", None))
        self.label_4.setText(_translate("MainWindow", "Resting Time", None))
        self.rest_edit.setPlaceholderText(_translate("MainWindow", "None", None))
        self.label_5.setText(_translate("MainWindow", "Cooling Time", None))
        self.cool_edit.setPlaceholderText(_translate("MainWindow", "None", None))
        self.label_6.setText(_translate("MainWindow", "Freezing Time", None))
        self.freeze_edit.setPlaceholderText(_translate("MainWindow", "None", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rec_tab), _translate("MainWindow", "Recipe", None))
        self.pos1_irb.setText(_translate("MainWindow", "Option 1", None))
        self.pos2_irb.setText(_translate("MainWindow", "Option 2", None))
        self.pos3_irb.setText(_translate("MainWindow", "Option 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ingr_tab), _translate("MainWindow", "Ingredients", None))
        self.cancel_button.setText(_translate("MainWindow", "Cancel", None))
        self.name_edit.setPlaceholderText(_translate("MainWindow", "Enter the recipe Name", None))
        self.save_button.setText(_translate("MainWindow", "Save", None))

