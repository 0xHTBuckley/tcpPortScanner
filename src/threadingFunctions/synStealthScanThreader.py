import threading
from queue import Queue
from scanFunctions.synStealthScan import synStealthScan

def connectScanThreader(host):
    while True:
        worker = queueOfPorts.get()
        synStealthScan(host, worker)
        queueOfPorts.task_done()

queueOfPorts = Queue()

def synStealthScanThread(host):
    ipaddress = [str(host)]
    for x in range(10):
        scanningThread = threading.Thread(target = connectScanThreader, args = ipaddress)
        scanningThread.daemon = True
        scanningThread.start()
    for worker in range(1, 65536):
        queueOfPorts.put(worker)
    queueOfPorts.join()