#!/usr/bin/python3

import socket
import sys

def usageMsg():
    print(f"""\nUsage: python3 {sys.argv[0]} [ipAddress] [-sWP]
            
            Command Summary: 
                [-help | -h]     Provides a short guide of how to use the tooling
                [-sWP]      Scan well known port range (1 - 1023)""")

if len(sys.argv) < 2 or sys.argv[1] == "-help":
    usageMsg()
    quit()

def scanPorts():
    host = sys.argv[1]
    for port in range(0, 65536):
        try:
            _socketLoop = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            _socketLoop.settimeout(0.01)
            if not _socketLoop.connect_ex((host, port)):
                print(f"Port {port} is open")
                _socketLoop.close()    
        except KeyboardInterrupt:
            print("\nYou have pressed CTRL+C")
            quit("Exiting!")
        _socketLoop.close()

scanPorts()

