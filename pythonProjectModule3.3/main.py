# def print_params(a, b, c):
#     print(a, b, c)
#
#
# list = [1, 2]
# dict = {'c': 3}
# print_params(*list, **dict)

def print_params(a=1, b='строка', c=True):
    print(a, b, c)



values_list_2 = [54.32, 'Строка']
values_list = [24, 'Привет', False]
values_dict = {'a': 'Удача', 'b': True, 'c': 36}
print_params(*values_list)
print_params(b=25, c=[1, 2, 3])
print_params(**values_dict)
print_params(*values_list_2, 42)