# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 21:02:39 2021

@author: garg0
"""

from tkinter import *
root = Tk()
root.geometry("644x344")

def getvals():
    pass
Label(root, text="welcome to vishal travells", font='comicsansns 13 bold',pady=15).grid(row=0,column=3)
name = Label(root,text="name")
phone = Label(root,text="phone no.")
gender = Label(root,text="gender")
payment_mode = Label(root,text="payment mode")
emergency = Label(root,text="emergency contact")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
payment_mode.grid(row=4,column=2)
emergency.grid(row=5,column=2)

namevalue=StringVar()
gendervalue=StringVar()
phonevalue=StringVar()
payment_modevalue=StringVar()
emergencyvalue=StringVar()
foodservicevalue=IntVar() #checkbox

nameentry=Entry(root, textvariable=namevalue)
phoneentry=Entry(root, textvariable=phonevalue)
genderentry=Entry(root, textvariable=gendervalue)
paymententry=Entry(root, textvariable=payment_modevalue)
emergencyentry=Entry(root, textvariable=emergencyvalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
paymententry.grid(row=4,column=3)
emergencyentry.grid(row=5,column=3)

# checkbox
foodservice=Checkbutton(text="want to prebook the meal",variable=foodservicevalue)
foodservice.grid(row=6,column=3)


Button(text="Submit", command=getvals).grid(row=7,column=3)


root.mainloop()