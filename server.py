from flask import Flask
from config.jinjacfg import render


app = Flask(__name__)


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
        return render('index.html')

    return app


if __name__ == "__main__":
    app = buildApp()
    app.run()