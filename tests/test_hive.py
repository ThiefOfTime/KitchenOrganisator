import unittest
from os import path, popen

from hive.SQLHiveConnection import DatabaseConnector
from connections.HiveIO import RecipeReader
from init.table_classes import create_database


hiveConnection = DatabaseConnector('../database')
hiveIO = RecipeReader(hiveConnection, '../recipes')


class TestIO(unittest.TestCase):

    def test_for_new_recipes(self):
        # Test should be True
        self.assertTrue(hiveIO.check_for_new_recipes())

    def test_load_recipes(self):
        hiveIO.load_recipes(False)
        self.assertGreater(len(hiveIO.get_recipes().keys()), 0)
        recipe = hiveIO.get_recipes()[hiveIO.get_recipes().keys()[0]]
        self.assertEqual(len(recipe), 2)
        self.assertGreaterEqual(len(recipe[1]), 1)

    def test_for_new_recipes_false(self):
        self.assertTrue(hiveIO.check_for_new_recipes())
        hiveIO.load_recipes()
        self.assertFalse(hiveIO.check_for_new_recipes())


class TestHive(unittest.TestCase):

    def test_check_if_dish_not_in_hive(self):
        create_database(path.join('.', 'test1.db'))
        con = DatabaseConnector('.', 'test1.db')
        hv = RecipeReader(con, '../recipes')
        hv.load_recipes(False)
        name = hv.get_recipes().keys()[0]
        self.assertFalse(con.check_if_in_hive('dish', name=name))
        popen('rm test1.db')

    def test_check_if_dish_in_hive(self):
        create_database(path.join('.', 'test2.db'))
        con = DatabaseConnector('.', 'test2.db')
        hiveio_new = RecipeReader(con, '../recipes')
        hiveio_new.load_recipes()
        name = hiveio_new.get_recipes().keys()[0]
        self.assertTrue(con.check_if_in_hive('dish', name=name))
        popen('rm test2.db')




if __name__ == '__main__':
    unittest.main()

