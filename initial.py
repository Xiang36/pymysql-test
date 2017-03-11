from sqlalchemy import create_engine
import pymysql , pymysql.cursors

connection=pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='user',
                           port=3306,
                           charset='utf8')
try:
   with connection.cursor() as cursor:
       sql = 'select * from user'
       sql2 = 'select * from user where id = 1'
       cout=cursor.execute(sql2)
       print("Data Number： "+str(cout))
       for row in cursor.fetchall():
           print("ID: "+str(row[0])+'  Name： '+row[1]+"  Email： "+row[2])
       connection.commit()
finally:
    connection.close()

