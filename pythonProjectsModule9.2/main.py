# def by_3(x):
#     return x * 3
#
# def is_odd(x):
#     return x % 2

# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = [x * 3 if x > 2 else x * 10 for x in my_numbers]
# print(list(result))

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
combined_strings = first_strings + second_strings
first_result = [len(x) for x in first_strings if len(x) >= 5]
second_result = [tuple((x, y)) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {x: len(x) for x in combined_strings if len(x) % 2 == 0}
print(first_result)
print(second_result)
print(third_result)