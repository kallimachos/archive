#FizzBuzz test
# Write a program that prints the numbers from 1 to 100. But for multiples of three print Fizz instead of the number and for the multiples of five print Buzz. For numbers which are multiples of both three and five print FizzBuzz.
#
#import time
#
#fizz = 3
#buzz = 5
#total = 100
#
#for x in range(1,total+1):
#    if x % (fizz * buzz) == 0:
#        print 'FizzBuzz'
#    elif x % fizz == 0:
#        print 'Fizz'
#    elif x % buzz == 0:
#        print 'Buzz'
#    else: print x
#    time.sleep(.2)
#
#-------------------------------------------------------------------------------
#Challenge 2 - translate strings

#import string
#
#puzzle = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#url = 'www.pythonchallenge.com/pc/def/map.html'
#
#table = string.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
#        "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB")
#print puzzle.translate(table)
#print url.translate(table)

#-------------------------------------------------------------------------------
#Challenge 6 - zip files

#import time
#import requests

#r = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')
#text = r.content

#nothing = '90052'
#comments = ''
#
#for x in range(909):
#    source = 'zips/' + nothing + '.txt'
#    f = open(source,'r')
#    info = f.read()
#    f.close()
#    print info
#    time.sleep(.001)
#    nothing = ''
#    for char in info:
#        if char.isdigit():
#            nothing += char
#print comments
#
#import zipfile
#
#zipper = zipfile.ZipFile(open('zips/channel.zip','r'))
#
#nothing = '90052'
#comments = [] #The answer is *in* the zip..
#for x in range(908):
#    raw_data = zipper.read(nothing+'.txt')
#    print raw_data
#    nothing = raw_data.split()[-1]
#    comments.append(zipper.getinfo(nothing+'.txt').comment)
#print "".join(comments)

#-------------------------------------------------------------------------------
#Challenge 7 - Image processing
#
#import Image
#import StringIO
#import requests
#
#r = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png')
#picture = Image.open(StringIO.StringIO(r.content))
#w,h = picture.size
#
#clue = ''
#for x in range(0,w,7):
#    char = picture.getpixel((x,h/2))
#    clue += chr(char[0])
#print clue
#
#answer = ''
#nums = [105, 110, 116, 101, 103, 114, 105, 116, 121]
#for x in nums:
#    answer += chr(x)
#print answer
#
#-------------------------------------------------------------------------------
#Challenge 8
