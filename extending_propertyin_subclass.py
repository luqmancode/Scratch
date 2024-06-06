class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('value should be string')
        self._name = value
        
    @name.deleter
    def name(self):
        raise AttributeError("name should not be deleted")
    
p1 = Person('mohamed')
print(p1.name)
p1.name = 'Luqman'
print(p1.name)
# del p1.name AttributeError: name should not be deleted

class SubPerson(Person):
    
    @property
    def name(self):
        print("Getting the name")
        return super().name
    
    @name.setter
    def name(self, value):
        print("calling the setter")
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print("Deleting the name")
        del self._name

sp1 = SubPerson('Mohamed')
print(sp1.name)
sp1.name = 'luqman'
print(sp1.name)
del sp1.name