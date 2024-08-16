# class _Human:
#     head = True
#     _legs = True
#     __arms = True
#
#     def say_hello(self):
#         print('Здравствуйте')
#
#     def about(self):
#         print(self.head)
#         print(self._legs)
#         print(self.__arms)
#
# class Student(_Human):
#     pass
#     # def about(self):
#     #     print('Я студент')

# class Teacher(_Human):
#     pass
#
#
# human = _Human()
# human.about()
#
# student = Student()
# student.about()
#
# print(dir(human))
# print(dir(student._Human__arms))



class Vehicle:

    __COLOR_VARIANTS = ['black', 'green', 'red', 'blue']

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.__color = color
        self.__engine_power = engine_power
        self.__model = model
        self.owner = owner
    def get_model(self):
        return f"Модель: {self.__model}"
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        if new_color.upper() in (color.upper() for color in self.__COLOR_VARIANTS):
            self.__color = new_color
            print(f'Цвет: {self.__color}')
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()