# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 20:24:44 2021

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
Label(root,text="what would you like to have",font="lucida 19 bold",justify=LEFT,padx=14,fg="blue").pack()

radio = Radiobutton(root, text="Dosa",padx=14,variable=var, value=1).pack(anchor="w") # must be n, ne, e, se, s, sw, w, nw, or center
radio = Radiobutton(root, text="idly",padx=14,variable=var, value=2).pack(anchor="w")
radio = Radiobutton(root, text="upma",padx=14,variable=var, value=3).pack(anchor="w")
radio = Radiobutton(root, text="bada",padx=14,variable=var, value=4).pack(anchor="w")
radio = Radiobutton(root, text="aloo chop",padx=14,variable=var, value=5).pack(anchor="w")

Button(root,text="order",command=Order).pack()


root.mainloop()
