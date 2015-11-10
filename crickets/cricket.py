#!/bin/python

import argparse
import logging
import requests
import re
from os import system
from time import sleep
from bs4 import BeautifulSoup

HOST = 'http://static.cricinfo.com/rss/livescores.xml'

def score(country):
    r = requests.get(HOST)
    soup = BeautifulSoup(r.text, from_encoding='utf-8')
    match = soup.find("title", text=re.compile(country))
    try:
        link = match.find_next("guid").text
    except AttributeError:
        print 'No ' + country + ' matches currently available.\n'
        quit()
    r = requests.get(link)
    soup = BeautifulSoup(r.text, from_encoding='utf-8')
    requirement = soup.find(class_="innings-requirement")
    print match.text
    print requirement.text.strip()

#----------------------------------------------------------
# main

def main():
    logConfig()
    parser = argparse.ArgumentParser(prog="cricket", description="Command line cricket scores", epilog="Use CTRL+C to quit when using --update option.")
    parser.add_argument('country', type=str, nargs='?', default='Australia', help='Select country to display. Default: Australia')
    parser.add_argument('-u', '--update', action='store_true', default=False, help='Update score at 1 minute intervals')
    args = parser.parse_args()
    if args.update:
        try:
            while True:
                system('clear')
                score(args.country)
                sleep(30)
        except KeyboardInterrupt:
            print ' Quit'
    else:
        print
        score(args.country)
        print

#===========================================================
# Logging Configuration

def logConfig():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='/home/bmoss/code/python/cricket/output.log',
                        filemode='w')

#===========================================================

if __name__ == '__main__':
	main()