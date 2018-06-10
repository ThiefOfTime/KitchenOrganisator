# -*- coding: utf-8 -*-
"""
Created on Apr 24, 2018
@author: ThiefOfTime
"""

import sys
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import queue
import threading

# PySide imports
try:
    from PySide.QtGui import QMainWindow, QPixmap, QApplication, QImage
    from PySide.QtCore import QTimer
except ModuleNotFoundError:
    from PySide2.QtGui import QPixmap, QImage
    from PySide2.QtWidgets import QMainWindow, QApplication
    from PySide2.QtCore import QTimer


# import start screen gui
import fridayUI.start_screen_gui as st

# import other windows
from fridayUI.new_rcp_gui_func import NewRecipe
from fridayUI.kitchen_gui_func import Kitchen
from fridayUI.inventory_gui_func import Inventory

# import hive connection
from hive.SQLHiveConnection import DatabaseConnector

# TODO: documentation
class Start(QMainWindow, st.Ui_Start):

    def __init__(self):
        super(Start, self).__init__()
        self.setupUi(self)

        #self.rec_ex = NewRecipe()
        hive_connection = DatabaseConnector()
        self.inventory = Inventory(hive_connection)
        self.ktch_ex = Kitchen(self, hive_connection)
        self.kitchen_bt.clicked.connect(self.show_kitchen)
        self.rec_bt.clicked.connect(self.show_new_recipe)

    def show_kitchen(self):
        self.hide()
        self.ktch_ex.show()

    def show_new_recipe(self):
        self.hide()
        self.inventory.show()
        #self.rec_ex.show()


def main():
    app = QApplication(sys.argv)
    ex_start = Start()
    ex_start.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

