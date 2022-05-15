import random
from scapy.all import sr1, TCP, IP
from tcpServices import serviceList

def tcpSynStealthScan(host):
    print("PORT\tSTATE\tSERVICE")
    for dstport in range(0, 65536):
        srcport = random.randint(1, 65535)
        if dstport == srcport:
            srcport += 1
        try:
            scan = sr1(IP(dst = host)/TCP(sport = srcport, dport = dstport, flags = "S"), verbose = 0, timeout = 0.01)
            if scan == None:
                continue
            if scan.getlayer(TCP).flags == "SA":
                print(f"{dstport}\topen\t{serviceList[str(dstport)]}")
                sr1(IP(dst = host)/TCP(sport = srcport, dport = dstport, flags = "R"), verbose = 0, timeout = 0.01)
        except KeyError:
            print(f"{dstport}\topen\tunknown")
    print("\nPort scan completed")