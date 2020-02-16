#! /usr/bin/python3
"""
Version: 0.1
Author: João Paulo Andrade
Data: 15/02/2020
Description: Sample scrip for scan host ports with only buit-in functions
This code just works with addresses of v4 family.
Python 3.x
"""

# Import modules
import socket
import sys
import errno
import os
import argparse
import ipaddress

# Main Class
class MyPortScanner(object):

    # Constructor, receive two parameters: target = IP that will be scanned and list of port that will be tested
    def __init__(self, target, portlist):
        self.target = target
        if type(portlist) is str:
            self.portlist = [int(x) for x in portlist.split(',')]
        else:
            self.portlist = portlist

    # Function that performs the scan on v4 family
    def check_port_socket_v4_tcp(self):

        print('--------------------------------')
        print('[+] Initializing scan...')
        print('[i] Target host: {}'.format(self.target))
        print('[i] Ports: {}'.format(self.portlist))

        try:
            for port in self.portlist:
                # Create the v4 socket, AF_INET == V4 Family, SOCK_STREAM == TCP
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # Define the timeout of response to 3 seconds
                s.settimeout(3)
                result = s.connect_ex((str(self.target), port))
                # If the return code is 0 then the port is OPEN
                if result == 0:
                    print('[+] Port {}: Open'.format(port))
                # Otherwise, the port is closed
                else:
                    print('[!] Port {}: Closed'.format(port))
                    print('\t[-] Code error: {}'.format(errno.errorcode[result]))
                    print('\t[-] Message: {}'.format(os.strerror(result)))
                s.close()
        # If have any problem with connection, the scan will be aborted
        except socket.error as e:
            print(str(e))
            print('[-] Connection Error')
            sys.exit()

        print('[+] Script finished.')


# Performs the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scan ports TCP\nVersion: 0.1')
    # Target parameter, accept just IPV4 Address
    parser.add_argument('-t', dest='target_host_v4', help='Target host IPv4', required=True, type=ipaddress.IPv4Address)
    # Port that will be scanned, if this parameter not been set then the default ports will be scanned
    parser.add_argument('-p', dest='ports', help='Ports separated by comma', type=str, default=[21, 22, 23, 53, 80, 443,
                                                                                                3389, 389, 3306, 1521,
                                                                                                8080, 8000])
    params = parser.parse_args()
    # Create an instance of MyPortScanner
    m = MyPortScanner(params.target_host_v4, params.ports)
    # Call the function check_port_socket_v4_tcp
    m.check_port_socket_v4_tcp()
