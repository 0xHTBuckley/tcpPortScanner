#!/usr/bin/python3

from sweepFunctions.pingSweep import pingSweep
from sweepFunctions.hostnameSweep import hostnameSweep
from threadingFunctions.connectScanThreader import connectScanThread
from threadingFunctions.finScanThreader import finScanThread
from threadingFunctions.nullScanThreader import nullScanThread
from threadingFunctions.synStealthScanThreader import synStealthScanThread
from threadingFunctions.xmasScanThreader import xmasScanThread
from threadingFunctions.defaultScanThreader import defaultScanThread
import argparse
from time import time, ctime
from socket import gethostbyaddr

def startupScanInterface(host):
    currentTime=time()
    hostname = gethostbyaddr(str(host))
    print(f"Starting port scan at {ctime(currentTime)}")
    print(f"Scan report for {hostname[0]} ({host})")
    print("PORT\tSTATE\tSERVICE")

def startupSweepInterface():
    currentTime=time()
    print(f"Starting network sweep at {ctime(currentTime)}")

def main():
    parser = argparse.ArgumentParser(description = "A port scanner that utilises numerous techniques to perform reconnaissance activities.")

    parser.add_argument("host", help = "IP address to scan", action='store')
    parser.add_argument("-cS", help = "Scan through all ports via standard TCP connections", dest='cS', action='store_true')
    parser.add_argument("-pS", help = "A ping sweep through a subnet", dest='pS', action='store_true')
    parser.add_argument("-nS", help = "Scan through all ports via NULL scan", dest='nS', action='store_true')
    parser.add_argument("-xS", help = "Scan through all ports via XMAS scan", dest='xS', action='store_true')
    parser.add_argument("-ssS", help = "Scan through all ports via SYN stealth scan", dest='ssS', action='store_true')
    parser.add_argument("-fS", help = "Scan through all ports via FIN scan", dest='fS', action='store_true')
    parser.add_argument("-hS", help = "A hostname sweep through a subnet", dest='hS', action='store_true')

    args = parser.parse_args()

    if args.cS:
        startupScanInterface(args.host)
        connectScanThread(args.host)
        quit()
    if args.pS:
        startupSweepInterface()
        pingSweep(args.host)
        quit()
    if args.nS:
        startupScanInterface(args.host)
        nullScanThread(args.host)
        quit()
    if args.xS:
        startupScanInterface(args.host)
        xmasScanThread(args.host)
        quit()
    if args.ssS:
        startupScanInterface(args.host)
        synStealthScanThread(args.host)
        quit()
    if args.fS:
        startupScanInterface(args.host)
        finScanThread(args.host)
        quit()
    if args.hS:
        startupSweepInterface()
        hostnameSweep(args.host)
        quit()
    if args.host:
        startupScanInterface(args.host)
        defaultScanThread(args.host)
        quit()




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit("\nKeyboard Interruption, exiting!")