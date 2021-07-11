from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("300x300")
root.title("Calculator")

number1TextField = Entry(root, width=20)
number1TextField.grid(column=0, row=0)

operationsFrame = LabelFrame(root, text="Choose operation")

operation = StringVar()

sumRadioButton = Radiobutton(operationsFrame, text="+", variable=operation, value="+")
sumRadioButton.grid(column=0, row=1)
sumRadioButton.select()

substractionRadioButton = Radiobutton(operationsFrame, text="-", variable=operation, value="-")
substractionRadioButton.grid(column=1, row=1)
substractionRadioButton.deselect()

multiplicationRadioButton = Radiobutton(operationsFrame, text="*", variable=operation, value="*")
multiplicationRadioButton.grid(column=2, row=1)
multiplicationRadioButton.deselect()

divisionRadioButton = Radiobutton(operationsFrame, text="/", variable=operation, value="/")
divisionRadioButton.grid(column=3, row=1)
divisionRadioButton.deselect()

operationsFrame.grid(column=0, row=1)

number2TextField = Entry(root, width=20)
number2TextField.grid(column=0, row=2)


def calculate():
    if number1TextField.get() == "" or number2TextField.get() == "":
        messagebox.showerror(title="Error", message="Number not entered")
        return
    number1 = float(number1TextField.get())
    number2 = float(number2TextField.get())
    calculation = operation.get()
    if calculation == "+":
        result = number1 + number2
    elif calculation == "-":
        result = number1 - number2
    elif calculation == "*":
        result = number1 * number2
    elif calculation == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            messagebox.showerror(title="Error", message="Cannot divide by 0")
            return
    else:
        messagebox.showerror(title="Error", message="Operation not chosen") # This should not happen
        return
    resultTextField.config(state=NORMAL)
    resultTextField.delete('1.0', END)
    resultTextField.insert(INSERT, str(result))
    resultTextField.config(state=DISABLED)


btn = Button(root, text="=", command=calculate, width=5)
btn.grid(column=0, row=3)

resultTextField = Text(root, width=20, height=1)
resultTextField.config(state=DISABLED)
resultTextField.grid(column=0, row=4)


root.mainloop()
