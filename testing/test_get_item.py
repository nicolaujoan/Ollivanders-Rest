# testing '/item' route
from repository.sql.dbRel import init_db, inserts_db


# returns a single item (format expected)
def test_aged_brie(client, app):
    with app.app_context():
        init_db()
        inserts_db()

    # aged brie --> {'id': 1, 'name': 'Aged Brie', 'quality': 0, 'sell_in': 2}


    resp = client.get('/item/Aged Brie')  # peticion

    # type and status code ckecks
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)

    # load our json
    data = resp.json

    # fields check
    assert data['id'] == 1
    assert data['name'] == 'Aged Brie'
    assert data['quality'] == 0
    assert data['sell_in'] == 2


# returns a list of items (format expected)
def test_sulfuras(client):
    resp = client.get('/item/Sulfuras, Hand of Ragnaros')
    assert resp.status_code == 200
    assert isinstance(resp.json, list)
    assert resp.json == [{'id': 4, 'name': 'Sulfuras, Hand of Ragnaros', 'quality': 80, 'sell_in': 0},
    {'id': 5, 'name': 'Sulfuras, Hand of Ragnaros', 'quality': 80, 'sell_in': -1}]
