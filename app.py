from flask import Flask
from flask_restful import Api
from resources.item import Item
from resources.welcome import Welcome;
from resources.stock import Stock
from resources.quality import StockByQuality
from resources.sell_in import StockBySellIn

def create_app(production=False):
    # app instance (production or test mode)
    app = Flask(__name__)

    # if app.config.db = sqlite
    # take the sqlite db
    from repository.sql import dbRel
    if production:
        dbRel.init_app(app)
    else:
        dbRel.init_app(app, False)

    # REST API
    api = Api(app, catch_all_404s=True)

    # RESOURCES
    api.add_resource(Welcome, '/')
    api.add_resource(Item, '/item/<name>')
    api.add_resource(Stock, '/stock')
    api.add_resource(StockBySellIn, '/stock/sell-in')
    api.add_resource(StockByQuality, '/stock/quality')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)