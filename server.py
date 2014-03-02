from flask import Flask, request, Response, render_template
from config.jinjacfg import setUpJinjaEnv
from blueprints.auth import auth_bp
from blueprints.base import base_bp
from config.settings import SETTINGS


def buildApp(env='dev'):

    app = Flask(__name__)
    setUpJinjaEnv(app)
    app.config.update(SETTINGS[env])

    app.register_blueprint(auth_bp)
    app.register_blueprint(base_bp)

    return app


if __name__ == "__main__":
    app = buildApp()
    app.run()