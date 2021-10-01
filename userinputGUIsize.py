# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:31:59 2021

@author: garg0
"""

from tkinter import *
root = Tk()
root.geometry("600x500")
def window():
    
    root.geometry(f"{xvalue.get()}x{yvalue.get()}")
    print(xvalue.get()+"x"+yvalue.get())
   

x = Label(root, text ="height")
y= Label(root,text="width")
x.grid()
y.grid(row=1)
xvalue =StringVar()
yvalue = StringVar()

xentry = Entry(root,textvariable = xvalue)
yentry = Entry(root,textvariable = yvalue)
xentry.grid(row=0,column=2)
yentry.grid(row=1,column=2)
Button(text="apply", command=window).grid(row=3,column=2)




root.mainloop()
