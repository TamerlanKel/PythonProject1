# int() --> int(input())
# float()
# bool()
# str()
# list()
# tuple()
# dict()
# set()
# salary = [2300, 1800, 5000, 1234.583434, 7500.122323]
# print(round(sum(salary)/len(salary), 2))
# print(round(max(salary), 2))
# print(round(min(salary), 2))
# names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
# zipped = dict(zip(names, salary))
# print(zipped['Денис'], '- зарплата Дениса')


# a = [1, 1, 1]
# b = '0'
# d = [1, 1, 1]
# c = d
# print(id(a))
# print(id(d))
# print(id(c))
# print(id(2))
# print(id(2))
# print(c is d)
# print(help(a))
# def helper():
#     """
#     Эта функция помощник
#     """
#     pass
# print(helper.__doc__)


# def find_max(list):
#     max = list[0]
#     for i in list:
#         if i > max:
#             max = i
#     return max
#
# print(find_max([1, 2, 1, 5]))


# def count_even(list):
#     counter = 0
#     for i in list:
#         if i % 2 == 0:
#             counter += 1
#         if counter == 0:
#             continue
#     return counter
# print(count_even([2, 2, 3, 4, 2, 1]))


# def unique(list):
#     new_list = []
#     for i in list:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
# print(unique([1, 2, 3, 4, 5, 6, 7, 8]))

# import tkinter as tk
#
# def get_values():
#     num1 = int(number1_entry.get())
#     num2 = int(number2_entry.get())
#     return num1, num2
#
#
#
# def insert_values(value):
#     answer_entry.delete(0, 'end')
#     answer_entry.insert(0, value)
#
#
#
# def add():
#     num1, num2 = get_values()
#     res = num1 + num2
#     insert_values(res)
#
#
# def sub():
#     num1, num2 = get_values()
#     res = num1 - num2
#     insert_values(res)
#
# def div():
#     num1, num2 = get_values()
#     res = num1 / num2
#     insert_values(res)
#
#
# def mul():
#     num1, num2 = get_values()
#     res = num1 * num2
#     insert_values(res)
#
#
# window = tk.Tk()
# window.title('Калькулятор')
# window.geometry("350x350")
# window.resizable(False, False)
# button_add = tk.Button(window, text="+", width=2, height=2, command=add)
# button_add.place(x=100, y=200)
# button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)
# button_sub.place(x=150, y=200)
# button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)
# button_mul.place(x=200, y=200)
# button_div = tk.Button(window, text="/",width=2, height=2, command=div)
# button_div.place(x=250, y=200)
# number1_entry = tk.Entry(window, width=28)
# number1_entry.place(x=100, y=75)
# number2_entry = tk.Entry(window, width=28)
# number2_entry.place(x=100, y=150)
# answer_entry = tk.Entry(window, width=28)
# answer_entry.place(x=100, y=300)
# number1 = tk.Label(window, text="Введите первое число:")
# number1.place(x=100, y=50)
# number2 = tk.Label(window, text="Введите второе число:")
# number2.place(x=100, y=125)
# answer = tk.Label(window, text="Ответ:")
# answer.place(x=100, y=275)
# window.mainloop()

def calculate_structure_sum(data):
    total_sum = 0
    if isinstance(data, int):
        return data
    elif isinstance(data, str):
        return len(data)
    elif isinstance(data,(list, tuple, set)):
        for item in data:
            total_sum += calculate_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)

    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


