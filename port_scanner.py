#!/usr/bin/python3

import socket
from ipaddress import ip_network
import sys
import subprocess
import random
from scapy.all import sr1, TCP, IP

#To do:
#For loop to rotate through host bit of pingsweep
#Figure out how to either use ICMP to get a changing return value / use a bash command or script to ping Sweep a subnet #POTENTIALLY USE SCAPY ICMP PACKET **WOULD REQUIRE CHANGE FROM subprocess
#REFURBISH AND REFINE THE SYNSTEALTH FUNCTION

def usageMsg():
    print(f"\nUsage: {sys.argv[0]} [ipAddress] [-htCSpS] [--help]")

def helpMsg():
    print(f"""\nCommand Summary: 
                [--help | -h]     Provides a short guide of how to use the tooling
                [-tCS]      Scan all ports through TCP connections
                [-pS]       A ping sweep through a""")

# Usage and help checkers
if len(sys.argv) < 2:
    usageMsg()
    quit()
if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    helpMsg()
    quit()

def pingSweep(): 
        try:
            hostIP = ip_network(sys.argv[1], strict=False)
            for addr in hostIP:
                # Returns a 0 on success | 1 on failure
                ping = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "0.025", str(addr)], stdout=subprocess.PIPE).wait()
                if ping == 0:
                        print(f"{addr} : Detected as online")
        except:
            print("f")

def tcpSynStealthScan():
    for dstport in range(0, 65536):
        srcport = random.randint(1, 65535)
        if dstport == srcport:
            srcport =+ 1
        scan = sr1(IP(dst = sys.argv[1])/TCP(sport = srcport, dport = dstport, flags = "S"), verbose = 0, timeout = 0.025)
        if scan == None:
            print(f"{dstport} closed")
            continue
        try:
            if scan.getlayer(TCP).flags == "SA":
                print(f"{dstport} : Open")
                sr1(IP(dst = sys.argv[1])/TCP(sport = srcport, dport = dstport, flags = "R"), verbose = 0, timeout = 0.025)
        except KeyboardInterrupt:
            print("Keyboard Interrupt!")
            quit("Exiting!")
    print("DONE")


def tcpFullConnectScan():
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
        except socket.error:
            print("\nUnable to make a connection")
            quit("Exiting!")

#pingSweep()
#tcpFullConnectScan()
tcpSynStealthScan()

