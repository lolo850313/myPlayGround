from flask import Flask, make_response, request, render_template, session, redirect, url_for, escape

app = Flask(__name__)
app.secret_key = "fkdjsafjdkfdlkjfadskjfadskljdsfklj"


@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        return '登录用户名是： ' + username + '<br>' + \
            "<b><a href = '/logout'>点击这里注销</br>"
    
    return "你暂时未登录， <br><a href='/login'></b>" + \
        "点击这里登录</b></a>"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] == request.form['username']
        return redirect(url_for('index'))
    return '''
    <form action="" methods="post">
        <p><input type="text" name="username"/></p>
        <p><input type="submit" value="登录"/></p>
    </form>
    '''

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)