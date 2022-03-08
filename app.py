from flask import Flask
from flask_restful import Api
from controllers.item import Item
from controllers.welcome import Welcome;
from controllers.stock import Stock
from controllers.quality import StockByQuality
from controllers.sell_in import StockBySellIn

# app instance
app = Flask(__name__)

# REST API
api = Api(app, catch_all_404s=True)

# RESOURCES
api.add_resource(Welcome, '/')
api.add_resource(Item, '/item/<name>')
api.add_resource(Stock, '/stock')
api.add_resource(StockBySellIn, '/stock/sell-in')
api.add_resource(StockByQuality, '/stock/quality')

# REPOSITORY (INIT OUR SQLITE3 DB)
from repository.sql import dbRel
dbRel.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)