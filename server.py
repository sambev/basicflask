from flask import Flask, request, Response, render_template
from config.jinjacfg import setUpJinjaEnv
from blueprints.auth import auth
from blueprints.base import base
from api_views.user import UserAPI
from config.settings import SETTINGS
from util.common import register_api


app = Flask(__name__)
setUpJinjaEnv(app)
app.config.update(SETTINGS['dev'])

# blueprints
app.register_blueprint(auth)
app.register_blueprint(base)

# api registers
register_api(app, UserAPI, 'user_api', '/users/', pk='user_id')


if __name__ == "__main__":
    app.run()
