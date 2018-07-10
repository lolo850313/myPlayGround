from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

@app.route('/hello')
def hello():
    headers = {
        'content-type' : 'application/json',
        'location' : 'http://www.bing.com'
    }
    return 'hello 22',301,headers

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=app.config['DEBUG'],port=81)