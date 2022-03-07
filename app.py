from flask import Flask
from flask_restful import Api
from controllers.item import Item
from controllers.welcome import Welcome;
from controllers.stock import Stock

# app instance
app = Flask(__name__)

# REST API
api = Api(app, catch_all_404s=True)

# RESOURCES
api.add_resource(Welcome, '/')
api.add_resource(Item, '/item/<name>')
api.add_resource(Stock, '/stock')

# REPOSITORY (INIT OUR SQLITE3 DB)
from repository.sql import dbRel
dbRel.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)