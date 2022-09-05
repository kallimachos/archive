import sys
strings = open(sys.argv[1], 'r').readlines()

for line in strings:
    if line != '\n':
        temp = line.strip().split()
        test = []
        for word in reversed(temp):
            test.append(word)
        result = ' '.join(test)
        print(result)
