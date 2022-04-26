#!/usr/bin/python3

import socket
import sys
import subprocess

#To do:
#For loop to rotate through host bit of pingsweep
#Figure out how to either use ICMP to get a changing return value / use a bash command or script to ping Sweep a subnet
#Put in .slice to alter IP address to be inputted as "x.x.x.{hostBit}"

def usageMsg():
    print(f"\nUsage: {sys.argv[0]} [ipAddress] [-sWP]")

def helpMsg():
    print(f"""\nCommand Summary: 
                [-help | -h]     Provides a short guide of how to use the tooling
                [-tS]      Scan all ports through TCP connections""")

if len(sys.argv) < 2:
    usageMsg()
    quit()
if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    helpMsg()
    quit()

def pingSweep(): 
        alteredIP = .slice#####
        for hostBit in range(1,255):
            # Returns a 0 on success | 1 on failure
            ping = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", sys.argv[1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
            if ping == 0:
                print('it worked')
            if ping != 0:
                print("It failed")

def tcpScan():
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

pingSweep()
#tcpScan()

