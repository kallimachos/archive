#!/bin/python3

# tkinter version of budget.py
# To do:
# 1. Refactor as per andbudget.py
# 2. Add exceptions handling (try, except, finally)
# 3. Use pickle for storing data?

import datetime
import tkinter
from tkinter import messagebox
from tkinter import simpledialog
from ast import literal_eval
from os import remove
from os.path import isfile


class root(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):   # build the main window
        self.grid()

        # Text box for entering dollars
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=0, sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter amount here")

        # buttons
        button = tkinter.Button(self, text=u"Add", command=self.OnButtonAdd)
        button.grid(column=2, row=0, sticky='EW')
        button = tkinter.Button(self, text=u"Spend",
                                command=self.OnButtonSpend)
        button.grid(column=3, row=0, sticky='EW')
        button = tkinter.Button(self, text=u"Setup",
                                command=self.OnButtonSetup)
        button.grid(column=2, row=1, sticky='EW')
        button = tkinter.Button(self, text=u"Increment",
                                command=self.OnButtonIncrement)
        button.grid(column=3, row=1, sticky='EW')
        button = tkinter.Button(self, text=u"Clear Data",
                                command=self.OnButtonClear)
        button.grid(column=2, row=2, sticky='EW')
        button = tkinter.Button(self, text=u"Quit", command=self.OnButtonQuit)
        button.grid(column=3, row=2, sticky='EW')

        # Label to display operation messages
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable=self.labelVariable,
                              anchor="w", fg="white", bg="blue")
        label.grid(column=0, row=1, columnspan=2, sticky='EW')
        self.labelVariable.set("Welcome")

        # Label to display running total
        self.amount = tkinter.StringVar()
        label2 = tkinter.Label(self, textvariable=self.amount)
        label2.grid(column=0, row=2, columnspan=2, sticky='EW')
        if isfile('data.txt'):
            increment(readData())
            self.amount.set("Available:  ${0:.2f}".format(readData()
                                                          ['funMoney']))
        else:
            self.amount.set("Run Setup")

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnButtonAdd(self):   # Add money to the total
        amount = self.entryVariable.get()
        if check():
            if adjustMoney(readData(), amount, 1):
                self.labelVariable.set("You added:  $" + amount)
            else:
                messagebox.showwarning("Bad input", "Invalid amount!")
                self.labelVariable.set("You added:  $0")
            self.amount.set("Available:  ${0:.2f}".format(readData()
                                                          ['funMoney']))
        else:
            self.labelVariable.set("No data available")
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnButtonSpend(self):   # Spend money from the total
        amount = self.entryVariable.get()
        if check():
            if adjustMoney(readData(), amount, 0):
                self.labelVariable.set("You spent:  $" + amount)
            else:
                messagebox.showwarning("Bad input", "Invalid amount!")
                self.labelVariable.set("You spent:  $0")
            self.amount.set("Available:  ${0:.2f}".format(readData()
                                                          ['funMoney']))
        else:
            self.labelVariable.set("No data available")
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnButtonSetup(self):   # Run Setup()
        setup()
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnButtonIncrement(self):   # Run SetIncrement()
        amount = self.entryVariable.get()
        if check():
            if SetIncrement(readData(), amount):
                self.labelVariable.set("${0:.2f}".format(float(amount)) +
                                       "/m = ${0:.2f}".format(readData()
                                                              ['increment'])
                                       + "/d")
            else:
                messagebox.showwarning("Bad input", "Invalid amount!")
                self.labelVariable.set("Error")
            self.amount.set("Available:  ${0:.2f}".format(readData()
                                                          ['funMoney']))
        else:
            self.labelVariable.set("No data available")
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnButtonClear(self):   # Delete the data.txt file
        clearData()
        self.labelVariable.set("Data cleared.")
        self.amount.set("Run Setup")
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnButtonQuit(self):   # Close the program
        self.destroy()

    def OnPressEnter(self, event):   # Does nothing
        self.labelVariable.set("ENTER does nothing")
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)


class MyDialog(simpledialog.Dialog):   # Dialog box for setting start date
    def body(self, master):
        e1 = tkinter.Label(master, text="Day:").grid(row=0)
        e2 = tkinter.Label(master, text="Month:").grid(row=1)
        e3 = tkinter.Label(master, text="Year:").grid(row=2)
        self.e1 = tkinter.Entry(master)
        self.e2 = tkinter.Entry(master)
        self.e3 = tkinter.Entry(master)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        return self.e1  # initial focus

    def apply(self):
        self.startday = self.e1.get()
        self.startmonth = self.e2.get()
        self.startyear = self.e3.get()


def check():  # Checks for data.txt and runs setup() if it is missing
    if isfile('data.txt'):
        app.amount.set("Available:  ${0:.2f}".format(readData()['funMoney']))
        return True
    else:
        app.amount.set("Run Setup")
        return False


def setup():  # Sets start date based on user input
    d = MyDialog(app)
    try:
        newDate = datetime.datetime(int(d.startyear), int(d.startmonth),
                                    int(d.startday))
        test = True
    except AttributeError:
        test = False
    except (ValueError, TypeError):
        messagebox.showwarning("Bad input", "Invalid date!")
        app.labelVariable.set("Setup Failed")
        test = False
    if test:
        start = [int(d.startday), int(d.startmonth), int(d.startyear)]
        increment = 1200.00/365.00
        startDate = datetime.date(start[2], start[1], start[0])
        today = datetime.date.today()
        dateDiff = today-startDate
        totalDays = int(dateDiff.days)
        today = str(today)
        totalMoney = increment*totalDays
        spentMoney = 0.00
        funMoney = totalMoney-spentMoney
        info = {'start': start, 'today': today, 'totalDays': totalDays,
                'totalMoney': totalMoney, 'spentMoney': spentMoney,
                'funMoney': funMoney, 'increment': increment}
        writeData(info)
        app.labelVariable.set("Setup Successful")
        app.amount.set("Available:  ${0:.2f}".format(readData()['funMoney']))


def readData():  # opens data.txt and reads it to an array
    f = open('data.txt', 'r')
    info = literal_eval(f.read())
    f.close()
    return info


def writeData(info):  # opens data.txt and writes to it
    f = open('data.txt', 'w+')
    f.write(str(info))
    f.close()


def clearData():  # removes data.txt file
    if isfile('data.txt'):
        remove('data.txt')


def SetIncrement(info, amount):  # sets the monthly increment
    try:
        isinstance(float(amount), float)
    except ValueError:
        return False
    info['increment'] = float(amount)*12/365
    writeData(info)
    return True


def increment(info):  # Increments total money available based on today's date
    if info['today'] != str(datetime.date.today()):
        info['today'] = str(datetime.date.today())
        dateDiff = datetime.date.today() - datetime.date(info['start'][2],
                                                         info['start'][1],
                                                         info['start'][0])
        info['totalDays'] = int(dateDiff.days)
        info['totalMoney'] = info['increment']*info['totalDays']
        info['funMoney'] = info['totalMoney']-info['spentMoney']
        writeData(info)


def adjustMoney(info, amount, kind):
    # adds or subtracts money from amount available
    try:
        isinstance(float(amount), float)
    except ValueError:
        return False
    if kind == 0:
        info['spentMoney'] += float(amount)
    else:
        info['spentMoney'] -= float(amount)
    info['funMoney'] = info['totalMoney'] - info['spentMoney']
    writeData(info)
    return True

if __name__ == "__main__":
    app = root(None)                # creates GUI window and widgets
    app.title('Budget App')         # sets the window title
    app.mainloop()                  # GUI action loop
