# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 00:08:52 2021

@author: garg0
"""

from tkinter import *
root = Tk()
root.title("MyGUI")
canvas_width = 800
canvas_height= 400

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget= Canvas(root,width = canvas_width,height = canvas_height)
can_widget.pack()

# THE LINE GOES FROM THE POINT X1,Y1 TO X2,Y2
can_widget.create_line(0,0,800,400, fill="red")
can_widget.create_line(0,400,800,0)

# TO CREATE A RECTANGLE SPECIFY PARAMETERS IN THIS ORDER -- COORDINATES OF TOP LEFT AND BOTTOM RIGHT
can_widget.create_rectangle(3,5,700,300, fill="blue")

can_widget.create_text(200,200, text="python", fill = "red")

# we give coordinate for rectange and the oval is inscribed in that rectangle
can_widget.create_oval(100,100,200,200)



root.mainloop()