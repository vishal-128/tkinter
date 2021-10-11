# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:11:59 2021

@author: garg0
"""

from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("Title of the gui ")
root.wm_iconbitmap("1.ico")
root.config(bg="red")
width = root.winfo_screenmmwidth()
height= root.winfo_screenheight()
print(f"{width}x{height}")
Button(text="close", command=root.destroy).pack()

root.mainloop()