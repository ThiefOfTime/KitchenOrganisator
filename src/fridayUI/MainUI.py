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
from PySide.QtGui import QMainWindow, QPixmap, QApplication, QImage
from PySide.QtCore import QTimer

# import start screen gui
import fridayUI.start_screen_gui as st

# import other windows
from fridayUI.new_rcp_gui_func import NewRecipe
from fridayUI.kitchen_gui_func import Kitchen


# TODO: documentation
class Start(QMainWindow, st.Ui_Start):

    def __init__(self):
        super(Start, self).__init__()
        self.setupUi(self)

        self.rec_ex = NewRecipe()
        self.ktch_ex = Kitchen(self)
        self.kitchen_bt.clicked.connect(self.show_kitchen)
        self.rec_bt.clicked.connect(self.show_new_recipe)

    def show_kitchen(self):
        self.hide()
        self.ktch_ex.show()

    def show_new_recipe(self):
        self.hide()
        self.rec_ex.show()


def main():
    app = QApplication(sys.argv)
    ex_start = Start()
    ex_start.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
