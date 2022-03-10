from flask_restful import Resource
from services.service import Service

class Item(Resource):
    def get(self, name):
        return Service.get_item(name),200
    
    def post(self, name):
        return Service.post_item(name), 201
    
    def delete(self, name):
        return Service.delete_item(name), 204
