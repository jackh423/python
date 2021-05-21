from multiprocessing import Process

def display(val):
    print ("display ",val)
    
if __name__ == '__main__':
    p1 = Process(target=display,args=(1,))
    p2 = Process(target=display,args=(2,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("Exiting main")