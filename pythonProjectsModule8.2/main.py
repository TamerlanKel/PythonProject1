# def f1(number):
#     return 10/number
#
#
# def f2():
#     print('Какой хороший день')
#     result_f1 = f1(0)
#     return result_f1
# try:
#     total = f2()
#     print(total)
# except ZeroDivisionError as exc:
#     print(f'вот что пошло не так - {exc}, но мы не устояли')


# def personal_sum(numbers):
#     result = 0
#     incorrect_data = 0
#     for item in numbers:
#         try:
#             result += item
#         except TypeError:
#             print(f'Некорректный тип данных для подсчета суммы - {item}')
#             incorrect_data += 1
#     return result, incorrect_data
#
# def calculate_average(numbers):
#     if not isinstance(numbers, (list, tuple)):
#         print('В numbers записан некорректный тип данных')
#         return None
#     total_sum, incorrect_count = personal_sum(numbers)
#     try:
#         average = total_sum / (len(numbers) - incorrect_count)
#     except ZeroDivisionError:
#         return 0
#     return average
#
# print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
# print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
# print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
# print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать


def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        total_sum, incorrect_count = personal_sum(numbers)
        count_valid_numbers = len(numbers) - incorrect_count
        if count_valid_numbers == 0:
            return 0
        average = total_sum / count_valid_numbers
    except ZeroDivisionError:
        return 0
    except TypeError:
        if not isinstance(numbers, (list, tuple)):
            print('В numbers записан некорректный тип данных')
            return None
    return average


# Примеры вызова функции
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
