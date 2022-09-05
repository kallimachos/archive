# source = open(sys.argv[1], 'r').readlines()
source = open('source.txt', 'r').readlines()

output = ''

for line in source:
    line = line.strip()
    array = []
    updown = 1  # 1 == uppercase
    for letter in line:
        if letter.isalpha():
            if updown == 1:
                array.append(letter.upper())
                updown = 0
            else:
                array.append(letter.lower())
                updown = 1
        else:
            array.append(letter)
    output += ''.join(array) + '\n'

print(output.strip())


def result():
    return output.strip()


# This code works with test.py as an example of testing these simple programs.

# You are given a piece of text. Your job is to write a program that sets the
# case of text characters according to the following rules:
#
#    The first letter of the line should be in uppercase.
#    The next letter should be in lowercase.
#    The next letter should be in uppercase, and so on.
#    Any characters, except for the letters, are ignored during determination
#    of letter case.
#
# The first argument will be a path to a filename containing sentences, one per
# line. You can assume that all characters are from the English language.
#
# Print to stdout the RoLlErCoAsTeR case version of the string.
#
# Constraints:  The length of each piece of text does not exceed 1000
# characters.
#
# Input example:
# To be, or not to be: that is the question.
# Whether 'tis nobler in the mind to suffer.
# The slings and arrows of outrageous fortune.
# Or to take arms against a sea of troubles.
# And by opposing end them, to die: to sleep.
#
# Output example:
# To Be, Or NoT tO bE: tHaT iS tHe QuEsTiOn.
# WhEtHeR 'tIs NoBlEr In ThE mInD tO sUfFeR.
# ThE sLiNgS aNd ArRoWs Of OuTrAgEoUs FoRtUnE.
# Or To TaKe ArMs AgAiNsT a SeA oF tRoUbLeS.
# AnD bY oPpOsInG eNd ThEm, To DiE: tO sLeEp.
