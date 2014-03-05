from flask import Blueprint, request, render_template

base = Blueprint('base', __name__,
                 template_folder='templates')


@base.route('/', methods=['GET'])
def index():
    """ Render the landing page """
    if request.method == 'GET':
        return render_template('index.html')


@base.route('/home', methods=['GET'])
def home():
    """ render the home page """
    if request.method == 'GET':
        return render_template('home.html')
