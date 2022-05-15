import random
from scapy.all import sr1, TCP, IP
from tcpServices import serviceList

def nullScan(host):
    print("PORT\tSTATE\tSERVICE")
    for dstport in range(0, 65536):
        srcport = random.randint(1, 65535)
        if dstport == srcport:
            srcport += 1
        try:
            scan = sr1(IP(dst = host)/TCP(sport = srcport, dport = dstport, flags = ""), verbose = 0, timeout = 0.03)
            if scan == None:
                print(f"{dstport}\topen | filtered\t{serviceList[str(dstport)]}")
            else:
                continue
        except KeyError:
            print(f"{dstport}\topen | filtered\tunknown")
    print("\nPort scan completed")