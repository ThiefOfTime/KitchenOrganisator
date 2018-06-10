# -*- coding: utf-8 -*-
"""
Created on Mai 11, 2018
@author: ThiefOfTime
"""

import re
import cv2
import queue
import threading
import multiprocessing

# import kitchen gui
import fridayUI.kitchen_gui as kitchen

# import Hive modules
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


class Kitchen(QMainWindow, kitchen.Ui_Kitchen):

    def __init__(self, start, hive_connection):
        super(Kitchen, self).__init__()
        self.setupUi(self)

        # Hive database
        self.database_connector = hive_connection
        self.recipe_reader = RecipeReader(self.database_connector)
        self.recipe_reader.load_recipes()

        # Recipe List
        self.recipes = self.recipe_reader.get_recipes()
        item = QListWidgetItem('< None >')
        self.recipe_list.addItem(item)
        for recipe in self.recipes:
            item = QListWidgetItem(recipe)
            self.recipe_list.addItem(item)
        self.recipe_list.itemClicked.connect(self.set_ingredients)
        self.recipe_list.currentItemChanged.connect(self.clear_table)
        self.regex = re.compile('([0-9,.]+)([a-zA-Z]*)')

        self.start = start
        self.cancel_bt.clicked.connect(self.show_start)

        # name widget chooser
        self.mid = MealInputDialog('Title', 'Message', 'Name', 'Links', ('Cancel', 'Accept'), lambda x, y: print(x))

        # language tag
        self.lang_tag = 'de'

        # language dicts
        self.stuff_hor_header_labels = {'en': ['Amount', 'Unit', 'Name'], 'de': ['Menge', 'Einheit', 'Name']}
        self.weekly_hor_header_labels = {'en': 'Meal', 'de': 'Gericht'}
        self.weekly_vert_header_labels = {'en': ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday',
                                             'Tuesday'], 'de': ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag',
                                                                'Freitag', 'Samstag', 'Sonntag']}
        self.set_language_label_text = {'en': 'set Language:', 'de': 'Sprache wechseln:'}
        self.rad_buttons_text = {'en': ['Calories Summation', 'Show stock (empty things)',
                                        'Show stock (existing things)', 'Bought goods'], 'de': ['Kalorienrechner',
                                        'Leere Nahrungsmittel', 'Vorhandene Nahrungsmittel', 'Einkaufsinventur']}
        self.tab_text = {'en': ['Recipes', 'Weekly Rota', 'Playlist'], 'de': ['Rezepte', 'Wochenplan', 'Playlist']}
        self.buttons_text = {'en': [('Calculate calories', 'Push to Database'), 'Cancel'],
                             'de': [('Kalorien berechnen', 'Übernehmen'), 'Zurück']}
        self.button_bought_calc_val = True

        # Tables
        self.stuff_table.setColumnCount(3)
        if not pyside_import:
            self.stuff_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            self.stuff_table.horizontalHeader().setResizeMode(QHeaderView.Stretch)

        self.weekly_tw.setColumnCount(1)
        self.weekly_tw.setRowCount(7)
        self.toggle_language()
        if not pyside_import:
            self.weekly_tw.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.weekly_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            self.weekly_tw.verticalHeader().setResizeMode(QHeaderView.Stretch)
            self.weekly_tw.horizontalHeader().setResizeMode(QHeaderView.Stretch)


        # Time
        self.time_lcd.setDigitCount(8)
        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)
        self.show_time()

        # Timer
        self.timer_lcd.setDigitCount(8)
        self.timer_dial.setMaximum(3600)
        if pyside_import:
            self.timer_dial.dialMoved.connect(self.set_timer)
        else:
            self.timer_dial.valueChanged.connect(self.set_timer)
        self.timer_timer = QTimer(self)
        self.timer_timer.timeout.connect(self.count_downwards)
        self.timer_bt.clicked.connect(self.timer_start)
        self.timer_time = 0
        self.timer_running = False
        bl_pixmap = QPixmap('icons/aperture.png')
        red_pixmap = QPixmap('icons/aperture_red.png')
        self.icon_bl = QIcon()
        self.icon_bl.addPixmap(bl_pixmap)
        self.icon_red = QIcon()
        self.icon_red.addPixmap(red_pixmap)

        # Music buttons
        # prev
        prev_icon = QIcon()
        prev_pixmap = QPixmap('icons/prev.png')
        prev_icon.addPixmap(prev_pixmap)
        self.prev_bt.setIcon(prev_icon)
        # next
        next_icon = QIcon()
        next_pixmap = QPixmap('icons/next.png')
        next_icon.addPixmap(next_pixmap)
        self.next_bt.setIcon(next_icon)
        # play
        self.play_icon = QIcon()
        play_pixmap = QPixmap('icons/play.png')
        self.play_icon.addPixmap(play_pixmap)
        self.pause_icon = QIcon()
        pause_pixmap = QPixmap('icons/pause.png')
        self.pause_icon.addPixmap(pause_pixmap)
        self.play_pause_bt.setIcon(self.play_icon)
        # stop
        stop_icon = QIcon()
        stop_pixmap = QPixmap('icons/stop.png')
        stop_icon.addPixmap(stop_pixmap)
        self.stop_bt.setIcon(stop_icon)
        # search
        search_icon = QIcon()
        search_pixmap = QPixmap('icons/search2.png')
        search_icon.addPixmap(search_pixmap)
        self.go_bt.setIcon(search_icon)

        # table
        self.weekly_meals = {}
        self.stuff_table.cellClicked.connect(self.item_clicked)
        self.weekly_tw.cellClicked.connect(self.weekly_cell_clicked)

        # button calc
        self.calculate_bt.clicked.connect(self.calculate_cal)
        self.lcd_palette = self.calorie_lcd.palette()
        self.lcd_palette.setColor(self.lcd_palette.WindowText, QColor(102, 255, 102))
        self.calorie_lcd.setPalette(self.lcd_palette)

        # radio buttons
        self.show_emp_rad.clicked.connect(lambda: self.radio_button_clicked(True, True))
        self.show_rad.clicked.connect(lambda: self.radio_button_clicked(True, False))
        self.cal_rad.clicked.connect(lambda: self.radio_button_clicked(True, None))
        self.bought_rb.clicked.connect(lambda: self.radio_button_clicked(False, None))

        # video
        stand_by_image = cv2.imread('src/default.png')
        self.update_frame(stand_by_image)
        #self.queue = queue.Queue()
        #self.capture_thread = threading.Thread(target=self.grab, args=(0, self.queue, stand_by_image))
        #self.timer = QTimer(self)
        #self.timer.timeout.connect(self.update_frame)
        #self.timer.start(1)
        #global running
        #running = True
        #self.capture_thread.start()

        # language button
        self.language_bt.clicked.connect(self.toggle_language)

        # Barcode queue and thread
        # TODO: use different way, not input. maybe get serial to work or make an input window, or start a new program
        #self.bar_thread = multiprocessing.Process(target=Kitchen.read_barcodes,
        #                                          args=(self.update_invent_table_barcode, ))
        #self.bar_thread.start()

    def update_invent_table_barcode(self, bar):
        '''
        update the inventory table via barcode
        :param bar: recieved barcode
        :return:
        '''
        row_count = self.stuff_table.rowCount()
        self.stuff_table.insertRow(row_count - 1)
        pass


    def radio_button_clicked(self, up_cal, empty_full):
        '''
        change button behavior if radio buttons are clicked
        :param up_cal: if calorien should be
        :param empty_full:
        :return:
        '''
        self.calorie_lcd.display('0')
        if up_cal:
            if empty_full is None:
                self.show_calorie_calc()
            else:
                self.show_empty_full_items(empty=empty_full)
            if self.button_bought_calc_val:
                self.calculate_bt.setText(self.buttons_text[self.lang_tag][0][0])
                self.toggle_signal_event(self.calculate_bt.clicked, self.calculate_cal, self.update_database)
                self.button_bought_calc_val = False
        else:
            self.show_calorie_calc(row_count=2)
            if not self.button_bought_calc_val:
                self.calculate_bt.setText(self.buttons_text[self.lang_tag][0][1])
                self.toggle_signal_event(self.calculate_bt.clicked, self.update_database, self.calculate_cal)
                self.button_bought_calc_val = True

    def update_database(self):
        '''
        update the database
        :return:
        '''
        for i in range(self.stuff_table.rowCount()):
            vol = ''
            unit = ''
            name = ''
            if self.stuff_table.item(i, 0) is not None and self.stuff_table.item(i, 1) is not None and \
                    self.stuff_table.item(i, 2) is not None:
                vol = self.stuff_table.item(i, 0).text()
                unit = self.stuff_table.item(i, 1).text()
                name = self.stuff_table.item(i, 2).text()
            else:
                return
            self.recipe_reader.get_hive_connection().set_volume_of_item(name, '%s%s' % (vol, unit))

    def toggle_language(self):
        '''
        set the language of the gui
        :return:
        '''
        self.lang_tag = 'de' if self.lang_tag == 'en' else 'en'
        self.language_bt.setText(self.lang_tag)
        self.label_2.setText(self.set_language_label_text[self.lang_tag])
        # weekly table
        self.weekly_tw.setHorizontalHeaderLabels([self.weekly_hor_header_labels[self.lang_tag]])
        self.weekly_tw.setVerticalHeaderLabels(self.weekly_vert_header_labels[self.lang_tag])
        # stuff table
        self.stuff_table.setHorizontalHeaderLabels(self.stuff_hor_header_labels[self.lang_tag])
        # buttons
        button_text_i = 0 if self.button_bought_calc_val else 1
        self.cancel_bt.setText(self.buttons_text[self.lang_tag][1])
        self.calculate_bt.setText(self.buttons_text[self.lang_tag][0][button_text_i])
        self.button_bought_calc_val = False
        # radio buttons
        self.cal_rad.setText(self.rad_buttons_text[self.lang_tag][0])
        self.show_emp_rad.setText(self.rad_buttons_text[self.lang_tag][1])
        self.show_rad.setText(self.rad_buttons_text[self.lang_tag][2])
        self.bought_rb.setText(self.rad_buttons_text[self.lang_tag][3])
        # tabs
        self.gloabal_tab.setTabText(0, self.tab_text[self.lang_tag][0])
        self.gloabal_tab.setTabText(1, self.tab_text[self.lang_tag][1])
        self.gloabal_tab.setTabText(2, self.tab_text[self.lang_tag][2])

    def weekly_cell_clicked(self, row, col):
        '''
        weekly play cell clicked
        :param row:
        :param col:
        :return:
        '''
        item = self.weekly_tw.item(row, col)
        if item is None or item.text() == '':
            day = self.weekly_vert_header_labels[self.lang_tag][row]
            title = {'en': 'Enter new Meal', 'de': 'Neue Mahlzeit hinzufügen'}
            message = {'en': 'Please enter the meal and link for %s' % day,
                     'de': 'Bitte geben sie ein Gericht und entsprechenden Link für den %s ein' % day}
            buttons = {'en': ('Cancel', 'Accept'), 'de': ('Abbrechen', 'Annehmen')}
            # TODO: handle links
            self.mid.change_settings(title[self.lang_tag], message[self.lang_tag], "Name",
                                     "Links", (buttons[self.lang_tag][0], buttons[self.lang_tag][1]),
                                     lambda x, y: self.weekly_tw.setItem(row, col, QTableWidgetItem(x)))
            self.mid.show()

    def closeEvent(self, event):
        '''
        override closing event
        :param event:
        :return:
        '''
        global running
        running = False
        self.bar_thread.terminate()
        self.bar_thread.join()

    def update_frame(self, img):
        '''
        update the image
        :return:
        '''
        #if not self.queue.empty():
        #    frame = self.queue.get()
        #img = frame['img']
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        size = self.video_view.size()
        img = cv2.resize(img, (size.width()-10, size.height()-10))
        height, width, bpc = img.shape
        bpl = bpc * width
        image = QImage(img.data, width, height, bpl, QImage.Format_RGB888)
        pitem = QGraphicsPixmapItem(QPixmap.fromImage(image))
        scene = QGraphicsScene()
        scene.addItem(pitem)
        self.video_view.setScene(scene)

    def calculate_cal(self):
        '''
        calculate calories out of table
        :return:
        '''
        all_there = True
        names = []
        for i in range(self.stuff_table.rowCount() - 1):
            if self.stuff_table.item(i, 2) is None:
                # if item is empty continue
                continue
            names.append(self.stuff_table.item(i, 2).text())
            if not self.recipe_reader.get_hive_connection().check_if_in_stock(self.stuff_table.item(i, 2).text()):
                # if the item is not in the stock mark it as red
                self.stuff_table.item(i, 0).setBackground(QColor(255, 128, 128))
                self.stuff_table.item(i, 1).setBackground(QColor(255, 128, 128))
                self.stuff_table.item(i, 2).setBackground(QColor(255, 128, 128))
                all_there = False
            elif self.stuff_table.item(i, 0).background() == QColor(255, 128, 128):
                all_there = False
        if all_there:
            # if all cals are there calculate everything and post it
            cals = 0
            for name in names:
                if not name == '':
                    cals += int(self.recipe_reader.get_hive_connection().get_cal_for_name(name))
            self.calorie_lcd.display(cals)
            self.calorie_lcd.setSegmentStyle(QLCDNumber.Flat)

    def show_empty_full_items(self, empty):
        '''
        show empty items
        :return:
        '''
        self.clear_table(None, None)
        self.stuff_table.setColumnCount(3)
        self.stuff_table.setHorizontalHeaderLabels(['Volume', 'State', 'Name'])
        items = self.recipe_reader.get_hive_connection().get_empty_stock_items(empty)
        self.stuff_table.setRowCount(len(items))
        for i, item in enumerate(items):
            self.stuff_table.setItem(i, 0, QTableWidgetItem(str(item.vol)))
            self.stuff_table.setItem(i, 1, QTableWidgetItem(item.state))
            self.stuff_table.setItem(i, 2, QTableWidgetItem(item.name))
            if empty:
                self.stuff_table.item(i, 0).setBackground(QColor(255, 128, 128))

    def show_calorie_calc(self, row_count=0):
        '''
        show calorie calculator
        :return:
        '''
        if row_count > 0:
            row_count += 1
        self.clear_table(None, None)
        self.stuff_table.clearContents()
        self.stuff_table.setColumnCount(3)
        self.stuff_table.setRowCount(row_count)
        self.stuff_table.setHorizontalHeaderLabels(['Amount', 'Unit', 'Name'])
        if row_count > 0:
            stuff_widget = QWidget()
            stuff_pixmap = QPixmap('icons/add.png')
            stuff_icon = QIcon()
            stuff_add_bt = QToolButton()
            stuff_icon.addPixmap(stuff_pixmap)
            stuff_add_bt.setIcon(stuff_icon)
            stuff_add_bt.setIconSize(QSize(8, 8))
            stuff_add_bt.clicked.connect(lambda: self.stuff_table.insertRow(row_count-1))
            stuff_layout = QHBoxLayout()
            stuff_layout.addWidget(stuff_add_bt)
            stuff_widget.setLayout(stuff_layout)
            self.stuff_table.setCellWidget(row_count-1, 2, stuff_widget)

    def item_clicked(self, row, col):
        '''
        action to perform when one item is clicked
        :param row: item row
        :param col: item col
        :return:
        '''
        item = self.stuff_table.item(row, col)
        if item is None:
            # if Item is none ignore
            return
        bg = item.background()
        if bg == QColor(255, 128, 128):
            # if item is colorful ask the user to add cals
            name = self.stuff_table.item(row, 2).text()
            text, ok = QInputDialog.getText(self, 'Calorie Input Dialog',
                                                  'Enter the calories per 100g for %s:' % name)
            reg = re.compile('([0-9,.]+)')
            cif = reg.match(text)
            if cif is None or len(cif.group(1)) == 0:
                return
            # if cal is added reprint the item
            self.recipe_reader.get_hive_connection().set_calorie_for_name(name, int(cif.group(1)))
            self.stuff_table.item(row, 0).setBackground(QColor(0, 0, 0))
            self.stuff_table.item(row, 1).setBackground(QColor(0, 0, 0))
            self.stuff_table.item(row, 2).setBackground(QColor(0, 0, 0))

    def clear_table(self, old, new):
        '''
        clear the table
        :param old: not used
        :param new: not used
        :return:
        '''
        for i in range(self.stuff_table.rowCount()):
            self.stuff_table.removeRow(i)

    def set_ingredients(self, item):
        '''
        action for recipe choosed
        :param item: choosen item
        :return:
        '''
        if item.text() == '< None >':
            # if None is choosen set up empty table
            self.show_calorie_calc(20)
        else:
            ing = self.recipe_reader.get_ingredients(item.text())
            ing_dic = {}
            self.stuff_table.setRowCount(len(ing))
            # set Row count to current list length
            for i, (vol, name, cal) in enumerate(ing):
                vol_gr = self.regex.match(str(vol))
                # regex the amount
                volume = self.recipe_reader.get_hive_connection().get_volume_of_item(name)
                volume = self.regex.match(volume)
                if vol_gr is not None:
                    vol = float(vol_gr.group(1))
                    unit = vol_gr.group(2)
                else:
                    vol = 1.0
                    unit = 'Priese'
                if name in ing_dic.keys():
                    i, vol_o, unit_o = ing_dic[name]
                    vol += vol_o
                else:
                    self.stuff_table.setItem(i, 2, QTableWidgetItem(name))
                # fill table
                ing_dic[name] = (i, vol, unit)
                self.stuff_table.setItem(i, 0, QTableWidgetItem(str(vol)))
                self.stuff_table.setItem(i, 1, QTableWidgetItem(unit))
                volume = volume.group(1)
                if int(volume) == 0:
                    self.stuff_table.item(i, 0).setBackground(QColor(247, 188, 7))
                if cal is None:
                    self.stuff_table.item(i, 2).setBackground(QColor(255, 128, 128))

    def set_timer(self, value):
        '''
        set the timer
        :param value: value to set to
        :return:
        '''
        self.timer_time = int(value)
        self.timer_lcd.display(Kitchen.format_time(value))

    def timer_start(self):
        '''
        start/stop the timer
        :return:
        '''
        if self.timer_running:
            self.timer_running = not self.timer_running
            self.timer_bt.setIcon(self.icon_bl)
            self.set_timer(0)
            self.timer_dial.setValue(0)
            self.timer_time = 0
            self.timer_dial.setDisabled(False)
            self.timer_timer.stop()
        else:
            if not self.timer_time == 0:
                self.timer_dial.setDisabled(True)
                self.timer_timer.start(1000)
                self.timer_running = not self.timer_running
                self.timer_bt.setIcon(self.icon_red)

    def count_downwards(self):
        '''
        timer count down
        :return:
        '''
        value = self.timer_time - 1
        self.timer_time = value
        if value == 0:
            self.timer_dial.setDisabled(False)
            self.timer_timer.stop()
        self.timer_lcd.display(Kitchen.format_time(value))

    def show_time(self):
        '''
        clock
        :return:
        '''
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.time_lcd.display(text)

    def show_start(self):
        '''
        show start window
        :return:
        '''
        self.hide()
        self.start.show()

    @staticmethod
    def format_time(number):
        '''
        format a number to time
        :param number: number to format
        :return:
        '''
        sek = number % 60
        minutes = int(number / 60) % 60
        hours = int(number / 3600)
        if sek < 10:
            sek = '0%i' % sek
        else:
            sek = str(sek)
        if minutes < 10:
            minutes = '0%i' % minutes
        else:
            minutes = str(minutes)
        if hours < 10:
            hours = '0%i' % hours
        else:
            hours = str(hours)
        return '%s:%s:%s' % (hours, minutes, sek)

    # currently ignore this method
    @staticmethod
    def grab(cam, grab_queue, standby_img):
        '''
        grabbing the next image and check if the camera is still connected
        :param cam: camera number
        :param grab_queue: queue
        :param standby_img: standby_img that has to be shown if no camera is found
        :return:
        '''
        global running
        capture = cv2.VideoCapture(cam)
        while running:
            frame = {}
            if capture.isOpened():
                retval, img = capture.read()
                if not retval:
                    frame['img'] = standby_img
                    #capture.release()
                    #capture = cv2.VideoCapture(cam)
                else:
                    frame['img'] = img

            else:
                frame['img'] = standby_img
                capture.open()
            if grab_queue.qsize() < 10:
                grab_queue.put(frame)

    @staticmethod
    def toggle_signal_event(signal, new_event, old_event):
        '''
        change the event of an signal slot
        :param signal: signal of an item
        :param new_event: new event method
        :param old_event: old event method
        :return:
        '''
        if new_event is None:
            return
        signal.disconnect()
        signal.connect(new_event)

    @staticmethod
    def read_barcodes(update):
            '''
            barcode reader
            :param bar_queue: queue for data
            :return:
            '''
            while True:
                bar = input()
                if len(bar) > 0:
                    if bar == '000000000':
                        break
                    update(bar)
            return