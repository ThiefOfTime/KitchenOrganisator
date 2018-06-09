# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kitchen_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Kitchen(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(971, 632)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 971, 631))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.time_lcd = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_lcd.sizePolicy().hasHeightForWidth())
        self.time_lcd.setSizePolicy(sizePolicy)
        self.time_lcd.setObjectName("time_lcd")
        self.gridLayout.addWidget(self.time_lcd, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timer_dial = QtWidgets.QDial(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timer_dial.sizePolicy().hasHeightForWidth())
        self.timer_dial.setSizePolicy(sizePolicy)
        self.timer_dial.setMaximum(300)
        self.timer_dial.setObjectName("timer_dial")
        self.horizontalLayout.addWidget(self.timer_dial)
        self.timer_lcd = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timer_lcd.sizePolicy().hasHeightForWidth())
        self.timer_lcd.setSizePolicy(sizePolicy)
        self.timer_lcd.setObjectName("timer_lcd")
        self.horizontalLayout.addWidget(self.timer_lcd)
        self.timer_bt = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timer_bt.sizePolicy().hasHeightForWidth())
        self.timer_bt.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../.designer/backup/icons/aperture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.timer_bt.setIcon(icon)
        self.timer_bt.setIconSize(QtCore.QSize(32, 32))
        self.timer_bt.setObjectName("timer_bt")
        self.horizontalLayout.addWidget(self.timer_bt)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancel_bt = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_bt.sizePolicy().hasHeightForWidth())
        self.cancel_bt.setSizePolicy(sizePolicy)
        self.cancel_bt.setObjectName("cancel_bt")
        self.horizontalLayout_3.addWidget(self.cancel_bt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.calorie_lcd = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calorie_lcd.sizePolicy().hasHeightForWidth())
        self.calorie_lcd.setSizePolicy(sizePolicy)
        self.calorie_lcd.setObjectName("calorie_lcd")
        self.horizontalLayout_4.addWidget(self.calorie_lcd)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.language_bt = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.language_bt.sizePolicy().hasHeightForWidth())
        self.language_bt.setSizePolicy(sizePolicy)
        self.language_bt.setMaximumSize(QtCore.QSize(38, 34))
        self.language_bt.setObjectName("language_bt")
        self.horizontalLayout_7.addWidget(self.language_bt)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 2, 1, 1)
        self.stuff_table = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stuff_table.sizePolicy().hasHeightForWidth())
        self.stuff_table.setSizePolicy(sizePolicy)
        self.stuff_table.setMaximumSize(QtCore.QSize(16777180, 16777215))
        self.stuff_table.setObjectName("stuff_table")
        self.stuff_table.setColumnCount(0)
        self.stuff_table.setRowCount(0)
        self.gridLayout.addWidget(self.stuff_table, 3, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.video_view = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_view.sizePolicy().hasHeightForWidth())
        self.video_view.setSizePolicy(sizePolicy)
        self.video_view.setMinimumSize(QtCore.QSize(350, 192))
        self.video_view.setMaximumSize(QtCore.QSize(350, 192))
        self.video_view.setObjectName("video_view")
        self.verticalLayout_2.addWidget(self.video_view)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(350, 3))
        self.line.setMaximumSize(QtCore.QSize(350, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.gloabal_tab = QtWidgets.QTabWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gloabal_tab.sizePolicy().hasHeightForWidth())
        self.gloabal_tab.setSizePolicy(sizePolicy)
        self.gloabal_tab.setObjectName("gloabal_tab")
        self.recipes_tab = QtWidgets.QWidget()
        self.recipes_tab.setObjectName("recipes_tab")
        self.recipe_list = QtWidgets.QListWidget(self.recipes_tab)
        self.recipe_list.setGeometry(QtCore.QRect(0, 0, 350, 291))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recipe_list.sizePolicy().hasHeightForWidth())
        self.recipe_list.setSizePolicy(sizePolicy)
        self.recipe_list.setMaximumSize(QtCore.QSize(350, 501))
        self.recipe_list.setObjectName("recipe_list")
        self.gloabal_tab.addTab(self.recipes_tab, "")
        self.weekly_tab = QtWidgets.QWidget()
        self.weekly_tab.setObjectName("weekly_tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.weekly_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 341, 281))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gridLayoutWidget_2)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.weekly_tw = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weekly_tw.sizePolicy().hasHeightForWidth())
        self.weekly_tw.setSizePolicy(sizePolicy)
        self.weekly_tw.setObjectName("weekly_tw")
        self.weekly_tw.setColumnCount(0)
        self.weekly_tw.setRowCount(0)
        self.verticalLayout_3.addWidget(self.weekly_tw)
        self.clear_bt = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_bt.sizePolicy().hasHeightForWidth())
        self.clear_bt.setSizePolicy(sizePolicy)
        self.clear_bt.setObjectName("clear_bt")
        self.verticalLayout_3.addWidget(self.clear_bt)
        self.gloabal_tab.addTab(self.weekly_tab, "")
        self.playlist_tab = QtWidgets.QWidget()
        self.playlist_tab.setObjectName("playlist_tab")
        self.playlist_lw = QtWidgets.QListWidget(self.playlist_tab)
        self.playlist_lw.setGeometry(QtCore.QRect(-10, 0, 361, 291))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlist_lw.sizePolicy().hasHeightForWidth())
        self.playlist_lw.setSizePolicy(sizePolicy)
        self.playlist_lw.setObjectName("playlist_lw")
        self.gloabal_tab.addTab(self.playlist_tab, "")
        self.verticalLayout_2.addWidget(self.gloabal_tab)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.stop_bt = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.stop_bt.setObjectName("stop_bt")
        self.horizontalLayout_5.addWidget(self.stop_bt)
        self.prev_bt = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.prev_bt.setObjectName("prev_bt")
        self.horizontalLayout_5.addWidget(self.prev_bt)
        self.play_pause_bt = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_pause_bt.sizePolicy().hasHeightForWidth())
        self.play_pause_bt.setSizePolicy(sizePolicy)
        self.play_pause_bt.setMaximumSize(QtCore.QSize(40, 40))
        self.play_pause_bt.setIconSize(QtCore.QSize(32, 32))
        self.play_pause_bt.setObjectName("play_pause_bt")
        self.horizontalLayout_5.addWidget(self.play_pause_bt)
        self.next_bt = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.next_bt.setObjectName("next_bt")
        self.horizontalLayout_5.addWidget(self.next_bt)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.search_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_le.sizePolicy().hasHeightForWidth())
        self.search_le.setSizePolicy(sizePolicy)
        self.search_le.setObjectName("search_le")
        self.horizontalLayout_6.addWidget(self.search_le)
        self.go_bt = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.go_bt.setObjectName("go_bt")
        self.horizontalLayout_6.addWidget(self.go_bt)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.cal_rad = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cal_rad.sizePolicy().hasHeightForWidth())
        self.cal_rad.setSizePolicy(sizePolicy)
        self.cal_rad.setChecked(True)
        self.cal_rad.setObjectName("cal_rad")
        self.verticalLayout.addWidget(self.cal_rad)
        self.show_emp_rad = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_emp_rad.sizePolicy().hasHeightForWidth())
        self.show_emp_rad.setSizePolicy(sizePolicy)
        self.show_emp_rad.setObjectName("show_emp_rad")
        self.verticalLayout.addWidget(self.show_emp_rad)
        self.show_rad = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_rad.sizePolicy().hasHeightForWidth())
        self.show_rad.setSizePolicy(sizePolicy)
        self.show_rad.setObjectName("show_rad")
        self.verticalLayout.addWidget(self.show_rad)
        self.bought_rb = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bought_rb.sizePolicy().hasHeightForWidth())
        self.bought_rb.setSizePolicy(sizePolicy)
        self.bought_rb.setObjectName("bought_rb")
        self.verticalLayout.addWidget(self.bought_rb)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.calculate_bt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.calculate_bt.setObjectName("calculate_bt")
        self.verticalLayout.addWidget(self.calculate_bt)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 2, 1)

        self.retranslateUi(Form)
        self.gloabal_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.timer_bt.setText(_translate("Form", "..."))
        self.cancel_bt.setText(_translate("Form", "Cancel"))
        self.label.setText(_translate("Form", "kcal"))
        self.label_2.setText(_translate("Form", "set Language:"))
        self.language_bt.setText(_translate("Form", "en"))
        self.gloabal_tab.setTabText(self.gloabal_tab.indexOf(self.recipes_tab), _translate("Form", "Recipes"))
        self.clear_bt.setText(_translate("Form", "Wipe List"))
        self.gloabal_tab.setTabText(self.gloabal_tab.indexOf(self.weekly_tab), _translate("Form", "Weekly Rota"))
        self.gloabal_tab.setTabText(self.gloabal_tab.indexOf(self.playlist_tab), _translate("Form", "Playlist"))
        self.stop_bt.setText(_translate("Form", "..."))
        self.prev_bt.setText(_translate("Form", "..."))
        self.play_pause_bt.setText(_translate("Form", "..."))
        self.next_bt.setText(_translate("Form", "..."))
        self.search_le.setPlaceholderText(_translate("Form", "Search ..."))
        self.go_bt.setText(_translate("Form", "..."))
        self.cal_rad.setText(_translate("Form", "Calories summation"))
        self.show_emp_rad.setText(_translate("Form", "Show stock (empty things)"))
        self.show_rad.setText(_translate("Form", "show stock (existing things)"))
        self.bought_rb.setText(_translate("Form", "Bought goods"))
        self.calculate_bt.setText(_translate("Form", "Calculate calories"))

