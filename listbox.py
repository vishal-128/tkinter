# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:37:41 2021

@author: garg0
"""

from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("list box")
def add():
    global i
    lbx.insert(END, f"{i}")
    i+=1
i=0 
lbx= Listbox(root,width=80,height=10)
lbx.pack()
# lbx.insert(index,"content")
lbx.insert(ACTIVE,"item of list box")
lbx.insert(1,"python")
lbx.insert(2,"php")

Button(root, text="add item",command=add).pack()



root.mainloop()