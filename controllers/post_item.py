from flask_restful import Resource
from services.service import Service

class PostItem(Resource):
    def post(self, name):
        return Service.post_item(name), 200