# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 20:53:27 2020

@author: Eric Dudgeon
"""

from tkinter import *
from tkinter import ttk
import pandas as pd
import sqlite3
data = pd.read_csv("Business Rules File.csv")
dosage_forms = data["Dosage_Form"].astype("string").to_list()

def openOP():
    OP = Toplevel()
    OP.title("Outpatient Business Rules")
    OP.iconbitmap("icon.ico")
    OP.geometry('{}x{}'.format(500, 600))
    
    # create all of the OP containers
    top_frame = Frame(OP, pady=10, padx=3)
    center = Frame(OP, padx=3, pady=3)
    btm_frame = Frame(OP, pady=3)
    btm_frame2 = Frame(OP, pady=3)
    
    # layout all of the OP containers
    # OP.grid_rowconfigure(1, weight=1)
    # OP.grid_columnconfigure(0, weight=1)
    
    top_frame.grid(row=0,sticky=N+E+S+W)
    center.grid(row=1, sticky=E+W)
    btm_frame.grid(row=2)
    btm_frame2.grid(row=3)
    
    ## Adding OP Back Button
    OPmenu = Menu(OP)
    OP.config(menu=OPmenu)
    OPsubMenu = Menu(menu)
    OPmenu.add_cascade(label = "File", menu=OPsubMenu)
    OPsubMenu.add_command(label="View All")
    OPsubMenu.add_separator()
    OPsubMenu.add_command(label="Back", command=OP.destroy)
    

    #Scroll Dropdown
    OP_button = ttk.Combobox(top_frame, value=dosage_forms)
    OP_button.grid(row=0, column=0,padx=10, pady=10,sticky=W)
    OP_button.current(0)
    
    
    
    
    ## Adding labels to OP Left
    OP_form_label = Label(top_frame,text="Dosage Form:").grid(row=1, column = 0, sticky=W, pady=10)
    OP_form_abbrev_label = Label(top_frame,text="Dosage Form Abbrev").grid(row=2, column=0, sticky=W,pady=10)
    OP_sig_label = Label(top_frame,text="SIG Tool").grid(row=3, column=0, sticky=W,pady=10)
    
    ## Aligned format
    space= Label(top_frame,text="").grid(row=0,column=1,padx=25)
    space1= Label(top_frame,text="").grid(row=1,column=1,padx=25)
    space3= Label(top_frame, text="").grid(row=2,column=1, padx=6)
    space3= Label(top_frame, text="").grid(row=3,column=1, padx=20)
    
    ##Adding Labels to OP Right
    OPlabel = Label(top_frame,text="Outpatient Pharmacy Business Rules")
    OPlabel.grid(row=0, column=2, sticky=W)
    OP_form = Label(top_frame,text="Tablet").grid(row=1, column = 2, sticky=W,pady=10)
    OP_form_abbrev = Label(top_frame,text="Tab").grid(row=2, column = 2, sticky=W,pady=10)
    OP_sig = Label(top_frame,text="TAB").grid(row=3, column=2, sticky=W,pady=10)
    
    
    
    
    
def openIP():
    IP = Toplevel()
    IP.title("Inpatient Business Rules")
    IP.iconbitmap("icon.ico")
    
def openUpdate():
    update = Toplevel()
    update.title("Updating Business Rules")
    update.iconbitmap("icon.ico")

def information():
    info_window = Toplevel()
    info_window.title("Help Menu")
    info_window.iconbitmap("icon.ico")
    info_frame = Frame(info_window)
    label = Label(info_window,text="Email Dan Garrison after 5pm for help")
    label.grid(row=0)


            
### CREATING MAIN WINDOW ###
        
root = Tk()
root.title("Federal Business Rules")
root.geometry('{}x{}'.format(250, 150))
root.iconbitmap("icon.ico")


# create all of the main containers
top_frame = Frame(root, pady=3)
center = Frame(root, padx=3, pady=3)
btm_frame = Frame(root, pady=3)
btm_frame2 = Frame(root, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0)
center.grid(row=1,)
btm_frame.grid(row=3)
btm_frame2.grid(row=4)

label1 = Label(top_frame, text = "Federal Pharmacy Business Rules")
label1.grid(row=0)

OPButton = Button(center, text="Outpatient", command=openOP)
OPButton.grid(row=0, column=0, padx=10, pady=10)
        
IPButton = Button(center, text="Inpatient", command=openIP)
IPButton.grid(row=0, column=1,padx=10, pady=10)

NTButton = Button(btm_frame2, text="Narrow Therp")
NTButton.grid(row=0, column=0,padx=5, pady=5)

SIButton = Button(btm_frame2, text="Syringe-Inj")
SIButton.grid(row=0, column=1,padx=5, pady=5)

ExButton = Button(btm_frame2, text="Exceptions")
ExButton.grid(row=0, column=2,padx=5, pady=5)


## Creating the Menu bar

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label = "File", menu=subMenu)
subMenu.add_command(label="Help", command=information)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)

updateMenu = Menu(menu)
menu.add_cascade(label = "Update", menu=updateMenu)
updateMenu.add_command(label="Database Path")
updateMenu.add_separator()
updateMenu.add_command(label="Add")
updateMenu.add_command(label="Modify")
updateMenu.add_command(label="Delete")


root.mainloop()