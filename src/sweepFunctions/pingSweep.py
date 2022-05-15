from ipaddress import ip_network
from subprocess import Popen, PIPE

def pingSweep(host): 
    hostIP = ip_network(host, strict=False)
    for addr in hostIP:
            # Returns a 0 on success | 1 on failure
        ping = Popen(["ping", "-c", "1", "-n", "-W", "0.025", str(addr)], stdout=PIPE).wait()
        if ping == 0:
            print(f"{addr} : Detected as online")