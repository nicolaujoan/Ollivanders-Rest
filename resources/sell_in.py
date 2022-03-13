from flask_restful import Resource
from services.service import Service

class StockBySellIn(Resource):
    # curl http://localhost:5000/stock/sell-in
    def get(self):
        return Service.get_stock_by_sell_in(), 200
