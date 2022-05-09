#!/usr/bin/python3

import socket
from ipaddress import ip_network
import sys
import subprocess
import random
from scapy.all import sr1, TCP, IP
import tcpCommonPorts

#To do:
#Use a bash command or script to ping Sweep a subnet #POTENTIALLY USE SCAPY ICMP PACKET **WOULD REQUIRE CHANGE FROM subprocess
#REFURBISH AND REFINE THE SYNSTEALTH FUNCTION
#CREATE A REPLICABLE SCAN FOR XMAS // SPEED UP THROUGH THREADING TEST FOR IMPROVEMENT
#TRY TO REDUCE THE try: except: BLOCKS TO A MENU OR FLAGS
#IMPLEMENT ARGPARSE LIBRARY OR OWN TYPE
#IMPLEMENT FIN, NULL, ACK FIREWALL DISCOVERY, WINDOW SCAN
#TEST THREADING TO SEE IF IMPROVEMENT OR NOT

def usageMsg():
    print(f"\nUsage: {sys.argv[0]} [ipAddress] [-htCSpS] [--help]")

def manMsg():
    print(f"""\nCommand Summary: 
                [--help | -h]     Provides a short guide of how to use the tooling
                [-tCS]      Scan all ports through TCP connections
                [-pS]       A ping sweep through a""")

# Usage and help checkers
if len(sys.argv) < 2:
    usageMsg()
    quit()
if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    manMsg()
    quit()

def hostnameSweep():
    hostIP = ip_network(sys.argv[1], strict=False)
    for addr in hostIP:
        try:
            scanResult = socket.gethostbyaddr(str(addr))
            if type(scanResult) == tuple:
                print(scanResult[0])
        except socket.herror:
            continue


def pingSweep(): 
        try:
            hostIP = ip_network(sys.argv[1], strict=False)
            for addr in hostIP:
                # Returns a 0 on success | 1 on failure
                ping = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "0.025", str(addr)], stdout=subprocess.PIPE).wait()
                if ping == 0:
                        print(f"{addr} : Detected as online")
        except KeyboardInterrupt:
            print()

def finScan():
    for dstport in range(0, 65536):
        srcport = random.randint(1, 65535)
        if dstport == srcport:
            srcport += 1
        try:
            scan = sr1(IP(dst = sys.argv[1])/TCP(sport = srcport, dport = dstport, flags = "F"), verbose = 0, timeout = 0.03)
            if scan == None:
                print(f"{dstport} / {tcpCommonPorts.ports[str(dstport)]} : Open | Filtered")
            else:
                continue
        except KeyboardInterrupt:
            quit("\nKeyboard Interrupt, exiting!")

def tcpSynStealthScan():
    for dstport in range(0, 65536):
        srcport = random.randint(1, 65535)
        if dstport == srcport:
            srcport += 1
        try:
            scan = sr1(IP(dst = sys.argv[1])/TCP(sport = srcport, dport = dstport, flags = "S"), verbose = 0, timeout = 0.01)
            if scan == None:
                continue
            if scan.getlayer(TCP).flags == "SA":
                print(f"{dstport} / {tcpCommonPorts.ports[str(dstport)]} : Open")
                sr1(IP(dst = sys.argv[1])/TCP(sport = srcport, dport = dstport, flags = "R"), verbose = 0, timeout = 0.01)
        except KeyboardInterrupt:
            quit("\nKeyboard Interrupt, exiting!")

def tcpXmasScan():
    for dstport in range(0, 65536):
        srcport = random.randint(1, 65535)
        if dstport == srcport:
            srcport =+ 1
        try:
            scan = sr1(IP(dst = sys.argv[1])/TCP(sport = srcport, dport = dstport, flags = "PFU"), verbose = 0, timeout = 0.05)
            if scan == None:
                print(f"{dstport} / {tcpCommonPorts.ports[str(dstport)]} : Open | Filtered")
            else: 
                continue
        except KeyboardInterrupt:
            quit("\nKeyboard Interrupt, exiting!")

def tcpFullConnectScan():
    host = sys.argv[1]
    for port in range(0, 65536):
        try:
            _socketLoop = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            _socketLoop.settimeout(0.01)
            if not _socketLoop.connect_ex((host, port)):
                print(f"Port {port} is open / {tcpCommonPorts.ports[str(port)]}")  
            _socketLoop.close()
        except KeyboardInterrupt:
            print("\nYou have pressed CTRL+C")
            quit("Exiting!")
        except socket.error:
            print("\nUnable to make a connection")
            quit("Exiting!")

#pingSweep()
#tcpFullConnectScan()
#tcpSynStealthScan()
#tcpXmasScan()
#hostnameSweep()
finScan()