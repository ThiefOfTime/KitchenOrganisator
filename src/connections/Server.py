# -*- coding: utf-8 -*-
"""
Created on Mar 30, 2018
@author: ThiefOfTime
"""

import uuid
import bluetooth
import _thread


class BluetoothIOServer:
    '''
    IOServer for bluetooth connections
    '''

    def __init__(self, main, hive_con, address='', port=3):
        '''

        :param hive_con: hive connection object
        :param address: bluetooth address
        :param port: bluetooth port
        '''
        # TODO: network scanner for smartphone
        self.server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.port = port
        self.server_socket.bind((address, port))
        self.server_socket.listen(1)
        self.hive_con = hive_con
        self.dev_uuid = str(uuid.NAMESPACE_URL)
        print(self.dev_uuid)
        self.main = main
        bluetooth.advertise_service(self.server_socket, 'IOServer', service_id=self.dev_uuid,
                                    service_classes=[self.dev_uuid, bluetooth.SERIAL_PORT_CLASS],
                                    profiles=[bluetooth.SERIAL_PORT_PROFILE])

    def communicate(self, client_socket, address):
        '''
        communication method run for each client
        :param client_socket: client socket
        :param address: client address
        :return: on hang up
        '''
        try:
            # send welcome message
            client_socket.send(':mes Welcome to the Hive! You are going to cook down here!')
            while True:
                msg = client_socket.recv(1024)
                if msg.startswith(':req'):
                    request = msg.split(' ', 1)[1]
                    # TODO: extract important info out of request
                elif msg.startswith(':chg'):
                    change = msg.split(' ', 1)[1]
                elif msg.startswith(':add'):
                    request = msg.split(' ', 1)[1]
                elif msg == ':quit':
                    client_socket.close()
                    self.main.close()
                    return
                else:
                    print(msg)
        except Exception:
            pass
        finally:
            client_socket.close()
            return

    def run(self):
        '''
        run the server
        :return:
        '''
        #while True:
        try:
            print("start listening")
            client_socket, address = self.server_socket.accept()
            print("client connected")
            _thread.start_new_thread(self.communicate, (client_socket, address))
            while True:
                pass
        except Exception:
            pass
        finally:
            self.server_socket.close()


