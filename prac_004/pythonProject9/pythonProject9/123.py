import mysql.connector
from mysql.connector import Error
mydb=mysql.connector.connect(host='127.0.0.1',database='new',user='root',password='')
mycursor=mydb.cursor()
sql="SELECT * FROM user WHERE `name` = '"+'root'+"'"
mycursor.execute(sql)
user=mycursor.fetchall()
print(user)

for user in user:

  print("name: "+user[1]+" password: "+ user[2])
