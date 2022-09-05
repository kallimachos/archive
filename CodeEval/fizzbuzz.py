import sys
numbers = open(sys.argv[1], 'r').readlines()


def fizzbuzz(a, b, l):
    result = []
    for x in range(1, int(l)+1):
        if x % int(a) == 0 and x % int(b) == 0:
            num = 'FB'
        elif x % int(a) == 0:
            num = 'F'
        elif x % int(b) == 0:
            num = 'B'
        else:
            num = str(x)
        result.append(num + ' ')
    return result

for line in numbers:
    line = line.split()
    print(''.join(fizzbuzz(line[0], line[1], line[2])).strip())
