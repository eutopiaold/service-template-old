"""package constructor"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_graphql import GraphQLView

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app

""" 
from schema import schema
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True  # for having the GraphiQL interface
)
)
"""

