from ExperimentManagement import ExperimentManager
from ESP import ESP32
from threading import Thread

def thread_func1(*args):
    for i in range(10):
        print(['a'])
    

def thread_func2(*args):
    for i in range(10):
        print(['b'])

t1 = Thread(target=thread_func1, args=())
t2 = Thread(target=thread_func2, args=())

t1.start()
t2.start()

t1.join()
t2.join()