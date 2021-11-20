# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:32:00 2021

@author: garg0
"""

from tkinter import *

root= Tk()
root.geometry("440x740+450+90")
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
b = Button(f,text="9",bg='black',fg='white',width=6, height=2,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b = Button(f,text="8",width=6, height=2,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b = Button(f,text="7",width=6, height=2,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="gray",padx=10)
b = Button(f,text="6",width=6, height=2,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b = Button(f,text="5",width=6, height=2,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b = Button(f,text="4",width=6, height=2,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="gray",padx=10)
b = Button(f,text="3",width=6, height=2,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b = Button(f,text="2",width=6, height=2,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b = Button(f,text="1",width=6, height=2,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="gray",padx=10)
b = Button(f,text="=",width=6, height=2,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)


b = Button(f,text="0",width=6, height=2,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b = Button(f,text="C",bg='powder blue',width=6, height=2,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="gray",padx=10)
b = Button(f,text="+",width=6, height=2,font="lucida 25 bold")
b.pack(side=RIGHT)
b.bind("<Button-1>",click)

b = Button(f,text="-",width=6, height=2,font="lucida 25 bold")
b.pack(side=RIGHT)
b.bind("<Button-1>",click)

b = Button(f,text="x",width=6, height=2,font="lucida 25 bold")
b.pack(side=RIGHT)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="gray",padx=10)
b = Button(f,text="/",width=6, height=2,font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b = Button(f,text=".",width=6, height=2,font="lucida 25 bold")
b.pack(side=RIGHT)
b.bind("<Button-1>",click)

b = Button(f,text="%",width=6, height=2,font="lucida 25 bold")
b.pack(side=RIGHT)
b.bind("<Button-1>",click)
f.pack()

# menubar for advance setting
def Scientific():
	root.resizable(width=False, height=False)
	root.geometry("944x740+0+0")
    
yourmenubar= Menu(root)
m1=Menu(yourmenubar, tearoff=0) # there was a horizontal line in menue for a diff purpose if u dont want that than we use tearoff
m1.add_command(label="advance", command=Scientific)
root.config(menu=yourmenubar)
yourmenubar.add_cascade(label="file", menu=m1)

label = Label(text="my GUI label")
label.pack(side=RIGHT)

root.mainloop()