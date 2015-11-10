# Store the date and the current amount in a data file.  When the app runs, it adds the value accrued since the last run of the app to the total amount and displays the total amount.  Provide a button to subtract an amount from the running total.  Use kivy to build it for android.

import datetime
from ast import literal_eval
from os.path import isfile

INCREMENT = 1200.00/365.00

def setup(direction):
#	startyear = 2013
#	startmonth = 9
#	startday = 1
	correctDate = False
	while not correctDate:
		startyear = int(raw_input('...\nEnter the start year: '))
		startmonth = int(raw_input('Enter the start month: '))
		startday = int(raw_input('Enter the start day: '))
		print 'Setup complete.'
		try:
			newDate = datetime.datetime(startyear,startmonth,startday)
			correctDate = True
		except ValueError:
			print 'Invalid date!'

	start = datetime.date(startyear,startmonth,startday).timetuple().tm_yday
	today = datetime.datetime.now().timetuple().tm_yday
	yearMultiple = 365*(datetime.date.today().year-startyear)
	totalDays = today-start+yearMultiple+1
	totalMoney = INCREMENT*totalDays
	spentMoney = 0.00
	funMoney = totalMoney-spentMoney
	info = {'start':start,'today':today,'yearMultiple':yearMultiple,'totalDays':totalDays,'totalMoney':totalMoney,'spentMoney':spentMoney,'funMoney':funMoney}
	writeData(info)
	if direction == 1:
		action(readData())

def check():
	if not isfile('data.txt'):
		print 'No data file, performing setup.'
		setup(0)

def increment(info):
	if info['today'] != datetime.datetime.now().timetuple().tm_yday:
		info['today'] = datetime.datetime.now().timetuple().tm_yday
		info['totalDays'] = info['today']-info['start']+info['yearMultiple']+1
		info['totalMoney'] = INCREMENT*info['totalDays']
		writeData(info)

def readData():
	f = open('data.txt','r')
	info = literal_eval(f.read())
	f.close()
	return info

def writeData(info):
	f = open('data.txt','w+')
	f.write(str(info))
	f.close()

def adjustMoney(info, kind):
	dollars = False
	while not dollars:
		amount = raw_input('Amount: ')
		try:
			isinstance(float(amount), float)
			dollars = True
		except ValueError:
			print 'Invalid amount!\n'
	if kind == 0: info['spentMoney'] += float(amount)
	else: info['spentMoney'] -= float(amount)
	info['funMoney'] = info['totalMoney'] - info['spentMoney']
	writeData(info)
	action(readData())

def viewInfo(info):
	print '''
Total money: $%.2f
Spent money: $%.2f
Available:   $%.2f''' % (info['totalMoney'],info['spentMoney'],info['funMoney'])
	action(readData())

def commands(info):
	print '''
---------------
Actions:
a:  add money
s:  spend money
v:  view info
r:  run setup
q:  quit
---------------
Money available: $%.2f''' % info['funMoney']

def action(info):
	commands(info)
	response = raw_input('\nEnter command: ')
	if response == 'r':
		answer = raw_input('WARNING: this deletes all your data! Continue? (y/n) ')
		if answer == 'y': setup(1)
		else: action(readData())
	elif response == 's': adjustMoney(info, 0)
	elif response == 'a': adjustMoney(info, 1)
	elif response == 'v': viewInfo(info)
	elif response == 'q': pass
	else:
		print 'Invalid action!'
		action(readData())

check()
increment(readData())
action(readData())
