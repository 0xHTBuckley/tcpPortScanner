from ipaddress import ip_network
from scapy.all import srp, ARP, Ether

def pingSweep(host): 
    print("ACTIVE HOSTS")
    hostIP = ip_network(host, strict=False)
    for addr in hostIP:
        ping = srp(Ether(dst = "ff:ff:ff:ff:ff:ff") / ARP(pdst = str(addr)), verbose = False, retry = 0, timeout = 0.3)[0]
        if ping:
            print(addr)
                
            
