from multiprocessing import Process, Manager
import os

def process1(q):
    q.put("Hello")
    print("process1: ", os.getpid())

def process2(q):
    print("process2: ", q.get())
    print("process2: ", os.getpid())

with Manager() as manager:
    print("main process: ", os.getpid())
    q = manager.Queue()

    p1 = Process(target=process1, args=(q,))
    p2 = Process(target=process2, args=(q,))

    print("a")
    print("is_alive: ", p1.is_alive())
    p1.start()
    print("p1: ", p1.pid, p1.is_alive())
    print("b")
    p2.start()
    print("p2: ", p2.pid, p2.is_alive())
    print("c")
    # p1.join()
    print("d")
    p2.join() # If not called any process to join throwing FileNotFoundError in making connection
    print("e")
    print(p1.is_alive(), p2.is_alive())