from flask_restful import fields, marshal_with, abort

from repository.db import DB

class Service:

    @staticmethod
    def get_stock():
        return DB.stock()
    
    @staticmethod
    def get_item(name=False):
        # if not name:
        #     abort(404, message="item name needed")
        
        item = DB.item(name)
        if not item:
            abort(404, message="item {} not in stock".format(name))
        
        return {"name": item[0], "sell-in": item[1], "quality": item[2]}