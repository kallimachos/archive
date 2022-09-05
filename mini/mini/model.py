#!/bin/python3
"""Model for mini."""

import json
import sqlite3 as sql
from os.path import exists

from gestalt import LoadConfig

settings = LoadConfig()
database = settings.database


def add(data):
    """Add an item to the DB."""
    item = json.loads(data)
    kind = item['kind']
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        if kind == 'game':
            cur.execute('INSERT INTO Game VALUES (:ID, :kind, :name, \
                        :company,:minPlayers, :maxPlayers, :age, :length, \
                        :link, :image, :notes)', item)
        elif kind == 'mini':
            cur.execute('INSERT INTO Mini VALUES (:ID, :kind, :name, :army, \
                        :type, :system, :company, :quantity, :status, :link, \
                        :image, :notes)', item)
        elif kind == 'paint':
            cur.execute('INSERT INTO Paint VALUES (:ID, :kind, :name, :color, \
                        :type, :company, :quantity, :link, :notes)', item)
        resp = json.dumps(cur.rowcount)
        return(resp)


def createdb():
    """Create DB and initialize tables."""
    if exists(database) is False:
        con = sql.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE Game
                        (ID INTEGER PRIMARY KEY,
                        kind TEXT NOT NULL,
                        name TEXT NOT NULL,
                        company TEXT,
                        minplayers INT,
                        maxplayers INT,
                        age INT,
                        length INT,
                        link TEXT,
                        image BLOB,
                        notes TEXT)""")
            cur.execute("""CREATE TABLE Mini
                        (ID INTEGER PRIMARY KEY,
                        kind TEXT NOT NULL,
                        name TEXT NOT NULL,
                        army TEXT,
                        type TEXT,
                        system TEXT,
                        company TEXT,
                        quantity INT,
                        status TEXT,
                        link TEXT,
                        image BLOB,
                        notes TEXT)""")
            cur.execute("""CREATE TABLE Paint
                        (ID INTEGER PRIMARY KEY,
                        kind TEXT NOT NULL,
                        name TEXT NOT NULL,
                        color TEXT,
                        type TEXT,
                        company TEXT,
                        quantity INT,
                        link TEXT,
                        notes TEXT)""")
    return(True)


def delete(data):
    """Delete an item from the DB."""
    item = json.loads(data)
    kind = item['kind']
    entry = (item['name'],)
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        if kind == 'game':
            cur.execute("DELETE FROM Game WHERE name = ?", entry)
        elif kind == 'mini':
            cur.execute("DELETE FROM Mini WHERE name = ?", entry)
        elif kind == 'paint':
            cur.execute("DELETE FROM Paint WHERE name = ?", entry)
        resp = json.dumps(cur.rowcount)
        return(resp)


def dump():
    """
    Return a raw dump of the DB.

    :returns: a raw dump of the DB
    :rtype: JSON
    """
    con = sql.connect(database)
    output = []
    for line in con.iterdump():
        output.append(line)
    resp = json.dumps(output)
    return(resp)


def edit(data):
    """Edit an item in the DB."""
    item = json.loads(data)
    kind = item['kind']
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        if kind == 'game':
            cur.execute("UPDATE Game SET name==:name, company==:company, \
                        minPlayers==:minPlayers, maxPlayers==:maxPlayers, \
                        age==:age, length==:length, link==:link, \
                        image==:image, notes==:notes WHERE name==:name", item)
        elif kind == 'mini':
            cur.execute("UPDATE Mini SET name==:name, army==:army, \
                        type==:type, system==:system, company==:company, \
                        quantity==:quantity, status==:status, link==:link, \
                        image==:image, notes==:notes WHERE name==:name", item)
        elif kind == 'paint':
            cur.execute("UPDATE Paint SET name==:name, color==:color, \
                        type==:type, company==:company, quantity==:quantity, \
                        link==:link, notes==:notes WHERE name==:name", item)
        resp = json.dumps(cur.rowcount)
        return(resp)


def sqlite_version():
    """Return the SQLite version of a database."""
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        resp = json.dumps('SQLite version: %s' % data)
        return(resp)


def view(data):
    """View an item in the DB."""
    item = json.loads(data)
    kind = item['kind']
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        if kind == 'game':
            cur.execute("SELECT * FROM Game WHERE name==:name", item)
        elif kind == 'mini':
            cur.execute("SELECT * FROM Mini WHERE name==:name", item)
        elif kind == 'paint':
            cur.execute("SELECT * FROM Paint WHERE name==:name", item)
        resp = json.dumps(cur.fetchone())
        return(resp)


# Specify database file and initialize DB if it does not already exist
createdb()

if __name__ == '__main__':
    # These statements are for testing only
    print(json.loads(sqlite_version()) + '\n')
    for line in json.loads(dump()):
        print(line)
