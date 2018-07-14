from flask import jsonify
from app.fisher import app

from app.helper import is_isbn_or_key
from app.yushu_book import YuShuBook


@app.route('/book/search/<q>/<page>')
def search(q,page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    # return json.dumps(result), 200, {'content-type' : 'application/json'}
    return jsonify(result)
