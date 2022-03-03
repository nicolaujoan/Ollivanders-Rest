from flask_restful import Resource

class Welcome(Resource):
   def get(self):
       return '<h1>Welcome to Ollivanders</h1>'