import class_namespaces_first_file

print("Second file")
class SecondClass(class_namespaces_first_file.FirstClass):
    def display(self):
        return f"Displaying: {self.data}"
    
z = SecondClass()
z.set_data('King Kohli')
print(z.display())


class ThirdClass(SecondClass):
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return ThirdClass(self.data + other)
    
    def __str__(self):
        return f"Third Class: {self.data}"

    def mul(self, other):
        return self.data * other

a = ThirdClass('abc')
print(a.display())
print(a)

b = a + 'xyz'
print(b)
print(b.display()) # due to return ThirdClass(self.data + other)

print(a.mul(3))




