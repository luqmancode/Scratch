from typing import Optional, Callable

count: int = 5


def add_numbers(n1: int, n2: int) -> None:
    print("Sum of numbers: ", n1 + n2)


add_numbers(5, 60)

prices: list[float] = [1.9, 2.3, 3, 5.5]
oil_gallon: tuple[int, int, float] = (4, 5, 1.5)
student: dict[str, int] = {"john": 56, "Lela": 18}

class Person:
    def __init__(self, name: str, age: int, weight: Optional[float] = None):
        self.name = name
        self.age = age
        self.weight = weight

p1 = Person('Mike', 49)
p2 = Person('Hillary', 13, 23)

persons: list[Person] = [p1, p2]

def smart_divide(func: Callable[[int, int], int | float]):
    def inner(a, b):
        if b == 0:
            raise ZeroDivisionError("demonimator should not be zero to divide")
            # print("demonimator should not be zero to divide")
        return func(a, b)
    return inner

@smart_divide
def divide(a: int, b: int) -> int | float :
    return a/b

print(divide(5, 0))




