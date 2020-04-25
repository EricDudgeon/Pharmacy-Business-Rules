# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 20:53:27 2020

@author: Eric Dudgeon
"""

from tkinter import *
import pandas as pd



def openOP():
    OP = Toplevel()
    OP.title("Outpatient Business Rules")
    OP.iconbitmap("icon.ico")
    
def openIP():
    IP = Toplevel()
    IP.title("Inpatient Business Rules")
    IP.iconbitmap("icon.ico")
    
def openUpdate():
    update = Toplevel()
    update.title("Updating Business Rules")
    update.iconbitmap("icon.ico")
            
### CREATING MAIN WINDOW ###
        
root = Tk()
root.title("Federal Business Rules")
root.geometry('200x100+100+100')
root.iconbitmap("icon.ico")

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

topframe = Frame(root)
topframe.pack( side = TOP )

label1 = Label(topframe, text = "Federal Pharmacy Business Rules")
label1.pack(side=TOP)

OPButton = Button(topframe, text="Outpatient", command=openOP)
OPButton.pack(side=LEFT)
        
IPButton = Button(topframe, text="Inpatient", command=openIP)
IPButton.pack(side=RIGHT)

quitButton = Button(bottomframe, text="Quit", command=root.destroy)
quitButton.pack(side=RIGHT)

updateButton = Button(bottomframe, text="Update", command=openUpdate)
updateButton.pack(side=LEFT)


root.mainloop()