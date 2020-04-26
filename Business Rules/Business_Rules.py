# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 20:53:27 2020

@author: Eric Dudgeon
"""

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import sqlite3
rules_text = open("Rule_Path.txt", "r")
data_file = rules_text.read()

if data_file == "":
    data_file = "Business Rules File.csv"
else:
    data_file = data_file

data = pd.read_csv(data_file, index_col=False)
OPkeys = data["Keys"].astype("string").to_list()
rules_text.close()
# def openOP():
#     OP = Toplevel()
#     OP.title("Outpatient Business Rules")
#     OP.iconbitmap("icon.ico")
#     OP.geometry('{}x{}'.format(500, 600))
    
#     # create all of the OP containers
#     top_frame = Frame(OP, pady=10, padx=3)
#     center = Frame(OP, padx=3, pady=3)
#     btm_frame = Frame(OP, pady=3)
#     btm_frame2 = Frame(OP, pady=3)
    
#     # layout all of the OP containers
#     # OP.grid_rowconfigure(1, weight=1)
#     # OP.grid_columnconfigure(0, weight=1)
    
#     top_frame.grid(row=0,sticky=N+E+S+W)
#     center.grid(row=1, sticky=E+W)
#     btm_frame.grid(row=2)
#     btm_frame2.grid(row=3)
    
#     ## Adding OP Back Button
#     OPmenu = Menu(OP)
#     OP.config(menu=OPmenu)
#     OPsubMenu = Menu(menu)
#     OPmenu.add_cascade(label = "File", menu=OPsubMenu)
#     OPsubMenu.add_command(label="View All")
#     OPsubMenu.add_command(label="View Inactive")
#     OPsubMenu.add_separator()
#     OPsubMenu.add_command(label="Back", command=OP.destroy)
    
#     ##Creating Selected command FUCKING GENIUS Line of Code
#     def Selected(event):
#         DosageForm = data[data["Keys"] == OP_button.get()][["Dosage_Form"]]
#         Form = DosageForm["Dosage_Form"]
#         select = StringVar(Form)
#         OP_form = Label.config(top_frame,text=select)
#         OP_form.grid(row=1, column = 2, sticky=W,pady=10)
        
#     #Scroll Dropdown
#     OP_button = ttk.Combobox(top_frame, value=keys)
#     OP_button.grid(row=0, column=0,padx=10, pady=10,sticky=W)
#     OP_button.current(0)
#     OP_button.bind("<<ComboboxSelected>>", Selected)
    
            
#     ## Adding labels to OP Left
#     OP_form_label = Label(top_frame,text="Dosage Form:").grid(row=1, column = 0, sticky=W, pady=10)
#     OP_form_abbrev_label = Label(top_frame,text="Dosage Form Abbrev").grid(row=2, column=0, sticky=W,pady=10)
#     OP_sig_label = Label(top_frame,text="SIG Tool").grid(row=3, column=0, sticky=W,pady=10)
    
#     ## Aligned format
#     space= Label(top_frame,text="").grid(row=0,column=1,padx=25)
#     space1= Label(top_frame,text="").grid(row=1,column=1,padx=25)
#     space3= Label(top_frame, text="").grid(row=2,column=1, padx=6)
#     space3= Label(top_frame, text="").grid(row=3,column=1, padx=20)
    
#     ##Adding Labels to OP Right
#     OPlabel = Label(top_frame,text="Outpatient Pharmacy Business Rules")
#     OPlabel.grid(row=0, column=2, sticky=W)
#     OP_form_abbrev = Label(top_frame,text="Tab").grid(row=2, column = 2, sticky=W,pady=10)
#     OP_sig = Label(top_frame,text="TAB").grid(row=3, column=2, sticky=W,pady=10)
    
    
def openUpdate():
    root.filename = filedialog.askopenfilename(initialdir="/",title="Browse")
    if root.filename == "":
        messagebox.showinfo("Warning: Please Make Selection","No selection will result in Business Rules at program creation")
    else:
        root.filename = root.filename
    file = open("Rule_Path.txt", "w")
    file.write(root.filename)
    file.close()
 
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
root.geometry('{}x{}'.format(325, 350))
root.iconbitmap("icon.ico")


# create all of the main containers
top_frame = Frame(root, pady=0)
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
label1.grid(row=0,column=0, columnspan=3, sticky=N, padx=25, pady=10)

OPlabel = Label(top_frame, text="Outpatient")
OPlabel.grid(row=1, column=0, padx=40, pady=0, sticky=W)
        
IPlabel = Label(top_frame, text="Inpatient")
IPlabel.grid(row=1, column=2,padx=50, pady=0, sticky=E)

NTButton = Button(btm_frame2, text="Narrow Therp")
NTButton.grid(row=0, column=0,padx=5, pady=5)

SIButton = Button(btm_frame2, text="Syringe-Inj")
SIButton.grid(row=0, column=1,padx=5, pady=5)

ExButton = Button(btm_frame2, text="Exceptions")
ExButton.grid(row=0, column=2,padx=5, pady=5)

#### Creating Outpatient

def OPSelected(event):
    OP = Toplevel()
    OP.title("Outpatient Bussiness Rules")
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
    back= Button(OP,text="Back",command=OP.destroy)
    back.grid(row=0,column=0,sticky=E)
    # Pulling in OP data
    
    DosageForm = data[data["Keys"] == OP_button.get()][["Dosage_Form"]]
    form = Label(OP, text=DosageForm)
    form.grid(row=0, column=1)
    # OP_form = Label.config(top_frame,text=select)
    # OP_form.grid(row=1, column = 2, sticky=W,pady=10)
    
#Scroll Dropdown
OP_button = ttk.Combobox(top_frame, value=OPkeys)
OP_button.grid(row=2, column=0,padx=2, pady=0,sticky=W)
OP_button.current(0)
OP_button.bind("<<ComboboxSelected>>", OPSelected)

#### Creating Inpatient

IPkeys = ["Eric", "Is", "A", "NERD"]

def IPSelected(event):
    print("YES")
    # DosageForm = data[data["Keys"] == OP_button.get()][["Dosage_Form"]]
    # Form = DosageForm["Dosage_Form"]
    # select = StringVar(Form)
    # OP_form = Label.config(top_frame,text=select)
    # OP_form.grid(row=1, column = 2, sticky=W,pady=10)
    
#Scroll Dropdown
IP_button = ttk.Combobox(top_frame, value=IPkeys)
IP_button.grid(row=2, column=2,padx=2, pady=0,sticky=E)
IP_button.current(0)
IP_button.bind("<<ComboboxSelected>>", IPSelected)


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
updateMenu.add_command(label="Data File Path", command=openUpdate)


viewMenu = Menu(menu)
menu.add_cascade(label = "View", menu=viewMenu)
viewMenu.add_command(label="All-OP")
viewMenu.add_command(label="All-IP")
viewMenu.add_separator()
viewMenu.add_command(label="Inactive")


root.mainloop()