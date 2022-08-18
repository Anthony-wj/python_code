from flask import request, render_template, current_app

app = current_app

@app.route("/hello/")
def hello():
    return "Hello"

@app.route("/index", methods=["GET", "POST"])
def index():
    username = request.args.get("username")
    result = render_template("index.html", user = username)
    return result