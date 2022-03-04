try:
    import tkinter
    from tkinter import messagebox
    import mysql.connector as conn
    import os
    import configparser
    import platform 
    import subprocess
    import logging
except ImportError as e:
    os.command(f"pip install {e.split()[-1]}")

users = []
CONFIG_FILE = "config.ini"

logging.basicConfig(filename='access.log')
logging.basicConfig(format='%(asctime)s %(message)s')

try:
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)


    host = config.get("DEFAULT","host")
    dbname = config.get("DEFAULT","dbname")
    login = config.get("DEFAULT","login")
    password = config.get("DEFAULT","password")

except Exception:
    print("Error reading configuration file")

class User:
    def __init__(self,id,name,password):
        self.id = id
        self.name = name
        self.password = password

class Connection:
    def __init__(self,name,password):
        self.name = name
        self.password = password


    def Auth(self):
        try:
            mydb=conn.connect(host=host,database=dbname,user=login,password=password)
            c = mydb.cursor()
        except Exception as e:
            messagebox.showerror(message=e)

        c.execute(f"SELECT * FROM user WHERE name = '{self.name}'")
        user = c.fetchall()
        if len(user) == 0:
            messagebox.showwarning(title="",message="Неверное имя пользователя")
            logging.warning(f"Someone entered uknown username:{self.name}")
        else:
            c.execute(f"SELECT * FROM user WHERE name = '{self.name}' AND password = '{self.password}'")
            record = c.fetchall()
            if len(record) == 0:
                messagebox.showerror(message="Неверный пароль")
                logging.warning(f"Someone entered wrong creds:{self.name}::{self.password}")
            else:
                callback = tkinter.Tk()
                callback.resizable(False,False)
                callback.title("Успех")
                Ans = tkinter.Label(callback,text = f"Здравствуйте,{self.name}")
                logging.warning(f"User:{self.name} successfully logged in ")
                Ans.pack()
                global users
                users.append(User(record[0][0],record[0][1],record[0][2]))

                callback.mainloop()
def main():
    window = tkinter.Tk()
    window.resizable(False,False)
    window.title("Введите логин и пароль")
    window.geometry("230x100")
    name_l = tkinter.Label(text="Логин ").grid(row=0,column=0)
    name = tkinter.Entry(window)
    name.grid(row=0,column=2,columnspan=3)

    passwd_l = tkinter.Label(text="Пароль ").grid(row=1,column=0)
    passwd = tkinter.Entry(window,show="*")
    passwd.grid(row=1,column=2,columnspan=3)
    B = tkinter.Button(window,text="Войти",command= lambda: Connection(name.get(),passwd.get()).Auth()).grid(row=2,column=1)
    window.mainloop()



if __name__ == "__main__":
    main()
else:
    print("This file could not be imported")

