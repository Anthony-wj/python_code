from flask import Blueprint, request
from model import db
from model.user import User
from libs.util import generate_response
import json
user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/add", methods=["POST"])
def add_user():
    userName = request.json.get("username")
    password = request.json.get("password")
    user = User(name=userName, passwd=password, role="普通用户")
    db.session.add(user)
    db.session.commit()
    return generate_response(message="create user successfully")

@user_bp.route("/delete/<id>", methods=["DELETE"])
def delete_user(id):
    # 使用get查找，只针对主键
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return generate_response(message="delete successfully")
    else:
        return generate_response(status=10002, message="用户不存在")

@user_bp.route("/update", methods=["PUT"])
def change_user():
    id = request.args.get("id")
    user = User.query.get(id)
    username = request.json.get("username")
    userage = request.json.get("userage")
    user.name = username
    user.age = userage
    db.session.add(user)
    db.session.commit()
    return generate_response("change successfully")

@user_bp.route("/get", methods=["GET"])
def get_user():
    # 拿到多条记录，里面存放的是一个列表，列表里存放多个对象
    # 数据库对象不能直接返回，需要对其进行序列化操作
    id = request.args.get("id", None)
    if id:
        user = User.query.get(id)
        if user:
            return generate_response(data=user.to_json())
        else:
            return generate_response(status=10002,message="没有此用户")
    else:
        user_list = User.query.all()
        if user_list:
            result = [u.to_json() for u in user_list]
            return generate_response(data=result)
        else:
            return generate_response(status=10001,message="没有用户")


'''
    1.客户端发起请求
    2.服务器收到请求，解析http包，获取URL和请求方法等数据
    3.flask通过url和请求方法来判断处理。在url_map表中找到对应的endpoint，在view_function表里找到对应的视图函数。判断请求方法是否正确
    4.调用相应的视图函数做处理，可通过request对象对传入的参数进行获取，也可以通过动态url进行参数获取
    5.如果有数据库的操作，就导入相应的模型类，通过orm对象来操控数据库，实现数据库的增删改查。
    6.返回响应api数据
'''

'''
统一返回标准化
    json格式
    status 定义程序的逻辑状态
    message 解释状态码
    data 请求返回的数据
    {"status": 10000, "message": "数据请求成功", "data": []}
'''
