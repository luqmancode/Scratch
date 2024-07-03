class Person:
    species = "Homo sapiens"

    @classmethod
    def tell_me(cls):
        print(f"Called {cls}")
        return cls.species


print(Person.tell_me())
p = Person
print(p.tell_me())
