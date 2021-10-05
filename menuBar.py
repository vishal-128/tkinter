# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 12:15:50 2021

@author: garg0
"""

from tkinter import *
import tkinter.messagebox as msgb
root = Tk()
root.geometry("400x400")
root.title("menue")

def myfunc():
    print("hello")

def helpkaro():
    print("help him")
    a= msgb.showinfo("HELP","i will be helping you")
    
def ask():
    print("how are you...good?")
    value=msgb.askquestion("condition","are you felling good?")  
    print(value)
    if value=="yes":
        msg=":) glad to hear it"
    else:
        msg="is there something i can do to make you fell better?"    
    msgb.showinfo("check",msg)

def retry():
    ans=msgb.askretrycancel("padh lo","not able to understand the topic")
    if ans:
        print("revise the topic again and again ")
    else:
        print("tera kuch nahi ho sakta")
# no dropdown menue    
# mymenue= Menu(root)
# mymenue.add_command(label="File", command=myfunc)
# mymenue.add_command(label="Exit", command=quit)
# pack
# root.config(menu=mymenue)

yourmenubar= Menu(root)
m1=Menu(yourmenubar, tearoff=0) # there was a horizontal line in menue for a diff purpose if u dont want that than we use tearoff
m1.add_command(label="new", command=myfunc)
m1.add_command(label="save", command=myfunc)
m1.add_separator() # make a simple horizontal line seprating menu
m1.add_command(label="print", command=myfunc)
root.config(menu=yourmenubar)
yourmenubar.add_cascade(label="file", menu=m1)




m2=Menu(yourmenubar) # there was a horizontal line in menue for a diff purpose if u dont want that than we use tearoff
m2.add_command(label="copy", command=myfunc)
m2.add_command(label="paste", command=myfunc)

m2.add_separator() # make a simple horizontal line seprating menu opt

m2.add_command(label="find", command=myfunc)
root.config(menu=yourmenubar)
yourmenubar.add_cascade(label="edit", menu=m2)


m3=Menu(yourmenubar,tearoff=0)
m3.add_command(label="help",command=helpkaro)
m3.add_command(label="status",command=ask)
m3.add_command(label="study",command=retry)
root.config(menu=yourmenubar)
yourmenubar.add_cascade(label="source",menu=m3)




root.mainloop()