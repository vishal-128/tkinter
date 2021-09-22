# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:43:03 2021

@author: garg0
"""

from tkinter import *
root = Tk()
root.geometry("655x355")
frame = Frame(root,bg="grey",borderwidth=3,relief =SUNKEN)
frame.pack(side=LEFT,anchor = "nw")

def hello():
    print("hello tkinter")

def name():
    print("vishal garg")
    
b1 = Button(frame,fg= "red",text="print", command = hello) # command can be use to call function on clicking the res. button
b1.pack(side=LEFT,padx=5) #padx gives space between button in x coordinates

b2 = Button(frame,fg= "red",text="print", command=name)
b2.pack(side=LEFT,padx=5)

b3 = Button(frame,fg= "red",text="print")
b3.pack(side=LEFT,padx=5)

b4 = Button(frame,fg= "red",text="print")
b4.pack(side=LEFT,padx=5)




root.mainloop()