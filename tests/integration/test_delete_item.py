from repository.sql.dbRel import init_db, inserts_db, get_db

# 1) Delete an item by its name (obtain its id)
# 2) Do a query to that id and check that returns nothing

def test_delete_item(app, client, name='Aged Brie'):

    with app.app_context():
        init_db()
        inserts_db()

    resp = client.delete('/item/{}'.format(name))
    assert resp.status_code == 204  # delete status code
    
    # data = resp.json
    # assert isinstance(data, dict)  # could be list but query limited to one result (LIMIT 1)

    with app.app_context():
        # db = get_db()
        # cur = db.cursor()
        # result = cur.execute('SELECT * FROM item WHERE itsname={}'.format(name))
        # print(result)
        init_db()
        inserts_db()

