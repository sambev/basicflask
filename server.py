from flask import Flask, request, Response, render_template
from config.jinjacfg import setUpJinjaEnv
from util.pbkdf2 import pbkdf2_hex
from util.salts import getRandomSalt


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


    @app.route("/login")
    def login():
        """ Endpoint for authentication
            *Requires some sort of database
        """
        if request.method == 'POST':
            # Get the user information
            name = request.form['username']
            passwd = request.form['userpass']

            # Find a user with that username an compare passwords
            res = db.users.find({ 'name': name })
            if res.count() > 0:
                user = parseMongoResponse(res)[0]
                if user:
                    salt = user['salt']
                    thehash = pbkdf2_hex(passwd.encode('utf-8'), salt.encode('utf-8'))
                else:
                    error = 'Invalid Credentials'
                    return render_template('home.html', { 'error': error })

                if thehash == user['hash']:
                    # store user id in the session
                    session['user'] = user['name']
                    return redirect('/company_list')
                else:
                    error = 'Invalid Credentials'
                    return render_template('home.html', { 'error': error })
            else:
                error = 'Invalid Credentials'
                return render_template('home.html', { 'error': error })


    @app.route('/signup')
    def signup():
        """ End Point for signups
            *Requires some sort of database
        """
        if request.method == 'GET':
            return render_template('signup.html')

        if request.method == 'POST':
            if request.form['userpass'] != request.form['userpass2']:
                error = 'Passwords do not match'
                return render_template('signup.html', { 'error': error })

            salt =  getRandomSalt(16)
            thehash = pbkdf2_hex(request.form['userpass'].encode('utf-8'), salt.encode('utf-8'))

            # Make a new user out of the info
            new_user = {
                'name': request.form['username'],
                'salt': unicode(salt),
                'hash': unicode(thehash)
            }

            user_id = db.users.save(new_user)
            # store user id in the session
            session['user'] = new_user['name']

            return redirect('/home')

    return app


if __name__ == "__main__":
    app = buildApp()
    app.run()