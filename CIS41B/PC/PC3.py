
# condition
import threading
import time
import random

condition = threading.Condition()
cookiejar = []

class Homer(threading.Thread):
    def run(self):
        global cookiejar
        time_elapsed = 0.0
        while True:
            if time_elapsed > 0.5:
                return
            condition.acquire()
            print("homer acquiring condition")
            if not cookiejar:
                print("Nothing in cookiejar, consumer will wait.")
                condition.wait()
                print("Producer added something to cookiejar - consumer will stop waiting.")
            cookie = cookiejar.pop(0)
            print("Consumed", cookie)
            print("Homer releasing lock")
            condition.release()
            time.sleep(0.1)
            time_elapsed += 0.1
            
class Marge(threading.Thread):
    def run(self):
        cookie = 1
        global cookiejar
        time_elapsed = 0.0
        while True:
            if time_elapsed > 0.5:
                return
            condition.acquire()
            print("Marge acquiring condition")
            cookiejar.append(cookie)
            print("Produced", cookie)
            condition.notify()
            print("Marge releasing condition")
            condition.release()
            cookie += 1
            time.sleep(0.1)
            time_elapsed += 0.1
            
Marge().start()
Homer().start()