from flask_restful import Resource
from services.service import Service

class Stock(Resource):
    # curl http://localhost:5000/stock
    def get(self):
        return Service.get_stock(), 200
    
    # put == update
    # curl http://localhost:5000/stock -X PUT -v
    def put(self):
        return Service.update_quality(), 201