import sys
source = open(sys.argv[1], 'r').readlines()

for line in source:
    line = line.strip()
    if len(line) <= 55:
        print(line)
    else:
        line = line[:40]
        space = line.rfind(' ')
        if space >= 0:
            line = line[:space]
        print(line.strip() + '... <Read More>')
