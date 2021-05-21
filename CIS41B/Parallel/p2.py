from multiprocessing import Process

numbers = [3, 4, 5, 6, 7, 8]

def cube(x):
    for x in numbers:
        print('%s cube  is  %s' % (x, x**3))
        
def evenno(x):
    for x in numbers:
        if x % 2 == 0:
            print('%s is an even number ' % (x))
            
if __name__ == '__main__':
    process1 = Process(target=cube, args=('x',))
    process2 = Process(target=evenno, args=('x',))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print("Exiting main")