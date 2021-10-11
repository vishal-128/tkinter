# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:32:00 2021

@author: garg0
"""

from tkinter import *

root= Tk()
root.geometry("600x400")
root.title("CALCULATOR")
root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="lucid 40 bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

f = Frame(root,bg="red")
b = Button(f,text="9",padx=10,pady=8,font="lucida 25 bold")
b.pack(side=LEFT)
f.pack()
b = Button(f,text="8",padx=10,pady=8,font="lucida 25 bold")
b.pack(side=LEFT)
b = Button(f,text="7",padx=10,pady=8,font="lucida 25 bold")
b.pack(side=LEFT)
b = Button(f,text="6",padx=10,pady=8,font="lucida 25 bold")
b.pack(side=LEFT)

root.mainloop()