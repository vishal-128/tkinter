# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:32:00 2021

@author: garg0
"""

from tkinter import *

root= Tk()
root.resizable(width=False, height=False)
root.geometry("530x620+450+20")
root.title("CALCULATOR")
root.wm_iconbitmap("1.ico")
f = Frame(root,bg="white")
f.grid()

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


label = Label(f,text="ADVANCED OPTIONS",font="lucid 25 bold")
label.grid(row=0,column=5,padx=18)   

# entry widget

screen = Entry(f,textvar=scvalue,font="lucid 40 bold",width=18)
screen.grid(row=0,column=0,columnspan=4,pady=1)

# buttons
# we have made frame of 3 button 

# f = Frame(root,bg="gray",padx=5)
b = Button(f,text="9",bg='black',fg='white',width=6, height=2,font="lucida 25 bold")
b.grid(row=1,column=0)
b.bind("<Button-1>",click)

b = Button(f,text="8",width=6, height=2,font="lucida 25 bold")
b.grid(row=1,column=1)
b.bind("<Button-1>",click)

b = Button(f,text="7",width=6, height=2,font="lucida 25 bold")
b.grid(row=1,column=2)
b.bind("<Button-1>",click)
#f.grid()

#f = Frame(root,bg="gray",padx=5)
b = Button(f,text="6",width=6, height=2,font="lucida 25 bold")
b.grid(row=2,column=0)
b.bind("<Button-1>",click)

b = Button(f,text="5",width=6, height=2,font="lucida 25 bold")
b.grid(row=2,column=1)
b.bind("<Button-1>",click)

b = Button(f,text="4",width=6, height=2,font="lucida 25 bold")
b.grid(row=2,column=2)
b.bind("<Button-1>",click)
#f.grid()

#f = Frame(root,bg="gray",padx=5)
b = Button(f,text="3",width=6, height=2,font="lucida 25 bold")
b.grid(row=3,column=0)
b.bind("<Button-1>",click)

b = Button(f,text="2",width=6, height=2,font="lucida 25 bold")
b.grid(row=3,column=1)
b.bind("<Button-1>",click)

b = Button(f,text="1",width=6, height=2,font="lucida 25 bold")
b.grid(row=3,column=2)
b.bind("<Button-1>",click)
#f.grid()

#f = Frame(root,bg="gray",padx=5)
b = Button(f,text="=",width=6, height=2,font="lucida 25 bold")
b.grid(row=4,column=0)
b.bind("<Button-1>",click)


b = Button(f,text="0",width=6, height=2,font="lucida 25 bold")
b.grid(row=4,column=1)
b.bind("<Button-1>",click)

b = Button(f,text="C",bg='powder blue',width=6, height=2,font="lucida 25 bold")
b.grid(row=4,column=2)
b.bind("<Button-1>",click)
#f.grid()

#f = Frame(root,bg="gray",padx=5)
b = Button(f,text="+",width=6, height=2,font="lucida 25 bold")
b.grid(row=5,column=0)
b.bind("<Button-1>",click)

b = Button(f,text="-",width=6, height=2,font="lucida 25 bold")
b.grid(row=5,column=1)
b.bind("<Button-1>",click)

b = Button(f,text="x",width=6, height=2,font="lucida 25 bold")
b.grid(row=5,column=2)
b.bind("<Button-1>",click)
#f.grid()

#f = Frame(root,bg="gray",padx=5)
b = Button(f,text="/",width=6, height=2,font="lucida 25 bold")
b.grid(row=1,column=3)
b.bind("<Button-1>",click)

b = Button(f,text=".",width=6, height=2,font="lucida 25 bold")
b.grid(row=2,column=3)
b.bind("<Button-1>",click)

b = Button(f,text="%",width=6, height=2,font="lucida 25 bold")
b.grid(row=3,column=3)
b.bind("<Button-1>",click)

#f.grid()
b = Button(f,text="(",width=6, height=2,font="lucida 25 bold")
b.grid(row=4,column=3)
b.bind("<Button-1>",click)

b = Button(f,text=")",width=6, height=2,font="lucida 25 bold")
b.grid(row=5,column=3)
b.bind("<Button-1>",click)
# menubar for advance setting
def Scientific():
	root.resizable(width=False, height=False)
	root.geometry("944x740+0+0")
 

yourmenubar= Menu(root)
m1=Menu(yourmenubar, tearoff=0) # there was a horizontal line in menue for a diff purpose if u dont want that than we use tearoff
m1.add_command(label="advance", command=Scientific)
root.config(menu=yourmenubar)
yourmenubar.add_cascade(label="file", menu=m1)



root.mainloop()