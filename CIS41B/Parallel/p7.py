from multiprocessing import Process, Manager

def func(dct, m):
    dct[1] = '11'
    dct['2'] = 22
    dct[0.25] = 0.33
    m.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        dct = manager.dict()
        ml = manager.list(range(10))

        p = Process(target=func, args=(dct, ml))
        p.start()
        p.join()

        print(dct)
        print(ml)
        
        print("Exiting main")