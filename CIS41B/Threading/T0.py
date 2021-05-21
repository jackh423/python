# start threads by passing function to Thread constructor
import threading
import time
import random

def tfunc(*t):
    time.sleep(random.randint(1,10))
    print('Thread running:  ',t) 
    return

t1 = ("Thread-",1)
t2 = ("Thread-",2)
t3 = ("Thread-",3)

thd1 = threading.Thread(target=tfunc,args=t1)
thd2 = threading.Thread(target=tfunc,args=t2)
thd3 = threading.Thread(target=tfunc,args=t3)

thd1.start() 
thd2.start() 
thd3.start() 

thd1.join()
thd2.join()
thd3.join()