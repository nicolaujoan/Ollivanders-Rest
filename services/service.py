from flask_restful import abort
from repository.sql import dbRel
from domain.gilded_rose import *

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
       item_id =  dbRel.post_item(name, sell_in=10, quality=10)  # item posted with default values
       return {"id": item_id}    

    @staticmethod
    def delete_item(name):
        dbRel.delete_item_by_name(name)
        return {"deleted": name}

    @staticmethod
    def update_quality():
        db_stock = dbRel.stock()  # stock from db
        stock_objects = Service.domainize(db_stock)  # same but domain objects instead of dicts
        stock_gilded = GildedRose(stock_objects)  # GildedRose stock (domain stock)
        stock_gilded.updateQuality()
        stock_objects = stock_gilded.get_stock()  # updated objects list
        db_stock = Service.undomainize(stock_objects)  # updated items list (dicts representation)
        dbRel.update_stock(db_stock)

        
    @staticmethod
    def domainize(stock):
        domain_stock = []
        for item in stock:
            if item['itsname'] == '+5 Dexterity Vest':
                domain_stock.append(NormalItem(item['id'], item['itsname'], item['sell_in'], item['quality']))
            if item['itsname'] == 'Aged Brie':
                domain_stock.append(AgedBrie(item['id'], item['itsname'], item['sell_in'], item['quality']))
            if item['itsname'] == 'Elixir of the Mongoose':
                domain_stock.append(NormalItem(item['id'], item['itsname'], item['sell_in'], item['quality']))
            if item['itsname'] == 'Sulfuras, Hand of Ragnaros':
                domain_stock.append(Sulfuras(item['id'], item['itsname'], item['sell_in'], item['quality']))
            if item['itsname'] == 'Backstage passes to a TAFKAL80ETC concert':
                domain_stock.append(BackstagePass(item['id'], item['itsname'], item['sell_in'], item['quality']))
            if item['itsname'] == 'Conjured Mana Cake':
                domain_stock.append(Conjured(item['id'], item['itsname'], item['sell_in'], item['quality']))
        return domain_stock
            

    @staticmethod
    def undomainize(stock):
        db_stock = []
        for object in stock:
            db_stock.append({"id": object.id, "itsname": object.name, "sell_in": object.sell_in, "quality": object.quality})
        return db_stock    
