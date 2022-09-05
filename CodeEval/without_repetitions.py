import sys
source = open(sys.argv[1], 'r').readlines()

for line in source:
    line = line.strip()
    array = []
    for letter in line:
        array.append(letter)
    for x in range(0, len(array)-1):
        while x+1 < len(array) and array[x] == array[x+1]:
            array.pop(x)
    print(''.join(array))
