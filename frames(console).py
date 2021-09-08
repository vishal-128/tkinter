# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 22:15:25 2021

@author: garg0
"""

from tkinter import *
root = Tk()
root.geometry("655x333")
f1=Frame(root,bg="grey", borderwidth =3, relief = SUNKEN)
f1.pack(side=LEFT, fill="y")

f2=Frame(root,bg="grey", borderwidth =3, relief = SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1,text="project tkinter")
l.pack(pady=142) # pady = position in y in the frame

l = Label(f2,text="welcome here", font="bold", fg ="red")
l.pack()

root.mainloop()