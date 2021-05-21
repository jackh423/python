# queue lock
import queue
import threading
import time

exitFlag = False


def processData(threadName, q):
    while not exitFlag:
        if not workQueue.empty():
            queueLock.acquire()
            data = q.get()
            print("%s processing %s" % (threadName, data))
            queueLock.release()
        time.sleep(1)


class TimeThread (threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        print("Starting " + self.name)
        processData(self.name, self.q)
        print("Exiting " + self.name)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []

# Create new threads
for tName in threadList:
    thread = TimeThread(tName, workQueue)
    threads.append(thread)
    thread.start()

# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = True

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")