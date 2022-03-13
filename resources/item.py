from flask_restful import Resource
from services.service import Service

class Item(Resource):
    # curl http://localhost:8000/item/<name> with %20 for spaces
    def get(self, name):
        return Service.get_item(name), 200
    
    # curl http://localhost:8000/item/<name> -X POST -v
    def post(self, name):
        return Service.post_item(name), 201
    
    # curl http://localhost:8000/item/<name> -X DELETE  -v
    def delete(self, name):
        return Service.delete_item(name), 204
