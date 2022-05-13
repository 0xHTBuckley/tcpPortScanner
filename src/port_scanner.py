#!/usr/bin/python3

from functionDefs import hostnameSweep, pingSweep, nullScan, tcpXmasScan, tcpFullConnectScan, tcpSynStealthScan, finScan
#import tcpPortNames ##FIGURE OUT IF NEEDED IN THIS FILE OR NO
import sys
import argparse

#To do:
#LOW LEVEL
#KeyError except for all scan success print functions **
#PROPERLY FILL IN AND FORMAT THE MAN & USAGE MSG
#CREATE A PROPER BANNER / UI WHEN LAUNCHING PROGRAM
#INPUT ALL FUNCTIONS INTO THE ARGPARSE BLOCK OF CODE

#MID LEVEL
#POTENTIALLY USE SCAPY ICMP PACKET **WOULD REQUIRE CHANGE FROM subprocess
#REFURBISH AND REFINE ALL FUNCTIONS, SEE IF THERE ARE ANY FLAWS OR OBVIOUS IMPROVEMENTS IN THE LOGIC **
#TRY TO REDUCE THE try: except: BLOCKS TO A MENU OR FLAGS **

#HIGH LEVEL
#PERHAPS AN ARRAY OF FUNCTIONS CAN BE USED TO GIVE THE THREADING FUNCTION THE NEEDED FUNCTION TO THREAD WITHOUT NEEDING TO HARDCODE IT IN
#FOLLOWING SIMILAR METHODOLOGY TO THE TCPCONNECT FUNC, CHANGE ALL FUNCTIONS TO ACCEPT THE HOST IP ADDRESS INSTEAD OF BEING HARDCODED WITH SYS.ARGV[1]
#TEST THREADING TO SEE IF IMPROVEMENT OR NOT

parser = argparse.ArgumentParser(description = "A port scanner that utilises numerous techniques to perform reconnaissance activities.")

parser.add_argument("host", help = "IP address to scan", action='store')   
parser.add_argument("-tcS", help = "Scan through all ports via standard TCP connections", dest='tcS', action='store_true')
parser.add_argument("-pS", help = "A ping sweep through a subnet", dest='pS', action='store_true')
parser.add_argument("-nS", help = "Scan through all ports via null scan", dest='nS', action='store_true')
parser.add_argument("-xS", help = "Scan through all ports via XMAS scan", dest='xS', action='store_true')
parser.add_argument("-ssS", help = "Scan through all ports via SYN stealth scan", dest='ssS', action='store_true')
parser.add_argument("-fS", help = "Scan through all ports via FIN scan", dest='fS', action='store_true')
parser.add_argument("-hS", help = "A hostname sweep through a subnet", dest='hS', action='store_true')

args = parser.parse_args()


if args.tcS:
    tcpFullConnectScan(args.host)
if args.pS:
    print("Completing the pS function")
if args.nS:
    print("Completing the nS function")
if args.xS:
    print("Completing the xS function")
if args.ssS:
    print("Completing the ssS function")
if args.fS:
    print("Completing the fS function")
if args.hS:
    print("Completing the hS function")

def usageMsg():
    print(f"""\nUsage: {sys.argv[0]} [ipAddress] [-htcSpSnS] [--help]
    
To see the complete list of arguments, supply the -h or --help argument.
    """)

# Usage and help checkers
if len(sys.argv) < 2:
    usageMsg()
    quit()
