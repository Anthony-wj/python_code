# from flask import current_app
# app = current_app

from flask import Blueprint, request, render_template
study_bp = Blueprint("study", __name__, url_prefix="/study")

@study_bp.route("/index")# 蓝图注册之后，study_bp --》endpoint就变成了study.index
def index():
    return "study index"

@study_bp.route("/endlish")
def endlish():
    return "study English"

# url参数
@study_bp.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    return f"username is {username}, password is {password} {request.url}"

# 路径参数
@study_bp.route("/login2/<username>/<password>")
def login2(username, password):
    return f"username is {username}, password is {password} "

@study_bp.route("/login3", methods=["POST"])
def login3():
    username = request.form.get("username")
    password = request.form.get("password")
    return f"username is {username}, password is {password}"

@study_bp.route("/login4")
def login4():
    username = request.json.get("username")
    password = request.json.get("password")
    return f"username is {username}, password is {password} "

@study_bp.route("/picture")
def picture():
    username = request.args.get("username")
    result = render_template('index.html', user = username)
    return result