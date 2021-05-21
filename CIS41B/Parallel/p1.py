from multiprocessing import Process

numbers = [3, 4, 5, 6, 7, 8]

def cube(x):
    for x in numbers:
        print('%s cube  is  %s' % (x, x**3))
        
if __name__ == '__main__':
    p1 = Process(target=cube, args=('x',))
    p1.start()
    p1.join()
    print ("Exiting main")