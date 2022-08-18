'''
    orm     object relational mapping 对象关系映射
    flask不需要和复杂的sql语句打交道，只需要操控orm对象即可
    orm就是用来将数据里的表结构映射成模型类。类产生的对象就是数据库里的一行记录
'''
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from . import user, monitor

def init_app(app):
    db.init_app(app)
    db.create_all(app=app)
