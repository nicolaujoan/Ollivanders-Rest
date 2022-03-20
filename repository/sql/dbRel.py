import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

# our database
DATABASE = 'repository/sql/database.db'

# test DB
TEST_DB = 'repository/sql/test.db'

# itemNames
ITEMS_NAMES = [
    
    'Aged Brie', '+5 Dexterity Vest', 'Elixir of the Mongoose', 'Sulfuras, Hand of Ragnaros',
    'Backstage passes to a TAFKAL80ETC concert', 'Conjured Mana Cake'
]

# init the db in the app (register in the application, instances will be available)
# also adding commands to flask --> flask <command>

def init_app(app, production=True):
    if production:
        app.config['DATABASE'] = DATABASE
        
    else:
        app.config['DATABASE'] = TEST_DB
    
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(inserts_db_command)


# using the db in our requests

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# queries to our database

########## GET ##########

# ------- get all stock -------
def stock():
    db = get_db()  # get db connection
    cur = db.cursor()  # setup cursor

    items = [list(row) for row in cur.execute('SELECT * FROM item')]  # get all items
    close_db()
    return items

# ------- get an item by its name -------
def item(name):
    db = get_db()
    cur = db.cursor()

    if name in ITEMS_NAMES:
        item = [list(row) for row in cur.execute("SELECT * FROM item WHERE itsname = '%s'" % name)]
        close_db()
        return item
    return []

# -------- filters ---------

# sell-in
def stock_by_sell_in():
    db = get_db()  # get db connection
    cur = db.cursor()  # setup cursor

    items = [list(row) for row in cur.execute('SELECT * FROM item ORDER BY sell_in DESC;')]
    close_db()
    return items

# quality
def stock_by_quality():
    db = get_db()
    cur = db.cursor()

    items = [list(row) for row in cur.execute('SELECT * FROM item ORDER BY quality DESC;')]
    close_db()
    return items

########## DELETE #############
def delete_item_by_name(name):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM item WHERE itsname=:name LIMIT 1", {"name": name})
    db.commit()
    close_db()


########## POST ################

def post_item(name, sell_in=10, quality=10):
    db = get_db()
    cur = db.cursor()
    result = cur.execute("INSERT INTO item values (?, ?, ?, ?)", (None, name, sell_in, quality))  # this solves integrity issues
    id = result.lastrowid
    db.commit()
    close_db()
    return id  # return the id of the posted item

########## UPDATE #############

# python functions that will run sql commands (from our .sql files)

def init_db():
    db = get_db()

    with current_app.open_resource('repository/sql/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def inserts_db():
    db = get_db()

    with current_app.open_resource('repository/sql/inserts.sql') as f:
        db.executescript(f.read().decode('utf8'))


# flask <name> commands 

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


@click.command('inserts-db')
@with_appcontext
def inserts_db_command():
    """insert data into tables"""
    inserts_db()
    click.echo('Initial inserts done.')
