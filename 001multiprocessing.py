from multiprocessing import Process, Queue
import sys 

def process1(q):
    q.put('Hello')

def process2(q):
    print(q.get())

q = Queue()
print(q, type(q), sys.getsizeof(q)) # <multiprocessing.queues.Queue object at 0x7cad2df27b00> <class 'multiprocessing.queues.Queue'> 48

p1 = Process(target=process1, args=(q,))
p2 = Process(target=process2, args=(q,))
print("a")
p1.start()
print("b")
p2.start()
print("c")
# p1.join()
print("d")
# p2.join()
print("e")