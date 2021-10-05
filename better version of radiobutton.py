# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:09:35 2021

@author: garg0
"""

from tkinter import *
root=Tk()
root.geometry("600x500")
root.title("radio type button")
def Order():
    d=" "
    if (var.get()==1):
        d="dosa"
    print(f"your order is {d} .THANKS FOR YOUR ORDER ")

var=IntVar()
# var.set(1)
Label(root,text="what would you like to have",font="lucida 19 bold",justify=LEFT,padx=35,fg="blue").grid(row=1,column=4)

radio = Radiobutton(root, text="Dosa",padx=0,variable=var, value=1).grid(row=3,column=0,sticky="w") # must be n, ne, e, se, s, sw, w, nw, or center
radio = Radiobutton(root, text="idly",padx=0,variable=var, value=2).grid(row=4,column=0,sticky='w')
radio = Radiobutton(root, text="upma",padx=0,variable=var, value=3).grid(row=5,column=0,sticky='w')
radio = Radiobutton(root, text="bada",padx=0,variable=var, value=4).grid(row=6,column=0,sticky='w')
radio = Radiobutton(root, text="aloo chop",padx=0,variable=var, value=5).grid(row=7,column=0,sticky='w')

Button(root,text="order",command=Order).grid(row=8,column=0,pady=10)


root.mainloop()