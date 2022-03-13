from flask_restful import Resource
from services.service import Service

class StockBySellIn(Resource):
    def get(self):
        return Service.get_stock_by_sell_in(), 200
