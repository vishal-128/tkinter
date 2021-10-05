# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 17:18:47 2021

@author: garg0
"""

from tkinter import *
import tkinter.messagebox as msgb
root=Tk()
root.geometry("600x500")
root.title("slider")
def getdollar():
    print(f"we have credited {myslider2.get()} dollar to your bank account")
    msgb.showinfo("no of dollars",f"we have credited {myslider2.get()} dollar to your bank account")
    

# myslider= Scale(root,from_=0,to=455)
# myslider.pack()

Label(root,text="how many dollars do you wants?",font="bold",fg="green").pack()
myslider2= Scale(root,from_=0,to=100,orient=HORIZONTAL)
myslider2.set(35)
myslider2.pack()
Button(root,text="Get dollar",command=getdollar).pack()


root.mainloop()