
# lock

import sys
import random
import time
import threading

threadLock = threading.Lock()

class marge(threading.Thread):
    def __init__(self, cookies):
        threading.Thread.__init__(self)
        self.cookies = cookies
    def produce(self):
        threadLock.acquire()
        print("marge acquires lock")
        self.cookies.append(1)
        print("{}: produced".format(self.name))
        print("marge releases lock")
        threadLock.release()
    def wait(self):
        time.sleep(random.uniform(0, 3))
    def run(self):
        while True:
            self.produce()	

class homer(threading.Thread):
    def __init__(self, cookies):
        threading.Thread.__init__(self)
        self.cookies = cookies
    def consume(self):
        threadLock.acquire()
        print("homer acquires lock")
        if len(self.cookies) > 0:
            cookie = self.cookies.pop()
            print("{}: consumed".format(self.name))
        print("homer releases lock")
        threadLock.release()
    def wait(self):
        time.sleep(random.uniform(0, 3))
    def run(self):
        while True:
            self.consume()

if __name__ == "__main__":
    count_producers = 3
    count_consumers = 3
    buffer_length = 10

    cookies = []
    producers = []
    consumers = []

    for i in range(count_producers):
        producers.append(marge(cookies))
        producers[-1].start()

    for i in range(count_consumers):
        consumers.append(homer(cookies))
        consumers[-1].start()

    for p in producers:
        p.join()

    for c in consumers:
        c.join()