class FirstClass:
    def set_data(self, value):
        self.data = value

    def display(self):
        return self.data
x = FirstClass()
y = FirstClass()
# print(x.display()) # AttributeError: 'FirstClass' object has no attribute 'data'
x.set_data('King Authur')
y.set_data(3.14)
print(x.display())
print(y.display())

x.data = 5.45
print(x.display())
print(y.display())


