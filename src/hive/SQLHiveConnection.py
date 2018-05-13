# -*- coding: utf-8 -*-
"""
Created on Mar 30, 2018
@author: ThiefOfTime
"""

from os import path

from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker


from init.table_classes import Base, Ingredients, Dish, Stock


class HiveTableException(Exception):
    pass


class HiveDishException(Exception):
    pass


class HiveUnknownTableException(Exception):
    pass


class DatabaseConnector:

    def __init__(self, dpath='../../database', db_name='sqlalchemy_hive.db'):
        if path.exists(dpath) and path.isfile('%s/%s' % (dpath, db_name)):
            self.engine = create_engine('sqlite:///%s/%s' % (dpath, db_name))
        else:
            raise ValueError('Please insert a correct path!')

        Base.metadata.bind = self.engine
        h_session = sessionmaker(bind=self.engine)
        self.hive_session = h_session()

    def add_new_recipe(self, stuff_rec, stuff_ingr):
        '''
        add new recipe to the database
        :param stuff_rec: recipe name and infos
        :param stuff_ingr: ingredients name and infos
        :return:
        '''
        link, prep, cook, bake, rest, cool, freeze, calp = stuff_rec[1]
        new_dish = Dish(name=stuff_rec[0], link=link, time_prep=prep, time_cook=cook, time_bake=bake, time_rest=rest,
                        time_cool=cool, time_freeze=freeze, calpp=calp)
        self.hive_session.add(new_dish)
        for stuff_line in stuff_ingr[1]:
            stock = self.add_to_stock(stuff_line[1])
            new_stuff = Ingredients(did=new_dish.id, sid=stock.id, volume=stuff_line[0],
                                    prepared=stuff_line[2], dish=new_dish, stock=stock)
            self.hive_session.add(new_stuff)

    def add_to_stock(self, name):
        '''
        add name to stock if not existing
        :param name: name of item
        :return: stock element
        '''
        stock = self.hive_session.query(Stock).filter(Stock.name == name).first()
        if stock is None:
            stock = Stock(name=name, vol=0, state=0, buy=True)
            self.hive_session.add(stock)
        return stock

    def add_new_column(self, table, stuff):
        '''
        add new column to table
        :param table: table to add the column
        :param stuff: stuff to add
        :return:
        '''
        if table == 'dish':
            # if a dish has to be added
            link, prep, cook, bake, rest, cool, freeze, calp = stuff[1]
            new_dish = Dish(name=stuff[0], link=link, time_prep=prep, time_cook=cook, time_bake=bake, time_rest=rest,
                            time_cool=cool, time_freeze=freeze, calpp=calp)
            self.hive_session.add(new_dish)
        elif table == 'ingredients':
            # add ingredients if dish is already known
            entries = self.hive_session.query(Dish).filter(Dish.name == stuff[0]).all()
            if len(entries) == 0:
                raise HiveDishException('No dish found. Please create the dish first!')
            else:
                dish = entries[0]
                for stuff_line in stuff[1]:
                    stock = self.hive_session.query(Stock).filter(Stock.name == stuff_line[1]).first()
                    # TODO: ask user to update the stock
                    if stock is None:
                        stock = Stock(name=stuff_line[1], vol=0, state=0, buy=True)
                        self.hive_session.add(stock)

                    new_stuff = Ingredients(did=dish.id, sid=stock.id, volume=stuff_line[0],
                                            prepared=stuff_line[2], dish=entries[0], stock=stock)
                    self.hive_session.add(new_stuff)
        elif table == 'stock':
            new_stock = Stock(name=stuff[1][0], vol=stuff[1][1], state=stuff[1][2], buy=stuff[1][3])
            self.hive_session.add(new_stock)
        else:
            raise HiveTableException('Table not known, please provide a proper table!')

    def check_if_in_hive(self, table, name):
        '''
        check if an attribute is in the provided table
        :param table: the searched table
        :param name: attribute name
        :return: bool
        '''
        if table == 'dish':
            table_class = Dish
        elif table == 'stock':
            table_class = Stock
        else:
            raise HiveUnknownTableException('The provided table is not known, please provide a known table!')
        entry = self.hive_session.query(table_class).filter(table_class.name == name).all()
        return len(entry) > 0

    def commit_changes(self):
        '''
        committing the changes to the db
        '''
        self.hive_session.commit()

    def discard_changes(self):
        '''
        discarding the changes
        '''
        self.hive_session.rollback()

    def close_connection(self):
        '''
        closing the db session
        '''
        self.hive_session.close()

    def get_recipes(self):
        '''
        getting all loaded recipe names
        :return: list of strings
        '''
        return [dish.name for dish in self.hive_session.query(Dish)]

    def get_cal_for_name(self, name):
        '''
        getting cal per 100 gramm
        :param name: given name
        :return: integer val
        '''
        return self.hive_session.query(Stock).filter(Stock.name == name).first().cal

    def check_if_in_stock(self, name):
        '''
        check if in stock
        :param name: check if name in stock
        :return: (name, bool)
        '''
        return self.hive_session.query(Stock).filter(Stock.name == name).first() is not None

    def get_ingredients(self, dish_name):
        '''
        getting ingredients for a dish
        :param dish_name: dish name
        :return: list of ingredients
        '''
        entry = self.hive_session.query(Dish).filter(Dish.name == dish_name).all()[0]
        return [(ing.volume, ing.stock.name, ing.stock.cal) for ing in
                self.hive_session.query(Ingredients).filter(entry.id == Ingredients.did)]

    def set_calorie_for_name(self, name, cal):
        '''
        update calories for item
        :param name: name of the item
        :param cal: for the item
        '''
        self.add_to_stock(name)
        self.hive_session.query(Stock).filter(Stock.name == name).update({Stock.cal: cal})
        self.hive_session.commit()

    def get_empty_stock_items(self, empty=False):
        '''
        return stock items that have to be bought
        :return:
        '''
        return self.hive_session.query(Stock).filter(Stock.buy == empty).all()
