from flask import Flask

def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile(config_filename)

    # if app.config.db = sqlite
    # take the sqlite db    
    from repository.sql import dbRel
    dbRel.init_app(app)

    return app
