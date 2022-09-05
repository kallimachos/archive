import sys
source = open(sys.argv[1], 'r').readlines()

digits = []
for line in source:
    digits.append(int(line))
print(sum(digits))
