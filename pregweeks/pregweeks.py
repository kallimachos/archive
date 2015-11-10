# Display a pregnancy's current status in weeks, and the number of weeks left.
# Option to enter date and display status at that date.

import datetime
from sys import exit

def week(endDate, name):
	if name == "Julie":
		START = datetime.datetime(2013,7,9).timetuple().tm_yday
		BIRTH = datetime.datetime(2014,4,16).timetuple().tm_yday
	elif name == "Peta":
		START = datetime.datetime(2013,4,8).timetuple().tm_yday
		BIRTH = datetime.datetime(2013,12,26).timetuple().tm_yday
	if endDate < START:
		currentWeek = (endDate-START+365+1)/7
		remainingWeeks = (BIRTH-endDate+1)/7
	else:
		currentWeek = (endDate-START+1)/7
		if name == "Julie": remainingWeeks = (BIRTH+365-endDate+1)/7
		else: remainingWeeks = (BIRTH-endDate+1)/7
	return currentWeek, remainingWeeks

def chooseDate():
	correctDate = False
	while not correctDate:
		year = int(raw_input('Enter the year: '))
		month = int(raw_input('Enter the month: '))
		day = int(raw_input('Enter the day: '))
		try:
			newDate = datetime.datetime(year,month,day)
			correctDate = True
		except ValueError:
			print 'Invalid date!'
	return newDate.timetuple().tm_yday

def viewInfo(currentWeek, remainingWeeks):
	print '''
Weeks past: %i
Weeks left: %i''' % (currentWeek, remainingWeeks)

def commands(name):
	print '''
---------------
Actions for %s:
d:  display current status
s:  select a date
c:  change woman
q:  quit
---------------
''' % name

def chooseWoman():
	print '''
---------------
Select the pregnant woman:
j:  Julie
p:  Peta
q:  quit
---------------
'''
	name = raw_input('Enter selection: ')
	if name == 'q': exit(0)
	elif name == 'j':
		name = 'Julie'
	elif name == 'p':
		name = 'Peta'
	else:
		print 'Invalid entry!'
		chooseWoman()
	action(name)

def action(name):
	commands(name)
	response = raw_input('Enter command: ')
	if response == 'd':
		currentDate = week(datetime.datetime.now().timetuple().tm_yday, name)
		viewInfo(currentDate[0],currentDate[1])
		action(name)
	elif response == 's':
		chosenDate = week(chooseDate(), name)
		viewInfo(chosenDate[0],chosenDate[1])
		action(name)
	elif response == 'c': chooseWoman()
	elif response == 'q': exit(0)
	else:
		print 'Invalid action!'
		action(name)

chooseWoman()