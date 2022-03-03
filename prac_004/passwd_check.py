

import tkinter
from tkinter import messagebox
window = tkinter.Tk()
window.resizable(False,False)
window.title("Введите логин и пароль")
window.geometry("400x400")
name_l = tkinter.Label(text="Логин ").grid(row=0,column=0)
name = tkinter.Entry(window)
name.grid(row=0,column=2,columnspan=3)

passwd_l = tkinter.Label(text="Пароль ").grid(row=1,column=0)
passwd = tkinter.Entry(window,show="*")
passwd.grid(row=1,column=2,columnspan=3)
class Connection:
	def __init__(self,name,password):
		self.name = name
		self.password = password
	def Auth(self):
		login = self.name
		password = self.password

		import mysql.connector as conn
		try:
			mydb=conn.connect(host='127.0.0.1',database='new',user='root',password='')
			c = mydb.cursor()
		except Exception as e:
			messagebox.showerror(message=e)

		c.execute(f"SELECT * FROM user WHERE name = '{login}'")
		user = c.fetchall()
		print(user)
		if len(user) == 0:
			messagebox.showwarning(title="",message="Неверное имя пользователя")
		else:
			c.execute(f"SELECT * FROM user WHERE name = '{login}' AND password = '{password}'")
			record = c.fetchall()
			if len(record) == 0:
				messagebox.showerror(message="Неверный пароль")
			else:
				callback = tkinter.Tk()
				callback.resizable(False,False)
				callback.title("Успех")
				Ans = tkinter.Label(text = f"Здравствуйте,{login}")
				callback.mainloop()
user = Connection(name.get(),passwd.get())

B = tkinter.Button(window,text="Войти",command=user.Auth).grid(row=2,column=1)
window.mainloop()
