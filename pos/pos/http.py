from flask import Flask
from pos.config import Config
from pos.models import db
from pos.views import products, index, transaction


def create_app(config=Config):
    """Create flask application
    
    :arg config: Flask configuration
    
    :return flask app
    """
    app = Flask(__name__)

    # load configuration
    app.config.from_object(config)

    # load sqlalchemy
    db.init_app(app)

    # register blueprint
    app.register_blueprint(products.bp)
    app.register_blueprint(index.bp)
    app.register_blueprint(transaction.bp)

    return app
