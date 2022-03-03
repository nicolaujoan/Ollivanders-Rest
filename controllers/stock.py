from re import S
from flask_restful import Resource
from services.service import Service

class Stock(Resource):
    def get(self):
        return Service.get_stock()