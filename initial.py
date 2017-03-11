import pymysql , pymysql.cursors

connection=pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='user',
                           port=3306,
                           charset='utf8')
try:
   with connection.cursor() as cursor:
       sql='select * from user'
       cout=cursor.execute(sql)
       print("Data Number： "+str(cout))
       for row in cursor.fetchall():
           print("ID: "+str(row[0])+'  Name： '+row[1]+"  Email： "+row[2])
       connection.commit()
finally:
    connection.close()