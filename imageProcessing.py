# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 20:33:41 2021

@author: garg0
"""

from tkinter import *
from PIL import Image, ImageTk # use for format other than png
root = Tk()
# width x height
root.geometry("455x244")
# =============================================================================
# for png image 

# photo = PhotoImage(file="1.png")
# label = Label(image=photo)
# label.pack()  
# =============================================================================

# FOR JPG IMAGES


photo = ImageTk.PhotoImage(file="1.jpg")

label = Label(image=photo)
label.pack()
root.mainloop()
