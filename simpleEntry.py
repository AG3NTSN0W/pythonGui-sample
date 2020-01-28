import tkinter
from tkinter import messagebox

def statusChange(event):
    messagebox.showinfo( "Hello Python", event.char)

def entryVar(var):
    messagebox.showinfo( "Hello Python", var)

window = tkinter.Tk()
window.geometry("100x100")
entry1 = tkinter.StringVar()
L1 = tkinter.Label(window, text = "User Name")
L1.pack()
E1 = tkinter.Entry(window, bd = 5, textvariable = entry1)
E1.pack()
E1.bind("<Key>", statusChange)

B = tkinter.Button(window, text = "click me", command = lambda : entryVar(entry1.get()))
B.place(x = 0,y = 50)


window.mainloop()