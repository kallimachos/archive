import sys
source = open(sys.argv[1], 'r').readlines()


def lowest(array):
    result = []
    for x in array:
        if array.count(x) == 1:
            result.append(x)
    result.sort()
    try:
        return result[0]
    except IndexError:
        return 0

for line in source:
    array = line.strip().split()
    x = lowest(array)
    if x == 0:
        print(0)
    else:
        print(array.index(x) + 1)
