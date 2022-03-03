from tkinter import *


def clicked():
    res = "Hi{}".messagebox+name.get() + surname.get()
    lbl.configure(text=res)


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
lbl = Label(window, text="Приветsdf")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt = Entry(window, width=10)
txt.grid(column=2, row=0)
name = StringVar()
surname = StringVar()
name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
name_entry.grid(row=3, column=1, padx=5, pady=5)
surname_entry.grid(row=4, column=1, padx=5, pady=5)

btn = Button(window, text="Клик!", command=clicked)
btn.grid(column=5, row=5)
window.mainloop()


