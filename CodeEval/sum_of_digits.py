import sys
numbers = open(sys.argv[1], 'r').readlines()


def sumdigits(num):
    result = 0
    for digit in str(num):
        result += int(digit)
    return result

for line in numbers:
    print(sumdigits(line.strip()))
