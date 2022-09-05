import sys
lines = open(sys.argv[1], 'r').readlines()

for string in lines:
    result = string.split()[-2]
    print(result)
