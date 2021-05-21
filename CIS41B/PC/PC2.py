
# semiphore

import sys
import random
import time
from threading import *

class marge(Thread):
    def __init__(self, cookies, semiproduce, semiconsume):
        Thread.__init__(self)
        self.cookies = cookies
        self.semiproduce = semiproduce
        self.semiconsume = semiconsume
    def produce(self):
        self.cookies.append(1)
        print("{}: produced".format(self.name))
    def wait(self):
        time.sleep(random.uniform(0, 3))
    def run(self):
        while True:
            self.wait()
            self.semiproduce.acquire()
            print("marge acquiring semiphore")
            self.produce()
            print("marge releasing semiphore")
            self.semiconsume.release()
class homer(Thread):
    def __init__(self, cookies, semiproduce, semiconsume):
        Thread.__init__(self)
        self.cookies = cookies
        self.semiproduce = semiproduce
        self.semiconsume = semiconsume
    def consume(self):
        cookie = self.cookies.pop()
        print("{}: consumed".format(self.name))
    def wait(self):
        time.sleep(random.uniform(0, 3))
    def run(self):
        while True:
            self.wait()
            self.semiconsume.acquire()
            print("homer acquiring semiphore")
            self.consume()
            print("homer releasing semiphore")
            self.semiproduce.release()
if __name__ == "__main__":
    count_producers = 3
    count_consumers = 3
    buffer_length = 10

    items = []
    producers = []
    consumers = []

    #acquire while buffer is not full
    semiproduce = Semaphore(buffer_length)

    #acquire while buffer is not empty
    semiconsume = Semaphore(0)

    for i in range(count_producers):
        producers.append(marge(items, semiproduce, semiconsume))
        producers[-1].start()

    for i in range(count_consumers):
        consumers.append(homer(items, semiproduce, semiconsume))
        consumers[-1].start()

    for p in producers:
        p.join()

    for c in consumers:
        c.join()