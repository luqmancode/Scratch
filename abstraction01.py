from abc import ABC, ABCMeta, abstractmethod
from math import pi

class Shape(metaclass=ABCMeta):

    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__('Rectangle')
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return (self.length + self.breadth) * 2

class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * pi * self.radius
    
# s1 = Shape('Square') TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter
r = Rectangle(5, 8)
print(r.area())
print(r.perimeter())
print(r.shape_type)

c = Circle(6)
print(c.area())
print(c.perimeter())