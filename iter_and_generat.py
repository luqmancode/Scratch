prices = [1, 4, 5, 565, 2, 232]
price_iter = iter(prices)
print(next(price_iter)) # 1
print(price_iter.__next__()) # 4

while True:
    try:
        print(price_iter.__next__())

    except StopIteration:
        break

class InfiniteNaturalNumber:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.num += 1
        return self.num
    
infi = iter(InfiniteNaturalNumber())
print(infi, type(infi))

print(next(infi))
print(next(infi))
print(infi.__next__())
print(infi.__next__())
print(infi.__next__())
print(infi.__next__())
print(infi.__next__())

def generate_natur_num(num: int = 0):
    while True:
        yield num
        num += 1


for num in generate_natur_num():
    print(num)