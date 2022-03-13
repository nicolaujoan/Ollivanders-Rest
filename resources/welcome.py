from flask_restful import Resource

class Welcome(Resource):

    # curl http://localhost:8000/ 
    def get(self):
       return {"message": "Welcome to Ollivanders!"}, 200