class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        print(self)
        return f"Pair({self.x}, {self.y})"

    def __str__(self):
        return f"{self.x}, {self.y}"

p1 = Point(5, 3)
print(p1)
