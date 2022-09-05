import sys
source = open(sys.argv[1], 'r').readlines()


def replace(n):
    result = 0
    for i in str(n):
        result += int(i)**2
    return result


def is_happy(n):
    result = []
    n = int(n)
    while n != 1:
        if result.count(n) == 1:
            return False
        else:
            result.append(n)
            n = replace(n)
    return True

for line in source:
    if is_happy(line):
        print(1)
    else:
        print(0)
