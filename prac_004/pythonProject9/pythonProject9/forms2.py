#future
from tkinter import *
def auth():
    sa=name.get()+ " " + surname.get()
    window1 = Tk()
    window1.title("Окно 2")
    window1.geometry('800x600')
    lbl1 = Label(window1, text=sa)
    lbl1.grid(column=0, row=0)
    window1.mainloop()


root = Tk()
root.geometry("300x300")
root.title("Форма 1")

surname = StringVar()

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")
name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=2, column=0, sticky="w")
surname_entry = Entry(textvariable=surname)
name = StringVar()
name_entry = Entry(textvariable=name)
name_entry.grid(row=1, column=1, padx=5, pady=5)
surname_entry.grid(row=2, column=1, padx=5, pady=5)
message_button = Button(text="Авторизация", command=auth)
message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

root.mainloop()