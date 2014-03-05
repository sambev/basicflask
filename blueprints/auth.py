from flask import Blueprint, request, render_template, session, redirect
from util.pbkdf2 import pbkdf2_hex
from util.salts import getRandomSalt

auth = Blueprint('auth', __name__,
                 template_folder='templates')

# TODO Uncomment and configure this to give this blueprint a handle to the db
# @auth.record
# def getDB(state):
#     client = MongoClient(state.app.config['DB_URI'])
#     auth.db = client[state.app.config['DB_NAME']]


@auth.route('/login', methods=['POST'])
def login():
    """ Endpoint for authentication
        *Requires some sort of database
    """
    #TODO remove this return when you have a db to use
    #return early so the code below doesn't break everything
    return redirect('/home')

    # A good starting point to handle login.  Configure for your own db.
    # if request.method == 'POST':
    #     # Get the user information
    #     name = request.form['username']
    #     passwd = request.form['userpass']

    #     # Find a user with that username an compare passwords
    #     res = db.users.find({'name': name})
    #     if res.count() > 0:
    #         # user = <find a user with your db>
    #         if user:
    #             salt = user['salt']
    #             thehash = pbkdf2_hex(passwd.encode('utf-8'),
    #                                  salt.encode('utf-8'))
    #         else:
    #             error = 'Invalid Credentials'
    #             return render_template('home.html', error=error)

    #         if thehash == user['hash']:
    #             # store user id in the session
    #             session['user'] = user['name']
    #             return redirect('/home')
    #         else:
    #             error = 'Invalid Credentials'
    #             return render_template('home.html', error=error)
    #     else:
    #         error = 'Invalid Credentials'
    #         return render_template('home.html', error=error)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """ End Point for signups
        *Requires some sort of database
    """
    if request.method == 'GET':
        return render_template('signup.html')

    # TODO, uncomment and configure once you get your db up
    if request.method == 'POST':
        return redirect('/home')
    #     if request.form['userpass'] != request.form['userpass2']:
    #         error = 'Passwords do not match'
    #         return render_template('signup.html', error=error)

    #     salt = getRandomSalt(16)
    #     thehash = pbkdf2_hex(request.form['userpass'].encode('utf-8'),
    #                          salt.encode('utf-8'))

    #     # Make a new user out of the info
    #     new_user = {
    #         'name': request.form['username'],
    #         'salt': unicode(salt),
    #         'hash': unicode(thehash)
    #     }

    #     # You'll need a database to save it to
    #     # user_id = db.users.save(new_user)
    #     # store user id in the session
    #     session['user'] = new_user['name']

    #     return redirect('/home')
