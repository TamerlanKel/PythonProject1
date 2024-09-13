# def adder(args):
#     res = 0
#     for number in args:
#         res += number
#     return res
#
# def multiplier(args):
#     res = 1
#     for number in args:
#         res *= number
#     return res
#
# def process_numbers(numbers, function):
#     result = function(numbers)
#     print(f'Получилось {result}')
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# process_numbers(numbers=my_numbers, function=adder)
# process_numbers(numbers=my_numbers, function=multiplier)


# def is_odd(x):
#     return x % 2
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = filter(is_odd, my_numbers)
# print(result)
# print(list(result))


def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:
        func_name = func.__name__
        results[func_name] = func(int_list)
    return results

print(apply_all_func([6, 20, 15, 9],  max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))