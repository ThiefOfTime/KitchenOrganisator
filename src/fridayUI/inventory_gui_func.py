# -*- coding: utf-8 -*-
"""
Created on Jun 10, 2018
@author: ThiefOfTime
"""

import re
import cv2
import queue
import threading
import multiprocessing

# import kitchen gui
import fridayUI.inventory_gui as inventory

# import Hive modules
from hive.SQLHiveConnection import DatabaseConnector
from connections.HiveIO import RecipeReader
from fridayUI.weekly_add_input_dialog_func import MealInputDialog

# import PySide modules
try:
    from PySide.QtGui import QHeaderView, QListWidgetItem, QTableWidgetItem, QImage, QPixmap, QGraphicsPixmapItem, \
        QGraphicsScene, QWidget, QHBoxLayout, QToolButton, QLCDNumber, QInputDialog, QLineEdit, QIcon
    from PySide.QtCore import QTime, QTimer, QSize
    pyside_import = True
except ModuleNotFoundError:
    from PySide2.QtWidgets import QHeaderView, QListWidgetItem, QTableWidgetItem, QGraphicsPixmapItem, QGraphicsScene, \
        QWidget, QHBoxLayout, QToolButton, QLCDNumber, QInputDialog, QLineEdit, QMainWindow
    from PySide2.QtGui import QImage, QPixmap, QIcon, QColor
    from PySide2.QtCore import QTime, QTimer, QSize
    pyside_import = False


class Inventory(QMainWindow, inventory.Inventory):

    def __init__(self, hive_connection):
        super(Inventory, self).__init__()
        self.setupUi(self)

        # variables
        self.hive_connection = hive_connection

        # change attributes
        self.code_tbl.setRowCount(0)
        self.code_tbl.setColumnCount(4)
        if not pyside_import:
            self.code_tbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            self.code_tbl.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.code_tbl.setHorizontalHeaderLabels(['Volume', 'Unit', 'Name', 'Barcode'])

        self.code_ed.setFocus()

        self.code_ed.returnPressed.connect(self.bacode_scanned)

    def bacode_scanned(self):
        code_text = self.code_ed.text()
        if len(code_text.strip()) == 0:
            return
        self.code_ed.clear()
        row_count = self.code_tbl.rowCount()
        self.code_tbl.insertRow(row_count)
        self.code_tbl.setItem(row_count, 3, QTableWidgetItem(code_text))


