from resources.factory import create_app
from flask_restful import Api
from resources.item import Item
from resources.welcome import Welcome;
from resources.stock import Stock
from resources.quality import StockByQuality
from resources.sell_in import StockBySellIn

# app instance (production or test mode)
app = create_app(production=False)  # need to create a config file maybe for testing purposes or to put the route of the db

# REST API
api = Api(app, catch_all_404s=True)

# RESOURCES
api.add_resource(Welcome, '/')
api.add_resource(Item, '/item/<name>')
api.add_resource(Stock, '/stock')
api.add_resource(StockBySellIn, '/stock/sell-in')
api.add_resource(StockByQuality, '/stock/quality')


if __name__ == '__main__':
    app.run(debug=True)