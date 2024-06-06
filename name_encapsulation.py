class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def _internal_method(self):
        pass

    def public_method(self):
        pass 

a1 = A()
print(a1._internal)
print(a1.public)
a1._internal_method()
a1.public_method()

class B:
    def __init__(self):
        self.__private = 2 # Non overridable on inheritance but override in 3.10 version
        self.public = 3

    def __private_method(self):
        return f"{self.__private}"
    
    def public_method(self):
        return self.__private_method()

b1 = B()
# print(b1.__private) // AttributeError: 'B' object has no attribute '__private'. Did you mean: '_B__private'?
print(b1.public)
# print(b1.__private_method()) // AttributeError: 'B' object has no attribute '__private_method'. Did you mean: '_B__private_method'?
print(b1.public_method())

class C(A):
    def __init__(self):
        self._internal = 4
        self.public = 5

    def _internal_method(self):
        return "I am new method overriding the base method"
    
    def public_method(self):
        return "I am overriding the base method"
    
c1 = C()
print(c1._internal)
print(c1.public)
print(c1._internal_method())
print(c1.public_method())

class D(B):
    def __init__(self):
        self.__private = 6
        self.public = 7

    def __private_method(self):
        print("I am private method overriding the base method")
        return self.__private
    
    def public_method(self):
        print("I am the public method overriding the base method")
        return self.__private_method()
    
d1 = D()
print(d1.public)
print(d1.public_method())
print('-'*50)
##########################################################################

# Example of using __ method name to implement a 
# non-overrideable method

class B:
    def __init__(self):
        self.__private = 8
    def __private_method(self):
        print('B.__private_method', self.__private)

    def public_method(self):
        self.__private_method()

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 9      # Does not override B.__private but here its override to 9 as result
    # Does not override B.__private_method()
    def __private_method(self):
        print('C.__private_method', self.__private)

    def public_method(self):
        self.__private_method()

c = C()
c.public_method()