# remove comment on android import to work on QPython

import android#helper as android
import sys
import time
import pickle
import logging
from datetime import date
from os import remove
from os.path import isfile

today = date.today()
app = android.Android()

# --------------------------------------------------------------------------------
# Controller functions

def check():  # Checks for data.p file. If it is missing, runs setup().
    logging.debug('check: checking for data.p')
    if isfile('data.p'):
        logging.debug('check: data.p exists')
        return True
    else:
        logging.debug('check: no data.p')
        status_update('No data file. Running setup.')
        return False

def setup():  # Initialises info{}
        logging.debug('setup: running setup')
        start = fetch_date()
        logging.debug('setup: start == %s', start)
        last_access = today
        logging.debug('setup: last_access == %s', last_access)
        incGoods = float(setInc('goods','yes'))
        incFood = float(setInc('food','yes'))
        dateDiff = today-start
        logging.debug('setup: dateDiff == %s', dateDiff)
        totalDays = dateDiff.days
        logging.debug('setup: totalDays == %s', totalDays)
        totalGoods = incGoods*12/365*totalDays
        totalFood = incFood*12/365*totalDays
        goods = {'totalMoney':totalGoods,'spentMoney':0.00,'funMoney':totalGoods,'increment':incGoods}
        food = {'totalMoney':totalFood,'spentMoney':0.00,'funMoney':totalFood,'increment':incFood}
        info = {'start':start,'last_access':last_access,'goods':goods,'food':food}
        #logging.debug('setup: info == %s', info)
        writeData(info)

def readData():  # reads a dictionary from data.p
    logging.debug('readData: reading data.p')
    try:
        with open('data.p', 'rb') as f:
            info = pickle.load(f)
    except IOError as ioerr:
        logging.error('readData: File error - %s', ioerr)
    return info

def writeData(info):  # writes a dictionary to data.p
    logging.debug('writeData: writing data.p')
    try:
        with open('data.p', 'wb') as f:
            pickle.dump(info, f)
    except IOError as ioerr:
        logging.error('writeData: File error - %s', ioerr)

def clearData():  # removes data.p file
    logging.debug('clearData: removing data.p')
    if isfile('data.p'): remove('data.p')

def setIncrement(info, expense, amount):  # sets the monthly increment
    logging.debug('setIncrement: setting increment')
    info[expense]['increment'] = float(amount)
    logging.debug('setIncrement: increment set to %s', amount)
    writeData(info)

def increment(info):  # Increments total money available based on today's date
    logging.debug('increment: incrementing money available')
    dateDiff = today - info['last_access']
    logging.debug('increment: today == %s', today)
    logging.debug('increment: last_access == %s', info['last_access'])
    logging.debug('increment: dateDiff == %s', dateDiff)
    totalDays = dateDiff.days
    logging.debug('increment: totalDays == %s', totalDays)
    info['last_access'] = today
    logging.debug('increment: updated last_access == %s', info['last_access'])
    for item in ['goods','food']:
        info[item]['totalMoney'] += info[item]['increment']*12/365*totalDays
        info[item]['funMoney'] = info[item]['totalMoney']-info[item]['spentMoney']
    writeData(info)

def adjustMoney(info, expense, amount, kind):  # adds or subtracts money from amount available
    logging.debug('adjustMoney: %s $%s', kind, amount)
    if kind == 'spend':
        info[expense]['spentMoney'] += float(amount)
    else: info[expense]['spentMoney'] -= float(amount)
    info[expense]['funMoney'] = info[expense]['totalMoney'] - info[expense]['spentMoney']
    writeData(info)

# --------------------------------------------------------------------------------
# View functions

def status_update(msg, how_long=2):  # Makes toast with given message
    app.makeToast(msg)
    time.sleep(how_long)

