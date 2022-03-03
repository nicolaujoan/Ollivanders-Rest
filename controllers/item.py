from flask_restful import Resource

class Item(Resource):
    def get(self, name):
        return {'name': name}
