try:
    import tkinter
    from tkinter import messagebox
    import mysql.connector as conn
    import os
    import configparser
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
    def __init__(self,login,password):
        self.login = login
        self.password = password
        if self.Auth():
            self.Fetch()

    def Fetch(self):
        try:
            mydb = conn.connect(host = host, database=dbname,user=login,password=password)
            c = mydb.cursor()
        except Exception as e:
            messagebox.showerror(message=e)
        c.execute(f"SELECT * FROM login WHERE name = '{self.login}' AND password = '{self.password}'")
        data = c.fetchall()
        id_ = int(data[0][0])
        c.execute(f"SELECT * FROM user_data WHERE user_id = {id_}")
        data = c.fetchall()
        surname =data[0][1]
        name = data[0][2]
        secondname = data[0][3]
        birth_date = data[0][4]
        email = data[0][5]
        phone = data[0][6]
        global users
        logging.warning(f"successfully fetched data:{id_},{self.login},{surname},{name},{secondname},{birth_date},{email},{phone}")
        users.append([id_,self.login,surname,name,secondname,birth_date,email,phone])
        print(users[-1])

    def Auth(self) -> bool:
        try:
            mydb=conn.connect(host=host,database=dbname,user=login,password=password)
            c = mydb.cursor()
        except Exception as e:
            messagebox.showerror(message=e)

        c.execute(f"SELECT * FROM login WHERE name = '{self.login}'")
        user = c.fetchall()
        if len(user) == 0:
            messagebox.showwarning(title="",message="Неверное имя пользователя")
            logging.warning(f"Someone entered uknown username:{self.login}")
            return False
        else:
            c.execute(f"SELECT * FROM login WHERE name = '{self.login}' AND password = '{self.password}'")
            record = c.fetchall()
            if len(record) == 0:
                messagebox.showerror(message="Неверный пароль")
                logging.warning(f"Someone entered wrong creds:{self.login}::{self.password}")
                return False
            else:
                callback = tkinter.Tk()
                callback.resizable(False,False)
                callback.title("Успех")
                Ans = tkinter.Label(callback,text = f"Здравствуйте,{self.login}")
                logging.warning(f"User:{self.login} successfully logged in ")
                Ans.pack()
                return True

                callback.mainloop()
        


def main():
    window = tkinter.Tk()
    window.resizable(False,False)
    window.title("Введите логин и пароль")
    window.geometry("230x100")
    name_l = tkinter.Label(text="Логин ").grid(row=0,column=0)
    name = tkinter.Entry(window).grid(row=0,column=2,columnspan=3)

    passwd_l = tkinter.Label(text="Пароль ").grid(row=1,column=0)
    passwd = tkinter.Entry(window,show="*").grid(row=1,column=2,columnspan=3)

    B = tkinter.Button(window,text="Войти",command= lambda: User(name.get(),passwd.get())).grid(row=2,column=1)
    window.mainloop()


if __name__ == "__main__":
    main()
else:
    print("This file could not be imported")
