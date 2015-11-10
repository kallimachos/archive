#! /usr/bin/python

#This app grabs the prices from Wiggle.com.au, compares the savings with the historical best, and prints the information to the command line.

import requests
import pickle
import logging
from bs4 import BeautifulSoup
from os.path import isfile
from sys import exit

datafile = '/home/bmoss/code/python/pricetracker/data.p'
dump = '/home/bmoss/code/python/pricetracker/dump.html'
root = ('http://www.wiggle.com.au/')
products = [#'dhb-aeron-pro-cycling-short',
            #'shimano-105-5700-10-speed-cassette',
            'shimano-ultegra-6701-10-speed-chain-116-links',
            'pro-lite-bracciano-a42-alloy-clincher-wheelset',
            'continental-gatorskin-folding-road-tyre',
            'continental-4000s-ii-folding-road-tyre',
            'continental-grand-prix-4000s-ii-folding-road-tyre-twin-pack']

class Product():
    def __init__(self, item):
        r = requests.get(root+item)
        soup = BeautifulSoup(r.text, from_encoding='utf-8')
        product = soup.title.string.split('|')[1].strip()

        try:
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
        except Exception as e:
            logging.error(e)
            logging.debug("list_price == %s", list_price)
            logging.debug("saving == %s", saving)
            logging.debug("unit_price == %s", unit_price)
            try:
                with open(dump, 'wb') as f:
                    f.write(str(soup))
            except Exception as err:
                logging.debug('File error: %s', str(err))
            logging.debug("HTML dumped to %s", dump)
            exit()

    def history(self): # adds or updates a product in data.p and returns the best price
        info = readData()
        if self.product_name in info and info[self.product_name] <= self.unit_price:
            pass
        else:
            new = {self.product_name:self.unit_price}
            info.update(new)
            writeData(info)
        return info[self.product_name]

    def printproduct(self): # print the product name and price info
        print '''
%s
RRP:   $%.2f
Price: $%.2f (%s)
Best:  $%.2f (SAVE %.0f%% = $%.2f)''' % (self.product_name,self.list_price,self.unit_price,self.saving,
                                          self.best_price,self.best_percent,self.best_diff)

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
    except IOError as ioerr:
        print('File error (readData): ' + str(ioerr))
    return info

def writeData(info):  # writes a dictionary to data.p
    try:
        with open(datafile, 'wb') as f:
            pickle.dump(info, f)
    except IOError as ioerr:
        print('File error (writeData): ' + str(ioerr))

def main():
    for item in products:
        product = Product(item)
        product.printproduct()
    print ""

#-----------------------------------------------------------
# Configure logging

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
                    #filename='debug.log',
                    #filemode='w')

#-----------------------------------------------------------

if __name__ == '__main__':
    if not isfile(datafile):
        setup()
    main()