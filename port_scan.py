'''
Version: 0.1
Author: João Paulo Andrade
Data: 06/10/2019
Description: Script to scan port of hosts
'''

import socket
import sys
import errno
import os


class MyPortScan(object):

    default_ports = [21, 22, 23, 53, 80, 443, 3389, 389, 3306, 1521, 8080, 8000]

    def __init__(self, ip, portlist=default_ports):
        self.ip = ip
        self.portlist = portlist

    def check_port_socket(self):

        try:
            for port in self.portlist:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                result = s.connect_ex((self.ip, port))
                if result == 0:
                    print('Port {}:\tOpen'.format(port))
                else:
                    print('Port {}:\tClosed'.format(port))
                    print('\tCode error: {}'.format(errno.errorcode[result]))
                    print('\tMessage: {}'.format(os.strerror(result)))
                s.close()
        except socket.error as e:
            print(str(e))
            print('Connection Error')
            sys.exit()


thread = MyPortScan('127.0.0.1')
thread.check_port_socket()
