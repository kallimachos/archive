#!/bin/python3
"""Controller logic for mini."""

import json
from os import path

import gestalt
import model
from bottle import (TEMPLATE_PATH, Bottle, debug, request, run, static_file,
                    template)

"""
Classic HTTP methods for REST APIs.

GET     Obtain information about a resource
  http://example.com/api/orders  (retrieve order list)

GET	    Obtain information about a resource
  http://example.com/api/orders/123  (retrieve order #123)

POST	Create a new resource
  http://example.com/api/orders
  (create a new order, from data provided with the request)

PUT	    Update a resource
  http://example.com/api/orders/123
  (update order #123, from data provided with the request)

DELETE  Delete a resource
  http://example.com/api/orders/123  (delete order #123)
"""

app = Bottle()

# append to bottle.TEMPLATE_PATH so views are correctly found by pytest
TEMPLATE_PATH.append('mini/views/')

# set static_path relative to this file
static_path = path.abspath(path.join(path.dirname(__file__), 'static'))

# set debug(True) for testing
debug(True)


@app.route('/', method='GET')
def index():
    """Return index template."""
    return(template('index'))


@app.route('/favicon.ico', method='GET')
def get_favicon():
    """Return the favicon."""
    return static_file('favicon.ico', root=static_path)


@app.route('/mini.css', method='GET')
def get_css():
    """Return the stylesheet."""
    return static_file('mini.css', root=static_path)


@app.route('/dump', method='GET')
@app.route('/api/dump', method='GET')
def dump():
    """
    Return a raw dump of the DB.

    :returns: a raw dump of the DB
    :rtype: JSON
    """
    if request.path == '/dump':
        return(template('dump', dump=model.dump()))
    else:
        return(model.dump())


@app.route('/endpoints', method='GET')
@app.route('/api/endpoints', method='GET')
def endpoints():
    """
    Return a list of API endpoints.

    :returns: a list of API endpoints
    :rtype: JSON array
    :example:

        >>> endpoints()  # doctest: +NORMALIZE_WHITESPACE
        '[["GET", "/"], ["GET", "/api/dump"], ["GET", "/api/endpoints"],
        ["GET", "/dump"], ["GET", "/endpoints"], ["GET", "/favicon.ico"],
        ["GET", "/mini.css"]]'
    """
    routes = []
    for route in app.routes:
        endpoint = [route.method, route.rule]
        routes.append(endpoint)
    routes.sort()
    resp = json.dumps(routes)
    if request.path == '/endpoints':
        return(template('endpoints', endpoints=resp))
    else:
        return(resp)


@app.error(404)
def missing(code):
    """Return 404 template."""
    return(template('404'))


@app.error(500)
def serverfault(code):
    """Return 500 template."""
    return(template('500'))


if __name__ == '__main__':
    settings = gestalt.LoadConfig()
    run(app, host=settings.host, port=settings.port, reloader=True)
