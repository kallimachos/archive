#!/bin/python3

import cli
import gestalt

api = gestalt.LoadConfig().api
prompt = cli.MainMenu()


def test_api():
    pass


def test_callapi():
    result = cli.callapi(api, 'get', 'endpoints')
    assert result[0] == ['GET', '/']
    result = cli.callapi(api, 'put', 'call')
    assert result is None
    result = cli.callapi(api, 'post', 'call')
    assert result is None
    result = cli.callapi(api, 'delete', 'call')
    assert result is None


def test_clear():
    pass


def test_dump():
    assert cli.dump()[0] == 'BEGIN TRANSACTION;'
    assert cli.dump()[-1] == 'COMMIT;'


def test_emptyline():
    assert prompt.emptyline() is None


def test_endpoints():
    pass


def test_menu():
    pass


def test_precmd():
    result = prompt.precmd('api')
    assert result == 'api'
    result = prompt.precmd('#api')
    assert result == ''


def test_quit():
    pass


def test_shell():
    pass
