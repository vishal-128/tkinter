# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 11:10:22 2021

@author: garg0
"""

from tkinter import *
root = Tk()
# gui logic here
# Width x Height
root.geometry("444x234")
# width , height
root.minsize(200,100)
root.maxsize(1200,800)

label = Label(text="my GUI label")
label.pack()

root.mainloop()
 
