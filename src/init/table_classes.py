# -*- coding: utf-8 -*-
"""
Created on Mar 29, 2018
@author: ThiefOfTime
"""

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

string_length = 250

#TODO: thoughts of relations

class Spice(Base):
    '''
    Table of spice dish relation
    '''

    __tablename__ = 'spices'

    # spice id and dish id
    sid = Column(Integer, ForeignKey('stock.id'), primary_key=True)
    did = Column(Integer, ForeignKey('dishes.id'), primary_key=True)


class Dish(Base):
    '''
    Table of Dishes
    '''
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True)
    name = Column(String(string_length), nullable=False)
    link = Column(String(string_length), nullable=False)
    time_prep = Column(Integer, nullable=False)
    time_cook = Column(Integer)
    time_bake = Column(Integer)
    time_rest = Column(Integer)
    time_cool = Column(Integer)
    time_freeze = Column(Integer)
    # calories per person
    calpp = Column(Integer)
    # book_ref = Column(Integer, ForeignKey('books.id'))


class Ingredients(Base):
    '''
    Table of Ingredients
    maps from Dishes to Inventory
    '''
    __tablename__ = 'ingredients'

    did = Column(Integer, ForeignKey('dishes.id'), primary_key=True)
    sid = Column(Integer, ForeignKey('stock.id'), primary_key=True)
    volume = Column(String(string_length), nullable=False)
    prepared = Column(Integer, nullable=False)
    dish = relationship('Dish')
    stock = relationship('Stock')


class Stock(Base):
    '''
    Table of stuff in stock
    '''
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    name = Column(String(string_length), nullable=False)
    cal = Column(Integer)
    vol = Column(String(string_length), nullable=False)
    state = Column(Integer, nullable=False)
    buy = Column(Boolean, nullable=False)


class Books(Base):
    '''
    Table of cooking books
    '''
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(string_length), nullable=False)
    iban = Column(String(string_length))
    lend = Column(Boolean, nullable=False)
    style = Column(String(string_length))


class Drinks(Base):
    '''
    Table of drinks
    '''
    __tablename__ = 'drinks'

    id = Column(Integer, nullable=False)
    name = Column(String(string_length), primary_key=True)
    iid = Column(Integer, ForeignKey('stock.id'), primary_key=True)
    link = Column(String(string_length), nullable=False)


class Tea(Base):
    '''
    list of teas
    '''
    __tablename__ = 'tea'

    id = Column(Integer, primary_key=True)
    name = Column(String(string_length), nullable=False)
    state = Column(Integer, nullable=False)
    ingredient = Column(String(string_length), primary_key=True)
    style = Column(String(string_length), nullable=False)


def create_database(path):
    engine = create_engine('sqlite:///%s/sqlalchemy_hive.db' % path)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_database("../../database")

