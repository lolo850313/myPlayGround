from flask import Flask,jsonify

app = Flask(__name__)
app.config.from_object('config')

from app.web import book

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=app.config['DEBUG'],port=81)