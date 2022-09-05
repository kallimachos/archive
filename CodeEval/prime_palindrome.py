import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def is_palindrome(n):
    front = []
    back = []
    for digit in str(n):
        front.append(digit)
    for digit in reversed(front):
        back.append(digit)
    if front == back:
        return True
    else:
        return False

for x in range(1000, 1, -1):
    if is_prime(x) and is_palindrome(x):
        print(x)
        break
