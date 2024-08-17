# class Human:
#     def __init__(self, name, group):
#         self.name = name
#         super().__init__(group)
#         super().about
#     def info(self):
#         print(f'Привет меня зовут {self.name}')
#
#
# class StudentGroup:
#     def __init__(self, group):
#         self.group = group
#
#     def about(self):
#         print(f'{self.name} учится в группе {self.group}')
# class Student(Human, StudentGroup):
#     def __init__(self, name, place, group):
#         super().__init__(name, group)
#         self.place = place
#         super().info()
#
# # human = Human('Тамерлан')
# # print(human.name)
# student = Student('Макс', 'Urban', 'Питон 1')
# student.about()
# print(Student.mro())



class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

