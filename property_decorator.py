class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius should be positive")

    @radius.deleter
    def radius(self):
        print("Called Deleter")
        del self._radius

    @property
    def diameter(self):
        return self._radius * 2


c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 50
print(c.diameter)
c._radius = 6
print(c._radius)

# c.radius = -3
del c.radius
