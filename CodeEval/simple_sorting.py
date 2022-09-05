import sys
source = open(sys.argv[1], 'r').readlines()

for line in source:
    array = []
    for number in line.strip().split():
        array.append(float(number))
    array.sort()
    string = ''
    for number in array:
        string += '%.3f ' % number
    print(string)
