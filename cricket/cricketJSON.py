#!/bin/python

import argparse
import logging
import requests
import json

HOST = 'http://cricscore-api.appspot.com/csa'

def getMatch(ID):  # return list of matches or return current score if a match ID is specified
    if ID > 0:
        url = HOST + '?id=' + str(ID)
    else: url = HOST
    try:
        r = requests.get(url)
        logging.debug('Content of request: ' + r.text)
    except Exception as e:
        logging.error(e)
        response = raw_input('\nWebsite error\nRetry? (y/n): ')
        if response == 'y': main()
        else: exit(0)
    data = json.loads(r.text)
    if ID > 0:
        result = '\n' + data[0]["si"] + '\n' + data[0]["de"] + '\n'
    else:
        result = '\n'
        num = 1
        for line in data:
            line['num'] = num
            match = str(line["num"]) + '   ' + str(line["id"]) + ': ' + line["t1"] + ' vs ' + line["t2"]
            result = result + match + '\n'
            num += 1
    return result

#----------------------------------------------------------
# main

def main():
    logConfig()
    parser = argparse.ArgumentParser(description="Command line cricket scores")
    parser.add_argument("match", nargs="?", type=int, help="match ID", default=0)
    args = parser.parse_args()
    print(getMatch(args.match))

#===========================================================
# Logging Configuration

def logConfig():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='/home/bmoss/code/python/cricket/output.log',
                        filemode='w')

#----------------------------------------------------------
# Tests in pytest format.

def test_getMatchAll():
    assert isinstance(getMatch(0), basestring)

def test_getMatchScore():
    assert isinstance(getMatch(754905), basestring)

#===========================================================

if __name__ == '__main__':
	main()