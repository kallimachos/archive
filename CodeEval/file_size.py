from sys import argv

source = open(argv[1], 'r').readlines()

size = []
for line in source:
    for char in line:
        size.append(char)
print(len(size))
