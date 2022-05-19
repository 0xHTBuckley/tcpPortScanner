#!/usr/bin/python3

from scanFunctions.nullScan import nullScan
from scanFunctions.xmasScan import xmasScan
from scanFunctions.connectScan import connectScan
from scanFunctions.synStealthScan import synStealthScan
from scanFunctions.finScan import finScan
from sweepFunctions.pingSweep import pingSweep
from sweepFunctions.hostnameSweep import hostnameSweep
import argparse
from time import time, ctime
from socket import gethostbyaddr

#To do:

#HIGH LEVEL
#REFURBISH AND REFINE ALL FUNCTIONS, SEE IF THERE ARE ANY FLAWS OR OBVIOUS IMPROVEMENTS IN THE LOGIC **
#PERHAPS AN ARRAY OF FUNCTIONS CAN BE USED TO GIVE THE THREADING FUNCTION THE NEEDED FUNCTION TO THREAD WITHOUT NEEDING TO HARDCODE IT IN
#TEST THREADING TO SEE IF IMPROVEMENT OR NOT

def startupInterface(host):
    currentTime=time()
    hostname = gethostbyaddr(str(host))
    print(f"Starting port scan at {ctime(currentTime)}")
    print(f"Scan report for {hostname[0]} ({host})")

def main():
    parser = argparse.ArgumentParser(description = "A port scanner that utilises numerous techniques to perform reconnaissance activities.")

    parser.add_argument("host", help = "IP address to scan", action='store')
    parser.add_argument("-tcS", help = "Scan through all ports via standard TCP connections", dest='tcS', action='store_true')
    parser.add_argument("-pS", help = "A ping sweep through a subnet", dest='pS', action='store_true')
    parser.add_argument("-nS", help = "Scan through all ports via NULL scan", dest='nS', action='store_true')
    parser.add_argument("-xS", help = "Scan through all ports via XMAS scan", dest='xS', action='store_true')
    parser.add_argument("-ssS", help = "Scan through all ports via SYN stealth scan", dest='ssS', action='store_true')
    parser.add_argument("-fS", help = "Scan through all ports via FIN scan", dest='fS', action='store_true')
    parser.add_argument("-hS", help = "A hostname sweep through a subnet", dest='hS', action='store_true')

    args = parser.parse_args()

    if args.tcS:
        startupInterface(args.host)
        connectScan(args.host)
    if args.pS:
        pingSweep(args.host)
    if args.nS:
        startupInterface(args.host)
        nullScan(args.host)
    if args.xS:
        startupInterface(args.host)
        xmasScan(args.host)
    if args.ssS:
        startupInterface(args.host)
        synStealthScan(args.host)
    if args.fS:
        startupInterface(args.host)
        finScan(args.host)
    if args.hS:
        hostnameSweep(args.host)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit("\nKeyboard Interruption, exiting!")