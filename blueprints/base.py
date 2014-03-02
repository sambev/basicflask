from flask import Blueprint, request, render_template

base_bp = Blueprint('base_bp', __name__,
                    template_folder='templates')

@base_bp.route('/', methods=['GET'])
def index():
    """ Render the landing page """
    if request.method == 'GET':
        return render_template('index.html')


@base_bp.route('/home', methods=['GET'])
def home():
    """ render the home page """
    if request.method == 'GET':
        return render_template('home.html')


