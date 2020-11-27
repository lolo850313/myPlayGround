from flask import Flask
app = Flask(__name__)

@app.route("/hello/<name>")
def hello_world(name):
    return "hello " + name

@app.route("/blog/<int:postId>")
def show_blog(postId):
    return "blog number %d"  %postId

@app.route("/rev/<float:revNo>/")
def revision(revNo):
    return "Revision Number %f" %revNo

if __name__ == "__main__":
    app.run(debug=True)