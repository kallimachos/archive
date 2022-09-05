import sys
numbers = open(sys.argv[1], 'r').readlines()

for line in numbers:
    digits = line.strip().split(',')
    x = int(digits[0])
    n = int(digits[1])
    multiple = 2
    result = n
    while result < x:
        result = n * multiple
        multiple += 1
    print(result)
