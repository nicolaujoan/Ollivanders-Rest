from flask_restful import fields, marshal_with, abort

from repository.dbMock import DB
from repository.sql import dbRel

class Service:

    @staticmethod
    def get_stock():
        return dbRel.stock()
    
    @staticmethod
    def get_item(name):
        item = dbRel.item(name)
        if not item:
            abort(404, message="item {} not in stock".format(name))
        return dbRel.item(name)