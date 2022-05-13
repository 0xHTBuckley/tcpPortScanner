#!/usr/bin/python3

from functionDefs import hostnameSweep, pingSweep, nullScan, tcpXmasScan, tcpFullConnectScan, tcpSynStealthScan, finScan
import tcpPortNames
import sys

#To do:
#Use a bash command or script to ping Sweep a subnet #POTENTIALLY USE SCAPY ICMP PACKET **WOULD REQUIRE CHANGE FROM subprocess
#REFURBISH AND REFINE THE SYNSTEALTH FUNCTION
#TRY TO REDUCE THE try: except: BLOCKS TO A MENU OR FLAGS
#IMPLEMENT ARGPARSE LIBRARY OR OWN TYPE
#TEST THREADING TO SEE IF IMPROVEMENT OR NOT
#KeyError except for all scan success print functions
#PROPERLY FILL IN AND FORMAT THE MAN & USAGE MSG
#CREATE A PROPER BANNER / UI WHEN LAUNCHING PROGRAM
#FORMAT THE GIT REPOSITORY TO BE INTO FOLDER / MAYBE SEPERATE THE DEFS INTO ITS OWN FILE THEN PUT INTO FOLDER ALONG tcpPortNames

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
