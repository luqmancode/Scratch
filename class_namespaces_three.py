class Rec: pass
print(Rec)
Rec.name = 'Bob'
Rec.age = 40

print(Rec.name, Rec.age)

x = Rec()
y = Rec()
print(x.name, x.age)
print(y.name, y.age)

x.name = 'Sue'
print(Rec.name, x.name, y.name)

print(1, Rec.__dict__)
print(2, x.__dict__)
print(3, y.__dict__)