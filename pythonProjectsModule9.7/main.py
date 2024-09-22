def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(3, int(result ** 0.5) + 1):
            if result % i != 0 and result > 1:
                print('Простое')
            else:
                print('Составное')
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)