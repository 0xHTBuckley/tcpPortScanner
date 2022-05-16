from ipaddress import ip_network
from scapy.all import sr1, IP, ICMP

def pingSweep(host): 
    hostIP = ip_network(host, strict=False)
    for addr in hostIP:
            # Returns a 0 on success | 1 on failure
        ping = sr1(IP(dst=addr)/ICMP(),verbose = 0, timeout = 0.03)
        if ping == 0:
            print(f"{addr} : online") 