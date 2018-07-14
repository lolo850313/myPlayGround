from flask import Flask
from helper import is_isbn_or_key
from yushu_book import YuShuBook
# import json
from flask import jsonify 

app = Flask(__name__)
app.config.from_object('config')

@app.route('/book/search/<q>/<page>')
def search(q,page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    # return json.dumps(result), 200, {'content-type' : 'application/json'}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=app.config['DEBUG'],port=81)