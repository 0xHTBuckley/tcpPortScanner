import socket
from ipaddress import ip_network
import sys
from subprocess import Popen, PIPE
import random
from scapy.all import sr1, TCP, IP
import tcpPortNames

def hostnameSweep():
    hostIP = ip_network(sys.argv[1], strict=False)
    for addr in hostIP:
        try:
            scanResult = socket.gethostbyaddr(str(addr))
            if type(scanResult) == tuple:
                print(scanResult[0])
        except socket.herror:
            continue

def pingSweep(): 
        try:
            hostIP = ip_network(sys.argv[1], strict=False)
            for addr in hostIP:
                # Returns a 0 on success | 1 on failure
                ping = Popen(["ping", "-c", "1", "-n", "-W", "0.025", str(addr)], stdout=PIPE).wait()
                if ping == 0:
                        print(f"{addr} : Detected as online")
        except KeyboardInterrupt:
            print()

def nullScan():
    for dstport in range(0, 65536):
        srcport = random.randint(1, 65535)
        if dstport == srcport:
            srcport += 1
        try:
            scan = sr1(IP(dst = sys.argv[1])/TCP(sport = srcport, dport = dstport, flags = ""), verbose = 0, timeout = 0.03)
            if scan == None:
                print(f"{dstport} / {tcpPortNames.ports[str(dstport)]} : Open | Filtered")
            else:
                continue
        except KeyError:
            print(f"{dstport} / unknown : Open | Filtered")

def finScan():
    for dstport in range(0, 65536):
        srcport = random.randint(1, 65535)
        if dstport == srcport:
            srcport += 1
            scan = sr1(IP(dst = sys.argv[1])/TCP(sport = srcport, dport = dstport, flags = "F"), verbose = 0, timeout = 0.03)
            if scan == None:
                print(f"{dstport} / {tcpPortNames.ports[str(dstport)]} : Open | Filtered")
            else:
                continue

def tcpSynStealthScan():
    for dstport in range(0, 65536):
        srcport = random.randint(1, 65535)
        if dstport == srcport:
            srcport += 1
        try:
            scan = sr1(IP(dst = sys.argv[1])/TCP(sport = srcport, dport = dstport, flags = "S"), verbose = 0, timeout = 0.01)
            if scan == None:
                continue
            if scan.getlayer(TCP).flags == "SA":
                print(f"{dstport} / {tcpPortNames.ports[str(dstport)]} : Open")
                sr1(IP(dst = sys.argv[1])/TCP(sport = srcport, dport = dstport, flags = "R"), verbose = 0, timeout = 0.01)
        except KeyboardInterrupt:
            quit("\nKeyboard Interrupt, exiting!")

def tcpXmasScan():
    for dstport in range(0, 65536):
        srcport = random.randint(1, 65535)
        if dstport == srcport:
            srcport =+ 1
        try:
            scan = sr1(IP(dst = sys.argv[1])/TCP(sport = srcport, dport = dstport, flags = "PFU"), verbose = 0, timeout = 0.05)
            if scan == None:
                print(f"{dstport} / {tcpPortNames.ports[str(dstport)]} : Open | Filtered")
            else: 
                continue
        except KeyboardInterrupt:
            quit("\nKeyboard Interrupt, exiting!")

def tcpFullConnectScan(host):
    for port in range(0, 65536):
        try:
            _socketLoop = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            _socketLoop.settimeout(0.01)
            if not _socketLoop.connect_ex((host, port)):
                print(f"Port {port} is open / {tcpPortNames.ports[str(port)]}")  
            _socketLoop.close()
        except KeyboardInterrupt:
            print("\nYou have pressed CTRL+C")
            quit("Exiting!")
        except socket.error:
            print("\nUnable to make a connection")
            quit("Exiting!")
        except KeyError:
            print(f"Port {port} is open / unknown")