def main_menu():  # Main menu command options dialog
    list_title = 'Command Options:'
    info = readData()
    goodsmoney = "${0:.2f}".format(info['goods']['funMoney'])
    foodmoney = "${0:.2f}".format(info['food']['funMoney'])
    command_options = ['Goods:  ' + goodsmoney,'Food:  ' + foodmoney,'Reset','Quit']
    app.dialogCreateAlert(list_title)
    app.dialogSetItems(command_options)
    app.dialogShow()
    resp = app.dialogGetResponse().result
    if resp is not None:
        option = command_options[resp['item']]
        if option == 'Goods:  ' + goodsmoney:
            sub_menu('goods')
        elif option == 'Food:  ' + foodmoney:
            sub_menu('food')
        elif option == 'Reset':
            reset()
        elif option == 'Quit':
            quit_app()
        else:
            status_update('Invalid option')
            main_menu()

def sub_menu(expense):  # Sub menu command options dialog
    list_title = 'Command Options:'
    info = readData()[expense]
    money = "${0:.2f}".format(info['funMoney'])
    increment = "{0:.0f}".format(info['increment'])
    command_options = ['Available:  ' + money,'Spend','Add','Set Increment: $' + increment,'Main Menu','Quit']
    app.dialogCreateAlert(list_title)
    app.dialogSetItems(command_options)
    app.dialogShow()
    resp = app.dialogGetResponse().result
    if resp is not None:
        option = command_options[resp['item']]
        if option == 'Spend':
            spend(expense)
        elif option == 'Add':
            add(expense)
        elif option == 'Set Increment: $' + increment:
            setInc(expense, 'no')
        elif option == 'Main Menu':
            main_menu()
        elif option == 'Quit':
            quit_app()
        else:
            status_update('Invalid option')
            sub_menu(expense)

def spend(expense):  # Spend money dialog
    title = 'Spend'
    msg = 'Enter the amount you want to spend:'
    resp = fetch_amount(title, msg)

    if resp is not None:
        amount = resp
        adjustMoney(readData(), expense, amount, 'spend')
        status_update('You spent $' + amount)
    sub_menu(expense)

def add(expense):  # Add money dialog
    title = 'Add'
    msg = 'Enter the amount you want to add:'
    resp = fetch_amount(title, msg)

    if resp is not None:
        amount = resp
        adjustMoney(readData(), expense, amount, 'add')
        status_update('You added $' + amount)
    sub_menu(expense)

def setInc(expense, init='no'):  # Set monthly increment dialog
    title = 'Monthly Increment'
    msg = 'Set the monthly ' + expense + ' budget:'
    if init == 'yes':
        inc_default = '100'
        resp = fetch_amount(title, msg, inc_default)

        if resp is not None:
            return resp
    else:
        resp = fetch_amount(title, msg)

        if resp is not None:
            amount = resp
            setIncrement(readData(), expense, amount)
            status_update('You set the monthly amount to $' + amount)
        sub_menu(expense)

def reset():  # Reset data.p dialog
    reset_title = 'WARNING'
    reset_msg = 'Do you want to reset all your data?'
    app.dialogCreateAlert(reset_title, reset_msg)
    app.dialogSetPositiveButtonText('Yes')
    app.dialogSetNegativeButtonText('No')
    app.dialogShow()
    resp = app.dialogGetResponse().result
    if resp is None or resp['which'] != 'positive': main_menu()
    else:
        clearData()
        setup()
        status_update('Setup successful')
        main_menu()

def quit_app():  # Quit app
    sys.exit()

def fetch_date():  # Date picker dialog
    app.dialogCreateDatePicker(today.year, today.month, today.day)
    app.dialogShow()
    resp = app.dialogGetResponse().result
    start = date(resp['year'], resp['month'], resp['day'])
    return start

def fetch_amount(title, msg, default_amount=""):
    app.dialogCreateInput(title, msg, default_amount, "numberDecimal")
    app.dialogSetPositiveButtonText('OK')
    app.dialogSetNegativeButtonText('Cancel')
    app.dialogShow()
    resp = app.dialogGetResponse().result
    if resp.get('which') == 'positive':
        return resp.get('value')

# --------------------------------------------------------------------------------
# Logging

def logconfig():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logging.debug('logconfig: Logging configured')

# --------------------------------------------------------------------------------
# Main function

if __name__ == "__main__":
    logconfig()
    if not check(): setup()
    increment(readData())
    main_menu()