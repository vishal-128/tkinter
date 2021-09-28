# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:25:10 2021

@author: garg0
"""

from tkinter import *
root = Tk()
root.title("onece again")
root.geometry("644x344")
def harry(event):
    print(f"you have clicked on the button at {event.x},{event.y}")

widget= Button(root,text="click here")
widget.pack()

widget.bind('<Button-1>', harry)



root.mainloop()


