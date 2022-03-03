
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def getinfo(name):
    query="SELECT * FROM user WHERE `name` = '"+name+"'"


    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)
        user = cursor.fetchall()
        print (user[0][1])
        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


getinfo("root")

