from flask import Flask, make_response, request, render_template, session, redirect, url_for, escape

app = Flask(__name__)

@app.route("/")
def index():    
    return render_template("log_in.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username'] == "admin":
        return redirect(url_for('success'))
        return redirect(url_for('index'))

@app.route("/success")
def success():
    return 'logged in successfully'


if __name__ == "__main__":
    app.run(debug=True)