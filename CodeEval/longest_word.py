import sys
source = open(sys.argv[1], 'r').readlines()

for line in source:
    line = line.strip().split()
    result = line.pop(0)
    for word in line:
        if len(word) > len(result):
            result = word
    print(result)
