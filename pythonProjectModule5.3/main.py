# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_info(self):
#         print(f'Привет меня зовут {self.name}, мне {self.age}')
#
#     def birthday(self):
#         self.age += 1
#         print(f'У меня день рождения, мне теперь {self.age}')
#
#     def __del__(self):
#         print(f'{self.name} ушел')
#
#     def __len__(self):
#         return self.age
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#     def __gt__(self, other):
#         return self.age > other.age
#
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age
#
#     def __bool__(self):
#         return bool(self.age)
#
#     def __str__(self):
#         return f'{self.name}'

# den = Human('Денис', 22)
# max = Human('Макс', 22)
# a = 6
# print(max)


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        
    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)




h1 = House('ЖК Эльбруc', 10)
h2 = House(' ЖК Акация', 20)

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