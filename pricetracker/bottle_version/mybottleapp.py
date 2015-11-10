#This app grabs the prices from Wiggle.com.au, compares the savings with the historical best, and serves the information to a web page.

import requests
import pickle
from bottle import route, static_file, template, error, run
from bs4 import BeautifulSoup
from os.path import isfile

# -------------------------------------------------------------------------------------
# Website routes

@route('/')
def index():
    return template('home')

# route for static files
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

# example route using a template
@route('/hello/<name>')
def index(name):
    return template('hello_name', name=name)

# display prices for products
@route('/prices')
def index():
    return template('price_display', inputlist=productlist())

# css test template
@route('/css')
def index():
    return template('css')

# route for printing data path
@route('/data')
def index():
    return template('data', data=datafile)

# route for printing debug information
@route('/debug')
def index():
    return template('debug', output=debug())

# 404 message
@error(404)
def error404(error):
    return template('404')

# 500 message
@error(500)
def error500(error):
    return template('500', output=logs())

# -------------------------------------------------------------------------------------
# Website scraping logic

datafile = '/home/bmoss/code/python/pricetracker/bottle_version/data.p'
root = ('http://www.wiggle.com.au/')
products = ['dhb-aeron-pro-cycling-short',
            'shimano-105-5700-10-speed-cassette',
            'continental-gatorskin-folding-road-tyre',
            'continental-4000s-ii-folding-road-tyre',
            'continental-grand-prix-4000s-ii-folding-road-tyre-twin-pack']

class Product():
    def __init__(self, item):
        r = requests.get(root+item)
        soup = BeautifulSoup(r.text, from_encoding='utf-8')
        product = soup.title.string.split('|')[1].strip()
        list_price = soup.find(class_="was-price").string.strip().split()[2]
        saving = soup.find(class_="saving").string.strip()
        unit_price = soup.find(class_="unit-price").string.strip()

        self.product_name = product
        self.list_price = float(list_price.strip("$"))
        self.saving = saving
        self.unit_price = float(unit_price.strip("$"))
        self.best_price = self.history()
        self.best_diff = self.list_price - self.best_price
        self.best_percent = self.best_diff / self.list_price * 100.00

    def history(self): # adds or updates a product in data.p and returns the best price
        if not isfile(datafile):
            setup()
        info = readData()
        if self.product_name in info and info[self.product_name] <= self.unit_price:
            pass
        else:
            new = {self.product_name:self.unit_price}
            info.update(new)
            writeData(info)
        return info[self.product_name]

    def returnProduct(self): # return product info as an array
        best_price = format(self.best_price, '.2f')
        best_percent = format(self.best_percent, '.0f')
        best_diff = format(self.best_diff, '.2f')
        specs = [self.product_name, self.list_price, self.unit_price, self.saving, best_price,
                  best_percent, best_diff]
        return specs

def setup():  # Initialises info{}
        print "No data file, performing setup."
        product = "test product"
        entry = 0.00
        info = {product:entry}
        writeData(info)

def readData():  # reads a dictionary from data.p
    try:
        with open(datafile, 'rb') as f:
            info = pickle.load(f)
        return info
    except IOError as ioerr:
        print('File error (readData): ' + str(ioerr))

def writeData(info):  # writes a dictionary to data.p
    try:
        with open(datafile, 'wb') as f:
            pickle.dump(info, f)
    except IOError as ioerr:
        print('File error (writeData): ' + str(ioerr))

def productlist():
    result = []
    for item in products:
        product = Product(item)
        result.append(product.returnProduct())
    return result

def readLog(filename):  # return contents of a log file
    try:
        with open(filename, 'rb') as f:
            text = f.read().split('\n')[-20:]
        return text
    except IOError as ioerr:
        return('File error (readData): ' + str(ioerr))

def debug():  # method for debugging
    r = requests.get(root+products[0])
    soup = BeautifulSoup(r.text, from_encoding='utf-8')
    return soup
    #return 'No errors means no debugging!'

def logs():  # prints logs
    pylog = readLog('example.log')
    return pylog

# -------------------------------------------------------------------------------------

run(host='localhost', port=8080, reloader=True)
#run(host='10.64.32.56', port=8080, reloader=True)