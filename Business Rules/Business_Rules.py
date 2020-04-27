# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 20:53:27 2020

@author: Eric Dudgeon
"""
import textwrap
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
data["Active"] = data["Active"].fillna("Yes")
data = data.fillna("Not in data")
OPkeys = data["Keys"].astype("string").to_list()
rules_text.close()
    
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
def wrap(string, lenght=50):
    return '\n'.join(textwrap.wrap(string, lenght))    
    
def openUpdate():
    root.filename = filedialog.askopenfilename(initialdir="/",title="Browse")
    if root.filename == "":
        rules_text = open("Rule_Path.txt", "r")
        data_file = rules_text.read()
        root.filename = data_file
        rules_text.close()
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

SIButton = Button(btm_frame2, text="Single-line Inj")
SIButton.grid(row=0, column=1,padx=5, pady=5)

ExButton = Button(btm_frame2, text="Exceptions")
ExButton.grid(row=0, column=2,padx=5, pady=5)

#### Creating Outpatient

def OPSelected(event):
    OP = Toplevel()
    OPclick = OP_button.get()
    OP.title(OPclick)
    OP.iconbitmap("icon.ico")
    OP.geometry('{}x{}'.format(675, 600))
    OP.grid_rowconfigure(0, weight=1)
    OP.grid_columnconfigure(1, weight=1)
    # create all of the OP containers
    top_frame = Frame(OP, pady=10, padx=3)
    center = Frame(OP, padx=3, pady=3)
    btm_frame = Frame(OP, pady=3)
    btm_frame2 = Frame(OP, pady=3)
    top_frame.columnconfigure(1,weight=1)
    ### Laying out OP container
    
    top_frame.grid(sticky=E+S+N+W)
    # center.grid(row=1, sticky=E+W)
    # btm_frame.grid(row=2)
    # btm_frame2.grid(row=3)
    back= Button(top_frame,text="Back",command=OP.destroy)
    back.grid(row=0,column=0,sticky=E)
    
    
    ## Pulling in OP data
    # DosageForm = data[data["Keys"] == OP_button.get()][["Dosage_Form", "Dosage_Abbrev"]]
    DosageForm = data[data["Keys"] == OP_button.get()]
    DosageForm = DosageForm.iloc[0,1:]
    OP_list = []
    for item in DosageForm:
        OP_list.append(item)   
    
    ### Getting OP Column headings
    headers = data.keys()
    headers = headers.to_list()
    headers = headers[1:]

    merged_list = [(headers[i], OP_list[i]) for i in range(0, len(headers))]
    
    treeview = ttk.Treeview(OP)
    ttk.Style().configure("Treeview",rowheight=60)
    treeview["columns"]=("One")
    treeview.column("One",width=200)
    treeview.grid(row=0,column=1,sticky=E+N+W+S,padx=15, pady=10)
    treeview.heading("#0",text="Reference")
    treeview.heading("One",text="Rules")
    for header, rule in merged_list:
        treeview.insert("",END,text=header, value=(rule,))


#Scroll Dropdown OP
OP_button = ttk.Combobox(top_frame, value=OPkeys)
OP_button.grid(row=2, column=0,padx=2, pady=0,sticky=W)
OP_button.current(0)
OP_button.bind("<<ComboboxSelected>>", OPSelected)

#### Creating Inpatient

IPkeys = ["Eric", "Dan", "Ethan", "Mack"]

def IPSelected(event):
    print("YES")

    
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