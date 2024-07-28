# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}')
#
# """
# 1x1
# 1x2
# 1x3
#
# """
#
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# for i, k in dict_.items():
#     print(i, k)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in (numbers):
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)


print("Primes: ", primes)
print("Not Primes: ", not_primes)
