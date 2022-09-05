import sys
source = open(sys.argv[1], 'r').readlines()

for line in source:
    array = line.strip().split(',')
    result = []
    for n in array:
        if result.count(n) < 1:
            result.append(n)
    print(','.join(result))
