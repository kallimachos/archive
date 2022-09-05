import sys
source = open(sys.argv[1], 'r').readlines()

for line in source:
    line = line.strip().lower()
    print(line)
