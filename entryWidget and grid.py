# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:45:18 2021

@author: garg0
"""

from tkinter import *
root = Tk()
root.geometry("655x333")
def getvals():
    pass

user = Label(root, text ="username")
passward= Label(root,text="passward")
user.grid()  # .grid is use to pack, it can take two arguments row and column
passward.grid(row=1)

# variable classes in tkinter
# BooleanVar() , DoubleVar(), StringVar()

uservalue =StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable = uservalue)
passentry = Entry(root,textvariable = passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
                 
Button(text="Submit", command=getvals).grid()

root.mainloop()


