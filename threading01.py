from ExperimentManagement import ExperimentManager
from ESP import ESP32
from threading import Thread
from multiprocessing import Process
import time



def thread_func1(*args):

    for i in range(10):
       print(['a'])
       time.sleep(1)
    
if __name__ == '__main__':
    a = ExperimentManager()
    t1 = Process(target=thread_func1, args=())
    # time.sleep(1)
    # t2 = Process(target=a.begin(), args=())
    t1.start()
    a.begin()
    print('b')

    # t2.start()
    t1.join()
    # t2.join()