from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def price(self):
        return self.price * self.quantity


p1 = Product("Toothpaste", 20.54, 10)
p2 = Product("Toothpaste", 20.54, 10)
p3 = Product("ToothBrush", 5.99, 5)
print(p1)
# dataclass has internally __init__, __repr__. __eq__ on it

print(p1 == p2)
print(p1 == p3)
