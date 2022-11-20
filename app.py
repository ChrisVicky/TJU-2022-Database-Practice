from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import db
import config
from api import app as api


def create_app():
    '''Factory Pattern: Create Flask app.'''
    app = Flask(__name__)

    # Initialization flask app
    configure_app(app, config.Config)
    configure_blueprints(app)
    configure_extensions(app)
    # 不使用 Jinja2，用不到模版过滤器和上下文处理器
    configure_before_handlers(app)
    configure_after_handlers(app)
    configure_errorhandlers(app)

    return app


def configure_app(app, config_class):
    app.config.from_object(config_class)
    # 不检查路由中最后是否有斜杠/
    app.url_map.strict_slashes = False


def configure_blueprints(app):
    # 注册 blueprint
    app.register_blueprint(api, url_prefix='/api')


def configure_extensions(app):
    '''Configures the extensions.'''
    # Enable CORS
    # cors.init_app(app)
    # Init Flask-SQLAlchemy
    db.init_app(app)
    # Init Flask-Migrate
    # migrate.init_app(app, db)
    # Init Flask-Mail
    # mail.init_app(app)


def configure_before_handlers(app):
    '''Configures the before request handlers'''
    pass


def configure_after_handlers(app):
    '''Configures the after request handlers'''
    pass


def configure_errorhandlers(app):
    '''Configures the error handlers'''
    pass


app = create_app()
if __name__ == '__main__':
    app.run(debug=True, port=8085)
