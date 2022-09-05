#!/bin/python3

import webtest

import controller
import gestalt

index = gestalt.LoadConfig().index

app = webtest.TestApp(controller.app)
status = gestalt.checkresponse(index)


def test_index():
    assert app.get(index).status_int == 200


def test_get_favicon():
    assert app.get(index + '/favicon.ico').status_int == 200


def test_get_css():
    assert app.get(index + '/mini.css').status_int == 200


def test_dump():
    assert app.get(index + '/dump').status_int == 200
    assert app.get(index + '/api/dump').status_int == 200


def test_endpoints():
    assert app.get(index + '/endpoints').status_int == 200
    assert app.get(index + '/api/endpoints').status_int == 200


def test_missing():
    assert 'Sorry, this page does not exist.' in controller.missing(404)


def test_serverfault():
    assert 'Sorry, there has been a server error.' \
        in controller.serverfault(500)
