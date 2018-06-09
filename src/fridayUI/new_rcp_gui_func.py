# -*- coding: utf-8 -*-
"""
Created on Apr 24, 2018
@author: ThiefOfTime
"""

# TODO: kick QtGui import out
# import PySide modules
try:
    from PySide.QtGui import QMainWindow, QMessageBox
except ModuleNotFoundError:
    from PySide2.QtWidgets import QMainWindow, QMessageBox

# import new recepie gui
import fridayUI.new_rcp_gui as nrcpd

# import Hive modules
from connections.HiveIO import RecipeHTMLExtractor, RecipeWriter


class NewRecipe(QMainWindow, nrcpd.Ui_NewRecipe):
    '''
    Widget class for the recipe extractor
    '''
    def __init__(self):
        super(NewRecipe, self).__init__()
        self.setupUi(self)

        # change settings
        self.ingr_text.setReadOnly(False)
        self.rec_text.setReadOnly(False)
        self.setFixedSize(self.size())
        # radio button settings
        self.pos1_rb.setChecked(True)
        self.pos1_irb.setChecked(True)
        self.rec_op = 0
        self.ingr_op = 0
        # Prep edit settings
        self.prep_edit.setEnabled(False)
        self.cook_edit.setEnabled(False)
        self.baking_edit.setEnabled(False)
        self.rest_edit.setEnabled(False)
        self.cool_edit.setEnabled(False)
        self.freeze_edit.setEnabled(False)
        # HTMLExtractor
        self.extractor = RecipeHTMLExtractor()
        # RecipeWriter
        self.recipe_writer = RecipeWriter()
        # connect buttons
        self.cancel_button.clicked.connect(self.cancel)
        self.save_button.clicked.connect(self.save)
        self.start_search_button.clicked.connect(self.get_html_content)
        # connect radio buttons
        self.pos1_rb.clicked.connect(self.refresh_recipe)
        self.pos2_rb.clicked.connect(self.refresh_recipe)
        self.pos3_rb.clicked.connect(self.refresh_recipe)
        # connect radio buttons
        self.pos1_irb.clicked.connect(self.refresh_ingredients)
        self.pos2_irb.clicked.connect(self.refresh_ingredients)
        self.pos3_irb.clicked.connect(self.refresh_ingredients)
        # connect check boxes
        self.prep_check.toggled.connect(self.toggle_pred_edit)
        self.cook_check.toggled.connect(self.toggle_cook_edit)
        self.baking_check.toggled.connect(self.toggle_baking_edit)
        self.rest_check.toggled.connect(self.toggle_rest_edit)
        self.cool_check.toggled.connect(self.toggle_cool_edit)
        self.freeze_check.toggled.connect(self.toggle_freeze_edit)

    def cancel(self):
        '''
        close the application
        :return:
        '''
        self.close()

    def clear_all(self):
        '''
        clear all Text fields and reset check box
        :return:
        '''
        prep_list_text = [self.prep_edit, self.cook_edit, self.baking_edit, self.rest_edit,
                          self.cool_edit, self.freeze_edit]
        prep_list_check = [self.prep_check, self.cook_check, self.baking_check, self.rest_check,
                           self.cool_check, self.freeze_check]
        for text in prep_list_text:
            text.setText('')
            text.setEnabled(False)
        for check in prep_list_check:
            check.setChecked(False)
        self.rec_text.setText('')
        self.ingr_text.setText('')
        self.name_edit.setText('')
        self.portion_edit.setText('')

    def save(self):
        '''
        check if all needed informations are provided and save to file
        :return:
        '''
        got_text = (not self.rec_text.toPlainText() == '') and (not self.ingr_text.toPlainText() == '')
        got_preps = False
        prep_list_check = [self.prep_check, self.cook_check, self.baking_check, self.rest_check,
                           self.cool_check, self.freeze_check]
        prep_list_text = [self.prep_edit, self.cook_edit, self.baking_edit, self.rest_edit,
                           self.cool_edit, self.freeze_edit]
        for i, check in enumerate(prep_list_check):
            if check.isChecked():
                got_preps = got_preps or (not prep_list_text[i].text() == '')

        got_name = not self.name_edit.text() == ''
        got_potion = not self.portion_edit.text() == ''
        if got_text and got_preps and got_name and got_potion:
            ingr = self.format_ingredients()
            rec = self.format_recipe()
            self.recipe_writer.save_ingredients(ingr, self.name_edit.text().lower().replace(' ', '_'))
            self.recipe_writer.save_recipe(rec, self.name_edit.text().lower().replace(' ', '_'),
                                           self.adress_edit.text())
        else:
            # if anything is missing send warning
            msg_box = QMessageBox()
            msg_box.setText("Some informations are missing!\n Make sure you inserted a recipe with ingredients,\n"
                            " preparaton time, name and portion size.")
            msg_box.exec_()

    def toggle_pred_edit(self):
        '''
        toggle edit field
        :return:
        '''
        if self.prep_check.isChecked():
            self.prep_edit.setEnabled(True)
        else:
            self.prep_edit.setEnabled(False)
            self.prep_edit.setText('')

    def toggle_cook_edit(self):
        '''
        toggle edit field
        :return:
        '''
        if self.cook_check.isChecked():
            self.cook_edit.setEnabled(True)
        else:
            self.cook_edit.setEnabled(False)
            self.cook_edit.setText('')

    def toggle_baking_edit(self):
        '''
        toggle edit field
        :return:
        '''
        if self.baking_check.isChecked():
            self.baking_edit.setEnabled(True)
        else:
            self.baking_edit.setEnabled(False)
            self.baking_edit.setText('')

    def toggle_rest_edit(self):
        '''
        toggle edit field
        :return:
        '''
        if self.rest_check.isChecked():
            self.rest_edit.setEnabled(True)
        else:
            self.rest_edit.setEnabled(False)
            self.rest_edit.setText('')

    def toggle_cool_edit(self):
        '''
        toggle edit field
        :return:
        '''
        if self.cool_check.isChecked():
            self.cool_edit.setEnabled(True)
        else:
            self.cool_edit.setEnabled(False)
            self.cool_edit.setText('')

    def toggle_freeze_edit(self):
        '''
        toggle edit field
        :return:
        '''
        if self.freeze_check.isChecked():
            self.freeze_edit.setEnabled(True)
        else:
            self.freeze_edit.setEnabled(False)
            self.freeze_edit.setText('')

    def refresh_recipe(self):
        '''
        a different toggle button was clicked, so refresh recipe
        :return:
        '''
        rec_op, _ = self.check_for_option()
        if rec_op == self.rec_op:
            return
        else:
            self.rec_op = rec_op
            rc = self.extractor.extract_recipe(option=rec_op)
            if rc is None:
                return
            self.rec_text.setText(''.join([str(e) for e in rc]))

    def refresh_ingredients(self):
        '''
        a different toggle button was clicked, so refresh ingredients
        :return:
        '''
        _, ingr_op = self.check_for_option()
        if ingr_op == self.ingr_op:
            return
        else:
            self.ingr_op = ingr_op
            ingr = self.extractor.extract_ingredients(option=ingr_op)
            if ingr is None:
                return
            self.ingr_text.setText(''.join([str(e) for e in ingr]))

    def get_html_content(self):
        '''
        collect informations from web site
        :return:
        '''
        url = self.adress_edit.text()
        self.clear_all()
        rec_op, ingr_op = self.check_for_option()
        self.rec_op = rec_op
        self.ingr_op = ingr_op
        self.extractor.set_url(url)
        rc = self.extractor.extract_recipe(option=rec_op)
        ingr = self.extractor.extract_ingredients(option=ingr_op)
        if rc is None and ingr is None:
            return
        self.rec_text.setText(''.join([str(e) for e in rc]))
        self.ingr_text.setText(''.join([str(e) for e in ingr]))

    def check_for_option(self):
        '''
        check which options are choosen
        :return:
        '''
        if self.pos1_rb.isChecked():
            rec = 0
        elif self.pos2_rb.isChecked():
            rec = 1
        else:
            rec = 2

        if self.pos1_irb.isChecked():
            ingr = 0
        elif self.pos2_irb.isChecked():
            ingr = 1
        else:
            ingr = 2

        return rec, ingr

    def format_ingredients(self):
        '''
        format given ingredients text to fit format
        :return: formatted text
        '''
        text = self.ingr_text.toPlainText()
        text_split = text.split('\n')
        text_ret = ''
        for t in text_split:
            tmp_text = t.split(' ')
            if len(tmp_text) == 3:
                tmp_text = ':'.join(tmp_text)
            else:
                tmp_text = '%s:None' % (':'.join(tmp_text))
            text_ret = '%s%s\n' % (text_ret, tmp_text)
        return text_ret

    def format_recipe(self):
        '''
        format given recipes text to fit format
        :return: formatted text
        '''
        ret_text = 'portion:%s' % self.portion_edit.text()
        prep_list_check = [self.prep_check, self.cook_check, self.baking_check, self.rest_check,
                           self.cool_check, self.freeze_check]
        prep_list_text = [('prep:', self.prep_edit), ('cook:', self.cook_edit), ('bake:', self.baking_edit),
                          ('rest:', self.rest_edit), ('cool:', self.cool_edit), ('freeze:', self.freeze_edit)]
        for i, check in enumerate(prep_list_check):
            if check.isChecked() and not prep_list_text[i][1].text() == '':
                text_add = prep_list_text[i][1].text()
            else:
                text_add = 'NULL'
            ret_text = '%s%s%s\n' % (ret_text, prep_list_text[i][0], text_add)

        ret_text = '%s\ncalpp:NULL\n%s' % (ret_text, self.rec_text.toPlainText())
        return ret_text

