from multiprocessing import Process, Lock

def display(k, n):
    k.acquire()
    print ('Hi', n)
    k.release()
    
if __name__ == '__main__':
    lock = Lock()
    names = ['Alice', 'Bob', 'Carol', 'Dennis']
    for n in names:
        p = Process(target=display, args=(lock,n,))
        p.start()
        p.join()
    
    print("Exiting main")