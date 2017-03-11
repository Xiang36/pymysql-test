import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root@127.0.0.1:3306/test?charset=utf8", max_overflow=5)
Session = sessionmaker(bind=engine)
session = Session()

#生成一個SQLORM基類，創建表必須繼承他，別問我啥意思就是這麽規定的
Base = declarative_base()

class Person(Base):
    __tablename__ = 'userinfo'

    id   = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return "<Person(name='%s')>" % self.name

## create
# Base.metadata.create_all(ENGINE)  # 创建表结构

# #創建一個person對象
# person = Person(name='張巖林')
# #添加person對象，但是仍然沒有提交到數據庫
# session.add(person)
# #提交數據庫
# session.commit()

# session.add_all([
#     Person(name='張巖林'),
#     Person(name='aylin')
# ])
# session.commit()

print(session.query(Person).all())