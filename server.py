from flask import Flask
from config.jinjacfg import render


app = Flask(__name__)

@app.route("/")
def index():
    return render('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run()