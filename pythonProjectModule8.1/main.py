# try:
#     truba = a + b
#     truba = 10/0
#
# except ZeroDivisionError:
#     print('нельзя делить на ноль!')

def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float) and (b, (int, float))):
            return a + b
        else:
            return str(a) + str(b)
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))