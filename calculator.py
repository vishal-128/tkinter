# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:32:00 2021

@author: garg0
"""

from tkinter import *

root= Tk()
root.geometry("300x465")
root.title("CALCULATOR")
root.wm_iconbitmap("1.ico")

def click(event):
    global scvalue
    text= event.widget.cget("text")  # cget is use to get the text value of the button
    print(text)
    if text=="x":
        text="*"
    
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value = eval(screen.get())  # eval evaluate string
        scvalue.set(value)
        screen.upadte()    
    elif text=="C":
        scvalue.set(" ")
        screen.update()
        
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    
scvalue = StringVar()
scvalue.set("")
# entry widget

screen = Entry(root,textvar=scvalue,font="lucid 40 bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

# buttons
# we have made frame of 3 button 

f = Frame(root,bg="gray",padx=10)
b = Button(f,text="9",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()
b = Button(f,text="8",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b = Button(f,text="7",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f = Frame(root,bg="gray",padx=10)
b = Button(f,text="6",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()
b = Button(f,text="5",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b = Button(f,text="4",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f = Frame(root,bg="gray",padx=10)
b = Button(f,text="3",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()
b = Button(f,text="2",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b = Button(f,text="1",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f = Frame(root,bg="gray",padx=10)
b = Button(f,text="=",padx=8,pady=5,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()
b = Button(f,text="0",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b = Button(f,text="C",padx=8,pady=5,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f = Frame(root,bg="gray",padx=10)
b = Button(f,text="+",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=RIGHT)
b.bind("<Button-1>",click)

f.pack()
b = Button(f,text="-",padx=12,pady=5,font="lucida 25 bold")
b.pack(side=RIGHT)
b.bind("<Button-1>",click)

b = Button(f,text="x",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=RIGHT)
b.bind("<Button-1>",click)


root.mainloop()