import tkinter
from tkinter import messagebox

                 
def statusChange():
    messagebox.showinfo( "Hello Python", "Hello World")

def statusChangeWithParams(param1):
    if param1 == 1:
        messagebox.showinfo( "Hello Python", "checkBox is checked")    
        pass
    else:
        messagebox.showinfo( "Hello Python", "checkBox is not longer checked")    
        pass

    
top = tkinter.Tk()
CheckVar1 = tkinter.IntVar()
CheckVar2 = tkinter.IntVar()
C1 = tkinter.Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20, command = statusChange)

C2 = tkinter.Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20, command = lambda : statusChangeWithParams(CheckVar2.get()))

C1.pack()
C2.pack()
top.mainloop()