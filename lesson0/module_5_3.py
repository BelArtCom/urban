class House():
    def __init__(self, name, number_of_floors ):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

# eq (==)
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

# lt (<)
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

# le (<=)
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

# gt (>)
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

# ge (>=)
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

# ne (!=)
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

# add (+n)
    def __add__(self, value):
        self.number_of_floors += value
        return self

# radd ()
    def __radd__(self, value):
        return self.__add__(value)

# iadd (increment, +=)
    def __iadd__(self, value):
        return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
