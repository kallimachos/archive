import sys
source = open(sys.argv[1], 'r').readlines()

for line in source:
    line = line.strip()
    result = ''
    for char in line:
        if char.isupper():
            char = char.lower()
        else:
            char = char.upper()
        result += char
    print(result)
