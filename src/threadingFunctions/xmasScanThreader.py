import threading
from queue import Queue
from scanFunctions.xmasScan import xmasScan

def xmasScanThreader(host):
    while True:
        worker = queueOfPorts.get()
        xmasScan(host, worker)
        queueOfPorts.task_done()

queueOfPorts = Queue()

def xmasScanThread(host):
    ipaddress = [str(host)]
    for x in range(10):
        scanningThread = threading.Thread(target = xmasScanThreader, args = ipaddress)
        scanningThread.daemon = True
        scanningThread.start()
    for worker in range(1, 65536):
        queueOfPorts.put(worker)
    queueOfPorts.join()