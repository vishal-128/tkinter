# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:42:48 2021

@author: garg0
"""

from tkinter import *


# in a class root is rreplaced AS self
# outside class root is represented as window
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")
    
    def click(self):
        print("button click")
        
    def button(self,inputtext):
        Button(text=inputtext,command=self.click).pack()
        
if __name__=='__main__':
    window = GUI()
    window.button("hello")
    window.mainloop()        
