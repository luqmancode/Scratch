class Math:
    
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

print(Math.add(5, 7))
print(Math.multiply(9, 5))
# Both works
m = Math()
print(m.add(3, 4))
print(m.multiply(2, 7))