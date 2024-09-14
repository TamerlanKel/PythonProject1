# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = (x ** 100 for x in my_numbers)
# print(result)
#
#
# for elem in result:
#     print(elem)
#
# print('Eshe razok')
#
# for elem in result:
#     print(elem)


first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
combined = first + second
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(first_result))
print(list(second_result))