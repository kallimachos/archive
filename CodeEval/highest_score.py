# import sys
# source = open(sys.argv[1], 'r').readlines()
#
# rows = [line.split("|") for line in source]
# for row in rows:
#     entry = []
#     entry = row.strip().split()
#     entry = [int(i) for i in entry]
#     print entry

# x = zip([1,2,3],[4,5,6],[7,8,9])

x = zip([72, 64, 150], [100, 18, 33], [13, 250, -6])
# x = [max(i) for i in x]
# print x

for i in x:
    print(max(i))

#
#     col = []
#     for row in rows:
#         entry = []
#         entry = row.strip().split()
#         entry = [int(i) for i in entry]
#         print entry
#     print allrows
#     allcols = []
#
#     print allcols

    # col.append(entry.pop(0))

    # print col

    # print max(entry)

# The first argument is a path to a file. Each line includes a test case with a
# table. Table rows are separated by pipes '|'.
# All table rows contain scores for each category, so all lines are of an equal
# length.
#
# You need to print the highest score for each category.
#
# Input sample:
#
# 72 64 150 | 100 18 33 | 13 250 -6
# 10 25 -30 44 | 5 16 70 8 | 13 1 31 12
# 100 6 300 20 10 | 5 200 6 9 500 | 1 10 3 400 143
#
# Output sample:
#
# 100 250 150
# 13 25 70 44
# 100 200 300 400 500
#
# Constraints:
#
#     All lines in a test case are of an equal length.
#     The number of participants can be from 2 to 10 people.
#     The number of categories can be from 4 to 20.
#     The number of points for one picture can be from -1000 to 1000.
#     The number of test cases is 40.
