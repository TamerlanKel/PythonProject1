# while 1 > 0:
#     number = int(input("Введите число: "))
#     if number % 2 == 0:
#         print("Число четное")
#         continue
#     else:
#         print("Число нечетное")
#     print("Меня не забыли")
# a = 5

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_list = []

i = 0
while i < len(my_list):
    if my_list[i] < 0:
        break
    elif my_list[i] > 0:
        positive_list.append(my_list[i])
    i += 1

print(positive_list)
