try:
    import tkinter
    from tkinter import messagebox
    import mysql.connector as conn
    import os
    import configparser
    import logging
    import re
except ImportError as e:
    os.command(f"pip install {e.split()[-1]}")

users = []
CONFIG_FILE = "config.ini"

logging.basicConfig(filename='access.log')
logging.basicConfig(format='%(asctime)s %(message)s')


class NotSuitadbleData(Exception):

    def __init__(self, message):
        self.message = message


try:
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    host = config.get("DEFAULT", "host")
    dbname = config.get("DEFAULT", "dbname")
    login = config.get("DEFAULT", "login")
    password = config.get("DEFAULT", "password")

except Exception:
    print("Error reading configuration file")


class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        if self.Auth():
            self.customer_data = self.Fetch()

    def Fetch(self) -> list:
        try:
            mydb = conn.connect(host=host,
                                database=dbname,
                                user=login,
                                password=password)
            c = mydb.cursor()
        except Exception as e:
            messagebox.showerror(message=e)
        c.execute(
            f"SELECT * FROM login WHERE name = '{self.login}' AND password = '{self.password}'"
        )
        data = c.fetchall()
        id_ = int(data[0][0])
        c.execute(f"SELECT * FROM user_data WHERE user_id = {id_}")
        data = c.fetchall()
        surname = data[0][1]
        name = data[0][2]
        secondname = data[0][3]
        birth_date = data[0][4]
        email = data[0][5]
        phone = data[0][6]
        global users
        data = [
            id_, self.login, self.password, surname, name, secondname,
            birth_date, email, phone
        ]
        logging.warning(
            f"successfully fetched data:{id_},{self.login},{self.password},{surname},{name},{secondname},{birth_date},{email},{phone}"
        )
        users.append(data)
        #print(users[-1])
        return data

    def Auth(self) -> bool:
        try:
            mydb = conn.connect(host=host,
                                database=dbname,
                                user=login,
                                password=password)
            c = mydb.cursor()
        except Exception as e:
            messagebox.showerror(message=e)

        c.execute(f"SELECT * FROM login WHERE name = '{self.login}'")
        user = c.fetchall()
        if len(user) == 0:
            messagebox.showwarning(title="",
                                   message="Неверное имя пользователя")
            logging.warning(f"Someone entered uknown username:{self.login}")
            return False
        else:
            c.execute(
                f"SELECT * FROM login WHERE name = '{self.login}' AND password = '{self.password}'"
            )
            record = c.fetchall()
            if len(record) == 0:
                messagebox.showerror(message="Неверный пароль")
                logging.warning(
                    f"Someone entered wrong creds:{self.login}::{self.password}"
                )
                return False
            else:
                callback = tkinter.Tk()
                callback.resizable(False, False)
                callback.title("Успех")
                callback.geometry("500x500")
                Ans = tkinter.Label(callback,
                                    text=f"Здравствуйте,{self.login}").grid(
                                        row=0, column=0, columnspan=3)
                ed = tkinter.Button(callback,
                                    text="Edit profile",
                                    command=lambda: self.EditGUI()).grid(
                                        row=1, column=0)
                logging.warning(f"User:{self.login} successfully logged in ")
                return True

                callback.mainloop()

    def NewPasswd(self, id_, old, new, repeat):
        try:
            if (old != new) and (new == repeat) and (len(new) <= 20):
                mydb = conn.connect(host=host,
                                    database=dbname,
                                    user=login,
                                    password=password)
                c = mydb.cursor()
                c.execute(
                    f"UPDATE login SET password = '{new}' WHERE id = {id_}")
                logging.warning(
                    f"password on {id_} changed from {old} to {new}")
            else:
                raise NotSuitadbleData("Passord is not suitable")
        except Exception as e:
            messagebox.showerror(message=e)

    def Checker(self, old, new):
        try:
            if (old != new) and (len(new) < 20):
                return True
            else:
                raise NotSuitadbleData(f"{new} is not not suitable")
        except Exception as e:
            messagebox.showerror(message=e)

    def EmailValidator(self, email):
        try:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if (re.fullmatch(regex, email)) and (len(email) < 30):
                return True
            else:
                raise NotSuitadbleData("Enter valid email")
        except Exception as e:
            messagebox.showerror(message=e)

    def PhoneValidator(self, phone):
        try:
            regex = r'/\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/'
            if (len(phone) <= 20):
                return True
            else:
                raise NotSuitadbleData("Enter valid phone")
        except Exception as e:
            messagebox.showerror(message=e)

    def DateValidator(self, date):
        try:
            regex = r'^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$'
            if (re.fullmatch(regex, date)):
                return True
            else:
                raise NotSuitadbleData("Enter valid date")
        except Exception as e:
            messagebox.showerror(message=e)

    def SubmitChanges(
        self, old, new
    ):  ## [id_,self.login,self.password,surname,name,secondname,birth_date,email,phone]
        try:
            mydb = conn.connect(host=host,
                                database=dbname,
                                user=login,
                                password=password)
            c = mydb.cursor()
        except Exception as e:
            messagebox.showerror(message=e)
        id_ = old[0]
        for idx in range(0, len(old)):
            if str(new[idx]) != str(old[idx]):
                if idx == 1:
                    #print(f"1 \t {old[idx]}\t{new[idx]}")
                    if self.Checker(old[idx], new[idx]):
                        c.execute(
                            f"UPDATE login SET name = '{str(new[idx])}' WHERE id = {id_}"
                        )
                        mydb.commit()
                        logging.warning(
                            f"Some data changed on {id_}  from {old} to {new}")
                elif idx == 3:
                    #print(f"3 \t {old[idx]}\t{new[idx]}")
                    if self.Checker(old[idx], new[idx]):
                        c.execute(
                            f"UPDATE user_data set surname = '{str(new[idx])}' WHERE user_id = {id_}"
                        )
                        mydb.commit()
                        logging.warning(
                            f"Some data changed on {id_}  from {old} to {new}")
                elif idx == 4:
                    #print(f"4 \t {old[idx]}\t{new[idx]}")
                    if self.Checker(old[idx], new[idx]):
                        c.execute(
                            f"UPDATE user_data set name = '{str(new[idx])}' WHERE user_id = {id_}"
                        )
                        mydb.commit()
                        logging.warning(
                            f"Some data changed on {id_}  from {old} to {new}")
                elif idx == 5:
                    #print(f"5 \t {old[idx]}\t{new[idx]}")
                    if self.Checker(old[idx], new[idx]):
                        c.execute(
                            f"UPDATE user_data set secondname = '{str(new[idx])}' WHERE user_id = {id_}"
                        )
                        mydb.commit()
                        logging.warning(
                            f"Some data changed on {id_}  from {old} to {new}")
                elif idx == 6:
                    #print(f"6 \t {old[idx]}\t{new[idx]}")
                    if self.DateValidator(new[idx]):
                        c.execute(
                            f"UPDATE user_data set birth_date = '{str(new[idx])}' WHERE user_id = {id_}"
                        )
                        mydb.commit()
                        logging.warning(
                            f"Some data changed on {id_}  from {old} to {new}")
                elif idx == 7:
                    #print(f"7 \t {old[idx]}\t{new[idx]}")
                    if self.EmailValidator(new[idx]):
                        c.execute(
                            f"UPDATE user_data set email = '{str(new[idx])}' WHERE user_id = {id_}"
                        )
                        mydb.commit()
                        logging.warning(
                            f"Some data changed on {id_}  from {old} to {new}")
                elif idx == 8:
                    #print(f"8 \t {old[idx]}\t{new[idx]}")
                    if self.PhoneValidator(new[idx]):
                        c.execute(
                            f"UPDATE user_data set telephone = '{str(new[idx])}' WHERE user_id = {id_}"
                        )
                        mydb.commit()
                        logging.warning(
                            f"Some data changed on {id_}  from {old} to {new}")
            else:
                idx += 1

    def EditGUI(self):
        GUI = tkinter.Tk()
        GUI.resizable(False, False)
        GUI.title("Изменить настройки профиля")
        GUI.geometry("500x1000")

        login_l = tkinter.Label(GUI, text="Логин ").grid(row=0, column=0)
        login = tkinter.Entry(GUI)
        login.grid(row=0, column=2, columnspan=3)

        passwd_l = tkinter.Label(GUI, text="Пароль текущий:").grid(row=1,
                                                                   column=0)
        passwd_l_N = tkinter.Label(GUI, text="Пароль Новый:").grid(row=2,
                                                                   column=0)
        passwd_l_N_R = tkinter.Label(GUI, text="Повторите новый пароль").grid(
            row=3, column=0)

        passwd = tkinter.Entry(GUI, show="*")
        passwd.grid(row=1, column=2, columnspan=3)

        passwd_N = tkinter.Entry(GUI, show="*")
        passwd_N.grid(row=2, column=2, columnspan=3)

        passwd_N_R = tkinter.Entry(GUI, show="*")
        passwd_N_R.grid(row=3, column=2, columnspan=3)

        name_l = tkinter.Label(GUI, text="Имя ").grid(row=4, column=0)
        name = tkinter.Entry(GUI)
        name.grid(row=4, column=2, columnspan=3)

        surname_l = tkinter.Label(GUI, text="Фамилия").grid(row=5, column=0)
        surname = tkinter.Entry(GUI)
        surname.grid(row=5, column=2, columnspan=3)

        secondname_l = tkinter.Label(GUI, text="Отчество").grid(row=6,
                                                                column=0)
        secondname = tkinter.Entry(GUI)
        secondname.grid(row=6, column=2, columnspan=3)

        date_l = tkinter.Label(GUI, text="Дата рождения").grid(row=7, column=0)
        date = tkinter.Entry(GUI)
        date.grid(row=7, column=2, columnspan=3)

        email_l = tkinter.Label(GUI, text="Email ").grid(row=8, column=0)
        email = tkinter.Entry(GUI)
        email.grid(row=8, column=2, columnspan=3)

        phone_l = tkinter.Label(GUI, text="Телефон ").grid(row=9, column=0)
        phone = tkinter.Entry(GUI)
        phone.grid(row=9, column=2, columnspan=3)
        B = tkinter.Button(GUI,
                           text="Apply",
                           command=lambda: self.SubmitChanges(
                               data, [data[0]] + [x.get() for x in form])
                           if (len(passwd_N.get()) == 0) else
                           (self.NewPasswd(data[0], passwd.get(), passwd_N.get(
                           ), passwd_N_R.get()))).grid(row=10, column=1)
        data = self.Fetch()
        form = [login, passwd, surname, name, secondname, date, email, phone]
        for i in range(0, len(data)):
            #print(i)
            if i == 0:
                continue
            else:
                form[i - 1].insert(0, str(data[i]))
        GUI.mainloop()


def main():
    window = tkinter.Tk()
    window.resizable(False, False)
    window.title("Введите логин и пароль")
    window.geometry("230x100")
    name_l = tkinter.Label(text="Логин ").grid(row=0, column=0)
    name = tkinter.Entry(window)
    name.grid(row=0, column=2, columnspan=3)

    passwd_l = tkinter.Label(text="Пароль ").grid(row=1, column=0)
    passwd = tkinter.Entry(window, show="*")
    passwd.grid(row=1, column=2, columnspan=3)

    B = tkinter.Button(window,
                       text="Войти",
                       command=lambda: User(name.get(), passwd.get())).grid(
                           row=2, column=1)
    window.mainloop()


if __name__ == "__main__":
    main()
else:
    print("This file could not be imported")
