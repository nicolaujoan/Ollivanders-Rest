from flask_restful import Resource
from services.service import Service

class StockByQuality(Resource):
    def get(self):
        return Service.get_stock_by_quality(), 200
