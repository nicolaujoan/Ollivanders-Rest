from flask import Flask

def create_app(production=False):
    app = Flask(__name__)
    # app.config.from_pyfile(config_filename)

    # if app.config.db = sqlite
    # take the sqlite db
    from repository.sql import dbRel
    if production:
        dbRel.init_app(app)
    else:
        dbRel.init_app(app, False)

    return app
