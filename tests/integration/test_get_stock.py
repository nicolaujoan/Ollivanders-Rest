from repository.sql.dbRel import init_db, inserts_db

def test_get_stock(app, client):

    expected_stock = [
    {
        "id": 1,
        "itsname": "Aged Brie",
        "sell_in": 2,
        "quality": 0
    },
    {
        "id": 2,
        "itsname": "+5 Dexterity Vest",
        "sell_in": 10,
        "quality": 20
    },
    {
        "id": 3,
        "itsname": "Elixir of the Mongoose",
        "sell_in": 5,
        "quality": 7
    },
    {
        "id": 4,
        "itsname": "Sulfuras, Hand of Ragnaros",
        "sell_in": 0,
        "quality": 80
    },
    {
        "id": 5,
        "itsname": "Sulfuras, Hand of Ragnaros",
        "sell_in": -1,
        "quality": 80
    },
    {
        "id": 6,
        "itsname": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 15,
        "quality": 20
    },
    {
        "id": 7,
        "itsname": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 10,
        "quality": 49
    },
    {
        "id": 8,
        "itsname": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 5,
        "quality": 49
    },
    {
        "id": 9,
        "itsname": "Conjured Mana Cake",
        "sell_in": 3,
        "quality": 6
    }
]


    with app.app_context():
        init_db()
        inserts_db()
    
    resp = client.get('/stock')
    assert resp.status_code == 200
    data = resp.json
    assert isinstance(data, list)
    assert data == expected_stock

