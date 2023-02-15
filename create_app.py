from flask import Flask

from bp_api.views import bp_api
from bp_posts.views import bp_posts

import config_logger


def create_and_config_app(config_path):

    app = Flask(__name__)

    app.register_blueprint(bp_posts)
    app.register_blueprint(bp_api, url_prefix='/api')
    app.config.from_pyfile(config_path)
    config_logger.config(app)

    return app
