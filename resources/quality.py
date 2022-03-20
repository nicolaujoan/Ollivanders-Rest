from flask_restful import Resource
from services.service import Service

class StockByQuality(Resource):
    # curl http://localhost:8000/stock/quality
    def get(self):
        return Service.get_stock_by_quality(), 200
