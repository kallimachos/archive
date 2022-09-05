import sys
source = open(sys.argv[1], 'r').readlines()

for line in source:
    array = line.split()
    result = []
    for word in array:
        result.append(word.replace(word[0], word[0].upper(), 1))
    print(' '.join(result))
