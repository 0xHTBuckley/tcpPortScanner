import threading
from queue import Queue
from scanFunctions.connectScan import connectScan

def connectScanThreader(host):
    while True:
        worker = q.get()
        connectScan(host, worker)
        q.task_done()

q = Queue()

def Thread(host):
    ipaddress = [str(host)]
    for x in range(10):
        t = threading.Thread(target = connectScanThreader, args = ipaddress)
        t.daemon = True
        t.start()
    for worker in range(1, 65536):
        q.put(worker)
    q.join()