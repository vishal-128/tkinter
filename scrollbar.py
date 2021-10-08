# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:09:52 2021

@author: garg0
"""

from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("scroll bar")
# for connrcting scrollbar to a widget
# 1. widget(yscrollcommand=scrollbar.set)
# 2. scrollbar.config(command=widget.yview)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

# listbox=Listbox(root, yscrollcommand = scrollbar.set)
# for i in range(30):
#     listbox.insert(END,f"{i}")
# listbox.pack(fill=BOTH)    

text= Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)
# scrollbar.config(command=listbox.yview)

root.mainloop()