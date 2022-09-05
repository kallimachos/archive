import math


def is_prime(n):
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

n = 3
result = 2
count = 1

while count < 1000:
    if is_prime(n):
        result += n
        count += 1
    n += 2
print(result)
