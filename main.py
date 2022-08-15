from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

def hello():
    return "Hello"

@app.route("/login/<username>/<password>")
def login1(username, password):
    if username == "root" and password == "123456":
        return "登录成功"
    else:
        return "登录失败"
@app.route("/login2", method=["GET", "POST"])
def login2():
    username = request.args.get("username")

app.add_url_rule("/hello", view_func=hello)

app.run(debug=True, host="127.0.0.1", port=8080)
