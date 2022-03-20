# testing '/' route
import pytest


def test_home(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    assert resp.json.get('message', 'Welcome to Ollivanders!')


def test_home_bad_http_method(client):
    resp = client.post('/')  # 405, method not allowed, this route only works with GET
    assert resp.status_code == 405