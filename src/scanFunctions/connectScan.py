import socket
from tcpServices import serviceList

def connectScan(host):
    print("PORT\tSTATE\tSERVICE")
    for port in range(0, 65536):
        try:
            _socketLoop = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            _socketLoop.settimeout(0.01)
            if not _socketLoop.connect_ex((host, port)):
                print(f"{port}\topen\t{serviceList[str(port)]}")  
            _socketLoop.close()
        except socket.error:
            print("\nUnable to make a connection")
            quit("Exiting!")
        except KeyError:
            print(f"{port}\topen\tunknown")
    print("\nPort scan completed")