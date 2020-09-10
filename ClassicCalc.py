from tkinter import *
from tkinter import messagebox

def check():
    math = txt.get()
    if math == "":
        messagebox.showerror("Error", "No text in label!")
    else:
        lbl2.configure(text=str(eval(math)))
    
window = Tk()
window.title("Calculator by VladimirPapazov88")
window.geometry('1500x100')

lbl = Label(window, text="Classic calculator! Enter a mathematical expression and click the '=' button: ", font=("Arial", 24))
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="", font=("Arial", 24), fg="Blue")
lbl2.grid(column=4, row=0)

txt = Entry(window, width=17, font=("Arial", 24), fg="Green")
txt.grid(column=1, row=0)

btn = Button(window, text="=", font=("Arial", 24), command=check)
btn.grid(column=3, row=0)

a = input("Type q to exit\n")
