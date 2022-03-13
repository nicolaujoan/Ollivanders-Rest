from flask_restful import Resource
from services.service import Service

class Stock(Resource):
    # curl http://localhost:8000/stock
    def get(self):
        return Service.get_stock(), 200