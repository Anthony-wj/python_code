from model import db
from sqlalchemy import Column, Integer, String, Enum

class monitor(db.Model):
    __tablename__ = "monitor"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    prov= Column(String(64), nullable=False)
    isp = Column(String(64), nullable=False)
    threshold = Column(Integer, nullable=False)
    action = Column(Enum("大于", "小于"))