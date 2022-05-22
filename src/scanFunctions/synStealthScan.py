import random
from scapy.all import sr1, TCP, IP
from scanFunctions.serviceList import serviceList
from threading import Lock

locked = Lock()

def synStealthScan(host, dstport):
    srcport = 80
    if dstport == srcport:
        srcport += 1
    try:
        scan = sr1(IP(dst = host)/TCP(sport = srcport, dport = dstport, flags = "S"), verbose = 0, timeout = 0.01)
        if scan == None:
            pass
        if scan.getlayer(TCP).flags == "SA":
            with locked:
                print(f"{dstport}\topen\t{serviceList[str(dstport)]}")
        sr1(IP(dst = host)/TCP(sport = srcport, dport = dstport, flags = "R"), verbose = 0, timeout = 0.01)
    except KeyError:
        with locked:
            print(f"{dstport}\topen\tunknown")
    except: 
        pass