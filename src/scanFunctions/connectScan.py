import socket
from threading import Lock
from scanFunctions.serviceList import serviceList

locked = Lock()

def connectScan(host, port):
    liveSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        liveSocket.connect((host, port))
        with locked:
            print(f"{port}\topen\t{serviceList[str(port)]}")  
        liveSocket.close()
    except KeyError:
        print(f"{port}\topen\tunknown")
    except:
        pass