from flask_restful import abort

# from repository.dbMock import DB
from repository.sql import dbRel

class Service:

    @staticmethod
    def get_stock():
        return dbRel.stock()
    
    @staticmethod
    def get_stock_by_sell_in():
        return dbRel.stock_by_sell_in()
    
    @staticmethod
    def get_stock_by_quality():
        return dbRel.stock_by_quality()
    
    @staticmethod
    def get_item(name):
        item = dbRel.item(name)
        if not item:
            abort(404, message="item {} not in stock".format(name))
        return dbRel.item(name)
    
    @staticmethod
    def post_item(name):
        dbRel.post_item(name, sell_in=10, quality=10)
