import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.geometry("100x100")

def helloCallBack():
    messagebox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(window, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
window.mainloop()