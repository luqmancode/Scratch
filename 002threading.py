from threading import Thread
import time
from datetime import datetime

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

@timer
def cuber(x):
    time.sleep(5)
    print(x * x * x)

@timer
def square(x):
    time.sleep(10)
    print(x * x)

if __name__ == "__main__":
    t1 = Thread(target=cuber, args=(5,))
    t2 = Thread(target=square, args=(5,))
    t1.start()
    t2.start()
    print("Hi")
    # t1.join()
    t2.join()
    print("Hello")