"""
Version: 0.1
Author: João Paulo Andrade
Data: 06/10/2019
Description: Script to scan port of hosts
"""

import socket
import sys
import errno
import os
import argparse
import ipaddress


class MyPortScan(object):

    def __init__(self, ip, portlist):
        self.ip = ip
        if type(portlist) is str:
            self.portlist = [int(x) for x in portlist.split(',')]
        else:
            self.portlist = portlist

    def check_port_socket(self):

        try:
            for port in self.portlist:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                result = s.connect_ex((str(self.ip), port))
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scan ports TCP\nVersion: 0.1')
    parser.add_argument('-t', dest='target', help='Target host IPv4', type=ipaddress.IPv4Address, required=True)
    parser.add_argument('-p', dest='ports', help='Ports separated by comma', type=str, default=[21, 22, 23, 53, 80, 443,
                                                                                                3389, 389, 3306, 1521,
                                                                                                8080, 8000])
    params = parser.parse_args()
    m = MyPortScan(params.target, params.ports)
    m.check_port_socket()
