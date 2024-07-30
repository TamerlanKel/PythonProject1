# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n-1)
#
#
# print(summa(5))

# stack = []
# stack.append(1)
# print('Добавили элемент', stack)
# stack.append(2)
# print('Добавили элемент', stack)
# stack.append(3)
# print('Добавили элемент', stack)
# print(stack)
# stack.pop()
# print("Убрали элемент", stack)
# stack.pop()
# print("Убрали элемент", stack)
# stack.pop()
# print("Убрали элемент", stack)

# def recursion():
#     recursion()
#
# recursion()

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)