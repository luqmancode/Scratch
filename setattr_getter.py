class Details:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


d1 = Details("Mohamed", 24)
d1.display()
setattr(d1, "name", "Luqman")
setattr(d1, "age", 35)
d1.display()
print("Getattr: ", getattr(d1, "age"))
print("Hasattr: ", hasattr(d1, "first_name"))
print("Hasattr2 :", hasattr(d1, "name"))

d1.make = "India"
print(getattr(d1, "make", None))
print(hasattr(d1, "make"))
delattr(d1, "make")
print(hasattr(d1, "make"))
