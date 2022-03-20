from repository.sql.dbRel import init_db, inserts_db, get_db

# 1) insert item and collect the id
# 2) do a query to the id and check that the properties are ok

def test_post_item(client, app, name='Aged Brie'):
    with app.app_context():
        init_db()
        inserts_db()
    
    resp = client.post('/item/{}'.format(name))
    
    assert resp.status_code == 201  # correct response -> post

    posted_id = resp.json['id']  # id of posted item

    with app.app_context():
        db = get_db()
        cur = db.cursor()
        # we have the item inside a list in dict format
        item = [dict(row) for row in cur.execute('SELECT * FROM item WHERE id={}'.format(posted_id))]
        assert item[0]['id'] == posted_id
        assert item[0]['itsname'] == name
        assert item[0]['sell_in'] == 10 == item[0]['quality']
    

    
