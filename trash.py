from multiprocessing import Process
import os
import time

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    for i in range(4):
    # info('function f')
        time.sleep(1)
        print('hello', name)

def g(name):
    for i in range(4):
    # info('function f')
        time.sleep(1)
        print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    r = Process(target=g, args=('karl',))
    p.start()
    time.sleep(0.5)
    r.start()
    p.join()
    r.join()