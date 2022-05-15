#!/usr/bin/python3

from src.functionDefs import hostnameSweep, pingSweep, nullScan, tcpXmasScan, tcpFullConnectScan, tcpSynStealthScan, finScan, startupInterface
import argparse

#To do:
#LOW LEVEL
#FORMAT THE DATA PROPERLY IN ALL THE OTHER DEFS
#FORMAT THE DATA FOR THE SWEEPING FUNCTIONS

#MID LEVEL
#POTENTIALLY USE SCAPY ICMP PACKET **WOULD REQUIRE CHANGE FROM subprocess
#TRY TO REDUCE THE try: except: BLOCKS TO A MENU OR FLAGS **

#HIGH LEVEL
#REFURBISH AND REFINE ALL FUNCTIONS, SEE IF THERE ARE ANY FLAWS OR OBVIOUS IMPROVEMENTS IN THE LOGIC **
#PERHAPS AN ARRAY OF FUNCTIONS CAN BE USED TO GIVE THE THREADING FUNCTION THE NEEDED FUNCTION TO THREAD WITHOUT NEEDING TO HARDCODE IT IN
#TEST THREADING TO SEE IF IMPROVEMENT OR NOT
def main():
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

    startupInterface(args.host)

    if args.tcS:
        tcpFullConnectScan(args.host)
    if args.pS:
        pingSweep(args.host)
    if args.nS:
        nullScan(args.host)
    if args.xS:
        tcpXmasScan(args.host)
    if args.ssS:
        tcpSynStealthScan(args.host)
    if args.fS:
        finScan(args.host)
    if args.hS:
        hostnameSweep(args.host)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit("Keyboard Interruption, exiting!")