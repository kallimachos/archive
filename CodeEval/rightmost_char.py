import sys
source = open(sys.argv[1], 'r').readlines()

for line in source:
    array = line.strip().split(',')
    if array[0] != '':
        char = array.pop()
        string = ','.join(array)
        print(string.rfind(char))
