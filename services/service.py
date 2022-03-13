from flask_restful import abort
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
    

    # this converts one item into a 'json doc'
    @staticmethod
    def __format_one_item(item):
        desired_item = {
            'id': 0,
            'name': "",
            'sell_in': 0,
            'quality': 0
        }

        desired_item['id'] = item[0][0]
        desired_item['name'] = item[0][1]
        desired_item['sell_in'] = item[0][2]
        desired_item['quality'] = item[0][3]
        
        return desired_item
    

    # this one converts the output into a json doc or an array of json docs
    @staticmethod
    def __formated(item):

        if len(item) == 1:
            item = Service.__format_one_item(item)
            return item
        
        if len(item) > 1:
            items = [Service.__format_one_item([i]) for i in item]
            return items
        return item
    

    @staticmethod
    def get_item(name):
        item = dbRel.item(name)
        if not item:
            abort(404, message="item {} not in stock".format(name))
        else:
            item = Service.__formated(item)
        return item
    

    @staticmethod
    def post_item(name):
        dbRel.post_item(name, sell_in=10, quality=10)
    

    @staticmethod
    def delete_item(name):
        deleted_id = dbRel.delete_item_by_name(name)
        return {'id': deleted_id}
