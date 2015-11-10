def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins, secs) = time_string.split(splitter)
	return(mins + '.' + secs)

pathroot = '/home/bmoss/code/python/headfirst/hfpy_code/chapter5/'
files = ['julie.txt','james.txt','sarah.txt','mikey.txt']

for file in files:
	try:
		with open(pathroot + file) as athlete:
			times = athlete.readline().strip().split(',')
			times = sorted(set([sanitize(time) for time in times]))
			print(times[0:3])
	except IOError as err:
		print('File error.' + str(err))