from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

#装饰器将函数绑定到一起
@app.route("/r/")
def hello_world1():
    return "hello world1"

def hello_world2():
    return "hello world2"

app.add_url_rule("/rr/","hello", hello_world2)

if __name__ == "__main__":
    app.run()