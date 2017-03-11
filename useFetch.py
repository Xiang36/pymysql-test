from sqlalchemy import create_engine
import pymysql

engine = create_engine("mysql+pymysql://root@127.0.0.1:3306/user",max_overflow=5)
result = engine.execute("select * from user")
print(result.fetchall())

