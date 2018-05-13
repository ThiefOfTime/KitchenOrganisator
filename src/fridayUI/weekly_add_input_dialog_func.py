# -*- coding: utf-8 -*-
"""
Created on Mai 11, 2018
@author: ThiefOfTime
"""

# PySide imports
from PySide.QtGui import QMainWindow

from fridayUI.weekly_add_input_dialoq import WeeklyAddInputDialoq


class MealInputDialog(QMainWindow, WeeklyAddInputDialoq):

    def __init__(self, window_name, message_text, name_text, links_text, buttons_text, return_func):
        super(MealInputDialog, self).__init__()
        self.setupUi(self)

        self.__return_function = return_func

        self.setWindowTitle(window_name)
        self.message_lb.setText(message_text)
        self.name_lb.setText(name_text)
        self.links_lb.setText(links_text)
        self.cancel_bt.setText(buttons_text[0])
        self.accept_bt.setText(buttons_text[1])

        # buttons
        self.cancel_bt.clicked.connect(self.cancel)
        self.accept_bt.clicked.connect(self.accept)

    def change_settings(self, window_name, message_text, name_text, links_text, buttons_text, return_function):
        '''
        changes the window settings
        :param window_name:
        :param message_text:
        :param name_text:
        :param links_text:
        :param buttons_text:
        :return:
        '''
        self.setWindowTitle(window_name)
        self.message_lb.setText(message_text)
        self.name_lb.setText(name_text)
        self.links_lb.setText(links_text)
        self.cancel_bt.setText(buttons_text[0])
        self.accept_bt.setText(buttons_text[1])
        self.__return_function = return_function

    def accept(self):
        '''
        accept function
        :return:
        '''
        list_items = []
        for i in range(self.links_lw.count()):
            list_items.append(self.links_lw.item(i))
        self.__return_function(self.name_le.text(), list_items)
        self.close()

    def cancel(self):
        '''
        cancel function
        :return:
        '''
        self.__return_function(None, None)
        self.close()

