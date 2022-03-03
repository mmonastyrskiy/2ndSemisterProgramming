from tkinter import *
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

class User:
    def __init__(self,name):
        self.user=123
        query = "SELECT * FROM user WHERE `name` = '" + name + "'"

        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)

            cursor = conn.cursor()
            cursor.execute(query)
            user = cursor.fetchall()
            self.userid=user[0][0]
            self.user=user[0][1]
            self.password=user[0][2]
            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()



user1=User(name="root")
print(user1.user)
print(user1.password)

