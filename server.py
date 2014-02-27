from flask import Flask, request, Response, render_template
from config.jinjacfg import setUpJinjaEnv
from controllers.auth import login, signup
from controllers.base import index, home
from config.settings import SETTINGS


def buildApp(env='dev'):

    app = Flask(__name__)
    setUpJinjaEnv(app)
    app.config.update(SETTINGS[env])

    app.add_url_rule('/', 'index', index, methods=['GET'])
    app.add_url_rule('/home', 'home', home, methods=['GET'])
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    app.add_url_rule('/signup', 'signup', signup, methods=['GET', 'POST'])

    return app


if __name__ == "__main__":
    app = buildApp()
    app.run()