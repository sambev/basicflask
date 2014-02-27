from flask import request, render_template

def index():
    """ Render the landing page """
    if request.method == 'GET':
        return render_template('index.html')


def home():
    """ render the home page """
    if request.method == 'GET':
        return render_template('home.html')


