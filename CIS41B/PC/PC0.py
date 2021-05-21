
# queue of threads

consumers = 10
producers = 5
cookies = 10
 
import _thread as thread, queue, time
 
cookiejar = queue.Queue()
 
def marge(idnum):
    for msgnum in range(cookies):
        time.sleep(msgnum)
        print("marge"+chr(idnum+ord('A'))+"=> cookie")
        cookiejar.put("put cookie "+ str(idnum))
 
def homer(idnum):
    while True:
        time.sleep(0.1)
        try:
            cookie = cookiejar.get()
        except queue.Empty:
            pass
        else:
            print('homer', chr(idnum+ord('A')), ' got <= ', cookie)
 
if __name__ == '__main__':
    
    for i in range(producers):
        thread.start_new_thread(marge, (i+1,))
        
    for i in range(consumers):
        thread.start_new_thread(homer, (i+1,))
         
    time.sleep(((producers - 1) * cookies) + 1)
    
    print('Main thread exit')