from model import db
from sqlalchemy import Column, Integer, String, Enum
from model import monitor

# 模型
# 类 --》 表
# 实例化一个对象就是表里的一行记录
class User(db.Model):
    __table__name = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    passwd = Column(String(64), nullable=False) # 建议哈希存入
    role = Column(Enum("root", "普通用户"), nullable=False) # 建议设计成枚举型
    monitor = db.relationship("monitor", backref="user")
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role
        }
