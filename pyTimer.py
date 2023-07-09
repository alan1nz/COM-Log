import threading
from time import sleep
import queue

def the_function():
    while 1:
        # print("LGBTQ")
        v = q.get()
        print(v)
        sleep(5)

def the_function1():
    i = 0
    while 1:
        i += 1
        q.queue.clear()

        q.put_nowait(i)
        
        sleep(0.1)

q = queue.Queue(1)
# t = threading.Timer(5,the_function)
# t.start()

t = threading.Thread(target= the_function,name="wdf", daemon=True)
t1 = threading.Thread(target=the_function1)
t.start()
t1.start()


    