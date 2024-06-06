class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("New name should be a string")
        self._first_name = new_name
        
    @first_name.deleter
    def first_name(self):
        raise AttributeError('First Name should not be deleted')
    
    def get_last_name(self):
        return self._last_name
    
    def set_last_name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError('Name should be string')
        self._last_name = new_name

    def del_last_name(self):
        raise AttributeError("last_name should not be deleted")
    
    name = property(get_last_name, set_last_name, del_last_name)
    # This property method is not working properly


p = Person('Mohamed', 'emp1')
print(p._first_name)
print(p.first_name)
# del p.first_name  // AttributeError: First Name should not be deleted
# p.first_name = 80 // ValueError: New name should be a string
p.first_name = 'Luqman'
print(p._first_name)

print(p._last_name)
print(p.last_name)
p.last_name = 'emp2'
print(p.last_name)