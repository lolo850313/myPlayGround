from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    my_str = 'hello world'
    my_int = 10
    my_array = [3,4,5,6,7,8,9]
    my_dict = {'name':'xiaoming',
                'age':18,
    }

    return render_template("hello.html",my_str=my_str,my_int=my_int,my_array=my_array,my_dict=my_dict)

if __name__ == "__main__":
    app.run(debug=True)