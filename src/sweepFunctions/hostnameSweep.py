import socket
from ipaddress import ip_network

def hostnameSweep(host):
    hostIP = ip_network(host, strict=False)
    for addr in hostIP:
        try:
            scanResult = socket.gethostbyaddr(str(addr))
            if type(scanResult) == tuple:
                print(scanResult[0])
        except socket.herror:
            continue