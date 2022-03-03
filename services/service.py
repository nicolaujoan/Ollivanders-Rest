import imp
from flask_restful import fields, marshal_with, abort

from repository.db import DB

class Service:

    @staticmethod
    def get_stock():
        return DB.stock()