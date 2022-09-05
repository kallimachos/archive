import sys
source = open(sys.argv[1], 'r').readlines()

for line in source:
    if int(line) % 2 == 0:
        print(1)
    else:
        print(0)
