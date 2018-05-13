# -*- coding: utf-8 -*-
"""
Created on Mar 30, 2018
@author: ThiefOfTime
"""

import requests
from os import path, listdir
from bs4 import BeautifulSoup


# TODO: implement check of recipe in database
class RecipeReader:
    '''
    IOReader for the recipes
    '''

    def __init__(self, hive_connection, rpath='../../recipes'):
        # TODO: think of useful variables
        if path.isdir(rpath):
            self.path = rpath
            if self.path.endswith(path.sep):
                self.path = self.path.rsplit(path.sep, 1)[0]
        else:
            raise ValueError('Please insert a correct path!')
        self.hive_connection = hive_connection
        self.__recp = {}
        self.__recipes = self.hive_connection.get_recipes()

    def __repr__(self):
        # TODO: implement
        pass

    def __load_recipe(self, rfile, directly_load_to_hive=True):
        '''
        load single recipe
        :param rfile: recipe file
        :param directly_load_to_hive: parameter for testing, to prevent directly loading to the hive
        :return: list of recipe tuple
        '''
        with open(path.join(self.path, rfile), 'r') as open_rec:
            lines = open_rec.readlines()

        recp = []
        for _ in range(lines.count('\n')):
            recp.append(lines[:lines.index('\n')])
            lines = lines[lines.index('\n') + 1:]
        recp.append(lines)
        info = recp[0]
        info = [inf.split(':', 1)[1].replace('\n', '') for inf in info[1:]]
        recp = recp[1:]
        recp_new = []
        for r in recp:
            recp_new.append((r[0].replace(':', ''), r[1:]))
        #if directly_load_to_hive and not rfile.rsplit('_')[0] in self.__recipes:
            #self.hive_connection.add_new_column('dish', (rfile.rsplit('_', 1)[0], info))
            #self.hive_connection.commit_changes()
        return recp_new, (rfile.rsplit('_', 1)[0], info)

    def __load_ingredient(self, rfile):
        '''
        load single recipe ingredients
        :param rfile: recipe ingredients file
        :return: list of recipe ingredients tuple
        '''
        with open(path.join(self.path, rfile), 'r') as open_rec:
            lines = open_rec.readlines()
        lines = [iline.replace('\n', '').split(':') for iline in lines[2:] if iline.count(':') == 2]
        # add to hive
        #self.hive_connection.add_new_column('ingredients', (rfile.rsplit('_', 1)[0], lines))
        #self.hive_connection.commit_changes()
        return rfile.rsplit('_')[0], lines

    def load_recipes(self, directly_load_to_hive=True):
        '''
        load method for recipes
        :param directly_load_to_hive: parameter for testing to not load the recipes to hive
        :return: receipt dictionary
        '''
        if self.check_for_new_recipes():
            files = listdir(self.path)
            files_ingr = [ifile for ifile in files if ifile.endswith('_ingredients.txt')]
            files = [rfile for rfile in files if rfile.endswith('_recipe.txt')]
            #self.__recp = files
            receipt_dict = {}
            for rfile, ifile in zip(files, files_ingr):
                file_name = rfile.rsplit('_', 1)[0]
                if not file_name in self.__recipes:

                    receipt_dict[file_name], stuff = self.__load_recipe(rfile,
                                                                directly_load_to_hive=directly_load_to_hive)
                    ingr = self.__load_ingredient(ifile)
                    if directly_load_to_hive and not rfile.rsplit('_')[0] in self.__recipes:
                         self.hive_connection.add_new_recipe(stuff, ingr)
                         self.hive_connection.commit_changes()

            self.__recp = receipt_dict

    def check_for_new_recipes(self, directly_load_to_hive=True):
        '''
        check for new given recipes
        :return: bool
        '''
        files = listdir(self.path)
        files = [rfile for rfile in files if rfile.endswith('_recipe.txt')]
        counter = 0
        for rfile in files:
            if rfile.rsplit('_')[0] in self.__recp.keys():
                continue
            counter += 1
        return counter > 0

    def get_recipes(self):
        '''
        :return: recipes dictionary
        '''
        return self.hive_connection.get_recipes()

    def get_ingredients(self, name):
        '''
        get ingredients
        :param name: recipe name
        :return: return list of ingredients
        '''
        return self.hive_connection.get_ingredients(name)

    def get_hive_connection(self):
        '''
        :return: hive connection reference
        '''
        return self.hive_connection


class RecipeWriter:
    '''
    Write given recipes to file
    '''
    def __init__(self, rpath='../../recipes'):
        self.path = rpath

    def save_recipe(self, text, name, link):
        '''
        save given recipe to file
        :param text: recipe text
        :param name: recipe name
        :param link: link to recipe
        :return:
        '''
        with open(path.join(self.path, '%s_recipe.txt' % name), 'w') as rfile:
            rfile.write('Infos:\n')
            rfile.write('link:%s\n' % link)
            rfile.write(text)

    def save_ingredients(self, text, name):
        '''
        save given ingredients to file
        :param text: ingredients text
        :param name: recipe name
        :return:
        '''
        with open(path.join(self.path, '%s_ingredients.txt' % name), 'w') as ifile:
            ifile.write('Menge:Name:prep')
            ifile.write('\n')
            ifile.write(text)


class RecipeHTMLExtractor:
    '''
    Extract recipes out of HTML files
    '''
    def __init__(self, url=''):
        self.url = url
        self.source = None
        self.soup = None

    def get_html_content(self, url):
        '''
        get website content
        :param url: given url
        :return: html code
        '''
        return requests.get(url)

    def extract_recipe(self, option=None):
        '''
        extract from html code
        :param option: given option
        :return: possible recipe fields
        '''
        if self.url is None or self.url == '':
            return None

        if self.source is None and self.soup is None:
            self.source = requests.get(self.url)
            self.soup = BeautifulSoup(self.source.content, 'html.parser')

        if option is None:
            return None
        elif option == 0:
            return [elem for elem in self.soup.find_all('p') if str(elem).startswith('<p>')]
        elif option == 1:
            pass
        elif option == 2:
            pass

        return None

    def extract_ingredients(self, option=None):
        '''
        extract from html code
        :param option: given option
        :return: possible ingredients fields
        '''
        if self.url is None or self.url == '':
            return None

        if self.source is None and self.soup is None:
            self.source = requests.get(self.url)
            self.soup = BeautifulSoup(self.source.content, 'html.parser')

        if option is None:
            return None
        elif option == 0:
            return [elem for elem in self.soup.find_all('li') if str(elem).startswith('<li>')]
        elif option == 1:
            return [elem for elem in self.soup.find_all(itemprop="recipeIngredient")]
        elif option == 2:
            return [elem for elem in self.soup.find_all('p', 'li') if str(elem).startswith('<li>')]
        return None

    def set_url(self, url):
        '''
        set url
        :param url: given url
        :return:
        '''
        self.url = url
        self.source = None
        self.soup = None
