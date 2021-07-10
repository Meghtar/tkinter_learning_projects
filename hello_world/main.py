from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("300x300")
root.title("Hello world app")

label = Label(root, text="Hello, world")
label.grid(column=0, row=0)

textField = Entry(root, width=20)
textField.grid(column=1, row=0)


def button_clicked():
    messagebox.showinfo(title="This is message box", message=textField.get())


btn = Button(root, text="Show message!", command=button_clicked)
btn.grid(column=1, row=1)

root.mainloop()
