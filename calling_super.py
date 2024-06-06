class A:
    def spam(self):
        print("A.spam")

class B(A):
    def spam(self):
        super().spam()
        print("B.spam")

a1 = A()
a1.spam()
b1 = B()
b1.spam()

class C:
    def __init__(self):
        self.x = 0

class D(C):
    def __init__(self):
        super().__init__()
        self.y = 1

d1 = D()
print(d1.x)
print(d1.y)

# dont understand anything here
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)
    
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)

p = Proxy('sun')
print(p)
print(getattr(p, 'sun', None))
# print(getattr(p, 'obj'))
setattr(p, 'sex', 'Male')
print(getattr(p, 'sex'))