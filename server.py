from flask import Flask, request, Response, render_template
from config.jinjacfg import setUpJinjaEnv
from controllers.auth import login, signup


app = Flask(__name__)
setUpJinjaEnv(app)


def buildApp(env='dev'):

    # Get the right config for the environment
    if env == 'dev':
        from config.dev import config
    elif env == 'test':
        from config.test import config
    elif env == 'production':
        from config.production import config

    app.config.update(config)

    # You can define routes this way
    @app.route('/')
    def index():
        """ Render the landing page """
        if request.method == 'GET':
            return render_template('index.html')


    @app.route('/home')
    def home():
        """ render the home page """
        if request.method == 'GET':
            return render_template('home.html')


    # Or this way.  There are others as well
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    app.add_url_rule('/signup', 'signup', signup, methods=['GET', 'POST'])

    return app


if __name__ == "__main__":
    app = buildApp()
    app.run()