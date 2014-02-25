from flask import Flask, request, Response, render_template
from config.jinjacfg import setUpJinjaEnv
from util.pbkdf2 import pbkdf2_hex
from util.salts import getRandomSalt
from controllers.auth import login, signup


app = Flask(__name__)
setUpJinjaEnv(app)


def buildApp(env='dev'):

    # Get the right config for the environment
    if env == 'dev':
        from config.dev import config
        app.config.update(config)
    elif env == 'test':
        from config.test import config
        app.config.update(config)
    elif env == 'production':
        from config.production import config
        app.config.update(config)


    @app.route("/")
    def index():
        """ Render the home page """
        if request.method == 'GET':
            return render_template('index.html')

    app.add_url_rule('/login', 'login', login)
    app.add_url_rule('/signup', 'signup', signup)

    return app


if __name__ == "__main__":
    app = buildApp()
    app.run()