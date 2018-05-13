# -*- coding: utf-8 -*-
"""
Created on Mar 30, 2018
@author: ThiefOfTime
"""

from hive.SQLHiveConnection import DatabaseConnector
from connections.HiveIO import RecipeReader
from connections.Server import BluetoothIOServer

from multiprocessing import Process


class FridayKitchen:

    def __init__(self):
        self.database_connector = DatabaseConnector()
        self.recipe_reader = RecipeReader(self.database_connector)
        self.bluetooth_server = BluetoothIOServer(self, self.database_connector)
        self.process = None

    def run_kitchen_helper(self):
        self.bluetooth_server.run()
        self.process = Process(target=self.bluetooth_server.run)
        self.process.start()
        while True:
            a = 0

    def close(self):
        self.process.terminate()


if __name__ == "__main__":
    f = FridayKitchen()
    f.run_kitchen_helper()
