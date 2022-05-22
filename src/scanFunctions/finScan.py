import random
from scapy.all import sr1, TCP, IP
from scanFunctions.serviceList import serviceList
from threading import Lock

locked = Lock()

def finScan(host, dstport):
    srcport = 80
    if dstport == srcport:
        srcport += 1
    try:    
        scan = sr1(IP(dst = host)/TCP(sport = srcport, dport = dstport, flags = "F"), verbose = 0, timeout = 1)
        if scan != None:
            pass
        else:
            with locked:
                print(f"{dstport}\topen|filtered\t{serviceList[str(dstport)]}")
    except KeyError:
        with locked:
            print(f"{dstport}\topen|filtered\tunknown")