import sys

class Date:
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

d1 = Date('2024', '5', '30')
print(sys.getsizeof(d1))

class DateSlots:
    __slots__ = ['year', 'month', 'date']

    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

d2 = DateSlots('2024', '5', '30')
print(sys.getsizeof(d2))
