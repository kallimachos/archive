import sys
source = open(sys.argv[1], 'r').readlines()


def F(n):
    if n > 1:
        result = F(n-1) + F(n-2)
        return result
    elif n == 1:
        return 1
    else:
        return 0

for line in source:
    print(F(int(line)))
