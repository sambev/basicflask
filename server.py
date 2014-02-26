from flask import Flask, request, Response, render_template
from config.jinjacfg import setUpJinjaEnv
from controllers.auth import login, signup
from config.settings import SETTINGS


def buildApp(env='dev'):

    app = Flask(__name__)
    setUpJinjaEnv(app)
    app.config.update(SETTINGS[env])


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