from multiprocessing import Process, Pipe

def pipefunction(conn):
    conn.send(['Python pipe send'])
    conn.close()
    
if __name__ == '__main__':
    parent, child = Pipe()
    p = Process(target=pipefunction, args=(child,))
    p.start()
    print ( 'received: ',parent.recv() )  
    p.join()
    print("Exiting main")