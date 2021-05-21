# Threading class using inheritance
import threading
import time
import random

count = 5

def printTime(threadName):
    time.sleep(random.randint(1,5))
    print("%s: %s" % (threadName, time.ctime(time.time())))
    time.sleep(1)

class TimeThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print("Starting " + self.name)
        printTime(self.name)
        print("Exiting " + self.name)

# Create new threads
threadlist = [] 
for i in range(count):
    sthread = "Thread-"+str(i+1)
    threadlist.insert(i,TimeThread(i+1, sthread))

# Start new Threads
for i in range(count):
    threadlist[i].start()

# Join Threads
for i in range(count):
    threadlist[i].join()

print("Exiting Main Thread")