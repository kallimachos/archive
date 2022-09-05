#!/bin/python3
"""CLI client for interacting with the mini REST API."""

import cmd
import json
import os

import requests

import gestalt

# set api url
api = gestalt.LoadConfig().api


def callapi(api, method, call):
    """
    Call the mini REST API.

    :param api: the API endpoint root
    :type api: string
    :param call: the function call
    :type api: string
    :param method: the HTTP method
    :type api: string
    :returns: API response
    :rtype: JSON
    """
    if method == 'get':
        r = requests.get(api + '/' + call)
        resp = json.loads(r.text)
        return(resp)
    elif method == 'put':
        pass
    elif method == 'post':
        pass
    elif method == 'delete':
        pass


def dump():
    """
    Print a raw dump of the DB.

    :param api: the API endpoint root
    :type api: string
    """
    output = callapi(api, 'get', 'dump')
    for line in output:
        print(line)
    return(output)


def endpoints():
    """
    Print a list of API endpoints.

    :param api: the API endpoint root
    :type api: string
    """
    output = callapi(api, 'get', 'endpoints')
    for endpoint in output:
        print(endpoint[0] + ' ' + endpoint[1])
    return(output)


class MainMenu(cmd.Cmd):
    """Main menu."""

    def __init__(self, intro="Mini CLI", prompt=">>> "):
        """Initialize MainMenu object."""
        cmd.Cmd.__init__(self)
        self.intro = intro
        self.prompt = prompt
        self.doc_header = "Mini CLI (type help <topic>):"

    def emptyline(self):
        """Retain prompt if user enters empty line."""
        pass

    def do_api(self, args):
        """Print API base URL.

        >>> MainMenu().onecmd('api')
        Making API requests to http://0.0.0.0:8080/api
        """
        text = 'Making API requests to ' + api
        print(text)

    def do_clear(self, args):
        """Clear screen.

        >>> MainMenu().onecmd('clear')
        """
        os.system('clear')

    def do_dump(self, args):
        """Dump database.

        >>> MainMenu().onecmd('dump')  # NOQA  # doctest: +NORMALIZE_WHITESPACE
        BEGIN TRANSACTION;
        CREATE TABLE Game
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
                            notes TEXT);
        INSERT INTO "Game" VALUES(1,'game','Game1','Company1',1,4,10,30,'www.example.com',NULL,'Fun!');
        INSERT INTO "Game" VALUES(2,'game','Game2','Company1',1,4,10,30,'www.example.com',NULL,'Fun!');
        INSERT INTO "Game" VALUES(3,'game','Game3','Company1',1,4,10,30,'www.example.com',NULL,'Fun!');
        CREATE TABLE Mini
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
                            notes TEXT);
        INSERT INTO "Mini" VALUES(1,'mini','Mini1','Orcs and Goblins','core','WFB','Company1',10,'painted','www.example.com',NULL,'Fun!');
        INSERT INTO "Mini" VALUES(2,'mini','Mini2','Orcs and Goblins','core','WFB','Company1',10,'painted','www.example.com',NULL,'Fun!');
        INSERT INTO "Mini" VALUES(3,'mini','Mini3','Orcs and Goblins','core','WFB','Company1',10,'painted','www.example.com',NULL,'Fun!');
        CREATE TABLE Paint
                            (ID INTEGER PRIMARY KEY,
                            kind TEXT NOT NULL,
                            name TEXT NOT NULL,
                            color TEXT,
                            type TEXT,
                            company TEXT,
                            quantity INT,
                            link TEXT,
                            notes TEXT);
        INSERT INTO "Paint" VALUES(1,'paint','Paint1','green','matte','Company1',1,'www.example.com','Fun!');
        INSERT INTO "Paint" VALUES(2,'paint','Paint2','green','matte','Company1',1,'www.example.com','Fun!');
        INSERT INTO "Paint" VALUES(3,'paint','Paint3','green','matte','Company1',1,'www.example.com','Fun!');
        COMMIT;
        """
        dump()

    def do_endpoints(self, args):
        """Print endpoints.

        >>> MainMenu().onecmd('endpoints')  # doctest: +NORMALIZE_WHITESPACE
        GET /
        GET /api/dump
        GET /api/endpoints
        GET /dump
        GET /endpoints
        GET /favicon.ico
        GET /mini.css
        """
        endpoints()

    def do_menu(self, line):
        """Print menu options.

        >>> MainMenu().onecmd('menu')  # doctest: +NORMALIZE_WHITESPACE
        Dump - Print database dump
        Endpoints - print endpoints
        Quit
        """
        print("""
Dump - Print database dump
Endpoints - print endpoints
Quit
           """)

    def do_quit(self, args):
        """Quit program.

        >>> MainMenu().onecmd('quit')
        True
        """
        os.system('clear')
        return True

    def do_shell(self, line):
        """Run a shell command.

        >>> MainMenu().onecmd('shell echo "hi"')
        running shell command:  echo "hi"
        hi
        <BLANKLINE>
        """
        print("running shell command: ", line)
        output = os.popen(line).read()
        print(output)
        self.last_output = output

    do_EOF = do_quit

    def help_api(self):
        """
        Print api command help message.

        >>> MainMenu().onecmd('help api')
        API URL
        """
        print("API URL")

    def help_clear(self):
        """
        Print clear command help message.

        >>> MainMenu().onecmd('help clear')
        Clear screen
        """
        print("Clear screen")

    def help_dump(self):
        """
        Print dump command help message.

        >>> MainMenu().onecmd('help dump')
        Raw dump of the DB
        """
        print("Raw dump of the DB")

    def help_endpoints(self):
        """
        Print endpoints command help message.

        >>> MainMenu().onecmd('help endpoints')
        API endpoints
        """
        print("API endpoints")

    def help_menu(self):
        """
        Print menu command help message.

        >>> MainMenu().onecmd('help menu')
        Main menu
        """
        print("Main menu")

    def help_quit(self):
        """
        Print quit command help message.

        >>> MainMenu().onecmd('help quit')
        Quit session
        """
        print("Quit session")

    help_EOF = help_quit

    def precmd(self, line):
        """Execute pre-command."""
        newline = line.strip()
        is_cmt = newline.startswith('#')
        if is_cmt:
            return ('')
        return (line)


if __name__ == '__main__':
    os.system('clear')
    mmenu = MainMenu()
    mmenu.cmdloop()
