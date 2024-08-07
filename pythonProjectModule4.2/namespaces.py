from module1 import d

d = 7
def square(x):

    d = x ** 2
    def even(x):
        nonlocal d
        d = x / 2
        if d % 2 == 0:
            print('Четное')
        else:
            print('Нечетное')
    even(x)
    return d


a = 5
b = square(4)
print(a)
print(b)
# print(globals())



