from flask import Flask
from flask_restful import Api
from controllers import *
from controllers.welcome import Welcome;

# app instance
app = Flask(__name__)

# REST API
api = Api(app, catch_all_404s=True)

# welcome resource with its endpoint
api.add_resource(Welcome, '/')

if __name__ == '__main__':
    app.run(debug=True)