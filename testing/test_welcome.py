# testing '/' route
import pytest
from app import app

# (setup function) flask client instance to simulate http requests to our Flask app
@pytest.fixture  # define on co
def client():
    return app.test_client()


''' Tests for '/'

    - only GET requests allowed
    - returns a json response body that has one field called "message"
        which maps to the string "Welcome to Ollivanders!"

 '''


def test_home(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    assert resp.json.get('message', 'Welcome to Ollivanders!')


def test_home_bad_http_method(client):
    resp = client.post('/')  # 405, method not allowed, this route only works with GET
    assert resp.status_code == 405