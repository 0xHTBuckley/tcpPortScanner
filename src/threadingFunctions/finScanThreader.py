import threading
from queue import Queue
from scanFunctions.finScan import finScan

def connectScanThreader(host):
    while True:
        worker = queueOfPorts.get()
        finScan(host, worker)
        queueOfPorts.task_done()

queueOfPorts = Queue()

def finScanThread(host):
    ipaddress = [str(host)]
    for x in range(10):
        scanningThread = threading.Thread(target = connectScanThreader, args = ipaddress)
        scanningThread.daemon = True
        scanningThread.start()
    for worker in range(1, 65536):
        queueOfPorts.put(worker)
    queueOfPorts.join()