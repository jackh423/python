# multiple threads
import threading
import time
import random
 
tlist = []
count = 10

def tfunc(*n):
    time.sleep(random.randint(1,5))
    print('Thread running:  ',n) 
    return
 
for i in range(count):
    t = ('Thread-',i+1)
    thd = threading.Thread(target=tfunc,args=t)
    tlist.append(thd)

for i in range(count):
    tlist[i].start()
    
for i in range(count):
    tlist[i].join()
    