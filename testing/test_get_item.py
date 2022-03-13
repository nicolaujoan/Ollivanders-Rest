# testing '/item' route
import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

''' Tests for '/item/<name>'
    - only GET requests allowed
 '''


# returns a single item (format expected)
def test_aged_brie(client):
    resp = client.get('/item/Aged Brie')
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    assert resp.json == {'id': 1, 'name': 'Aged Brie', 'quality': 0, 'sell_in': 2}


# returns a list of items (format expected)
def test_sulfuras(client):
    resp = client.get('/item/Sulfuras, Hand of Ragnaros')
    assert resp.status_code == 200
    assert isinstance(resp.json, list)
    assert resp.json == [{'id': 4, 'name': 'Sulfuras, Hand of Ragnaros', 'quality': 80, 'sell_in': 0},
    {'id': 5, 'name': 'Sulfuras, Hand of Ragnaros', 'quality': 80, 'sell_in': -1}]
