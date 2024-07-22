# name = input('Введите ваше имя: ')
# if name == "Urban":
#     print("Здравствуйте, администратор")
# if name == "Tamerlan":
#     print("Здравствуйте, студент")
# else:
#     print("Привет", name)
# number = int(input("Введите число: ")) # Fizz, Buzz, FizzBuzz
# if number % 3 == 0 and number % 5 == 0:
#     print('FizzBuzz')
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# else:
#     print('Число не подходит')
first = int(input("Введите ваше 1 число: "))
second = int(input("Введите ваше 2 число: "))
third = int(input("Введите ваше 3 число: "))
if first and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)