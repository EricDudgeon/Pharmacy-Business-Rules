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
    data_file = "Business Rules File - Master.xlsx"
else:
    data_file = data_file

while True:
    try:
        datafile = pd.read_excel(data_file, sheet_name="Drug Forms")
    except:
        data_file = "Business Rules File - Master.xlsx"
    else:
        break
          
rules_text.close()

data = pd.read_excel(data_file, index_col=False, sheet_name="Drug Forms")
        
###Reading Narrow Therp
Narrows = pd.read_excel(data_file,index_col=False,sheet_name="NTIs")
Item_desc = Narrows.loc[0,"Item Description"]
NDC_desc = Narrows.loc[0,"NDC Description"]
Narrows.loc[Narrows["Item Description"].isnull(), "Item Description"] = Item_desc
Narrows.loc[Narrows["NDC Description"].isnull(), "NDC Description"] = NDC_desc
Narrows = Narrows.fillna("")
NTkeys = Narrows["Keys"].to_list()
NTkeys = sorted(NTkeys,key=str.lower)

###inactive Data
old_data = data[~data["Active"].isnull()]
old_data = old_data.fillna(" ")
INkeys = old_data["Keys"].astype("string").to_list()
INkeys = sorted(INkeys,key=str.lower)
#### Active OP data
data = data[data["Active"].isnull()]
data["Active"] = data["Active"].fillna("Yes")
data = data.fillna("")
OPkeys = data["Keys"].astype("string").to_list()
OPkeys = sorted(OPkeys,key=str.lower)
    
#### TEXT WRAP FUNCTION

def wrap(item, length=75):
    item = item.replace("\n\n","\n")
    item = item.replace("\n","**")
    item = item.replace("'","")
    item ='\n'.join(textwrap.wrap(item, length))
    item = item.replace("**","\n")
    return item
        
##### CREATING ABILITY TO UPDATE FILE   
def openUpdate():
    root.filename = filedialog.askopenfilename(initialdir="/",title="Browse", filetypes=(("Excel Workbook","*.xlsx"),))
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

#### CREATING HELP WINDOW FUNCTION
def information():
    info_window = Toplevel()
    info_window.title("Help Menu")
    info_window.iconbitmap("icon.ico")
    info_frame = Frame(info_window)
    label = Label(info_window,text="1: Do not change 'Active' column heading in dataset")
    label.grid(row=0, pady=5,padx=10, sticky=W)
    label2 = Label(info_window, text="2: Active column values should be blank unless inactive")
    label2.grid(row=1, pady=5,padx=10, sticky=W)
    label3 = Label(info_window, text="3: Primary Keys(to pull back data) are in dataset column A.")
    label3.grid(row=2, pady=5,padx=10, sticky=W)
    label3 = Label(info_window, text="4: Keys can be changed as needed but not the header 'Keys'")
    label3.grid(row=3, pady=5,padx=10, sticky=W)
    label4 = Label(info_window, text="5: Dont change sheet names relating to the data")
    label4.grid(row=4, pady=5,padx=10, sticky=W)

#### CREATING INACTIVE FUNCTION
def inactive():
    i_form = Toplevel()
    i_form.title("Inactive")
    i_form.iconbitmap("icon.ico")
    i_form.geometry('{}x{}'.format(200, 50))
    top_frame = Frame(i_form, pady=10)
    top_frame.grid(row=0, sticky=N+E+S+W)
    back= Button(top_frame,text="Back",command=i_form.destroy)
    back.grid(row=0,column=0,sticky=E+N)
    
    def INSelected(event):
        inactive = Toplevel()
        INClick = scroll.get()
        inactive.title(INClick)
        inactive.iconbitmap("icon.ico")
        inactive.geometry('{}x{}'.format(752, 600))
        inactive.grid_rowconfigure(0, weight=1)
        inactive.grid_columnconfigure(1, weight=1)
        top_frame = Frame(inactive, pady=0)
        top_frame.grid(row=0, sticky=N+E+S+W)
        back= Button(top_frame,text="Back",command=inactive.destroy)
        back.grid(row=0,column=0,sticky=E+N)
 
        ### Getting inactive information
        old = old_data[old_data["Keys"] == scroll.get()]
        old = old.iloc[0,1:]
        old = old.apply(str)
        old_list = []
        for item in old:
            old_list.append(item)   
        ### Getting OP Column headings
        headers = old_data.keys()
        headers = headers.to_list()
        headers = headers[1:]
    
        merged_list = [(headers[i], old_list[i]) for i in range(0, len(headers))]
        
        ### DISPLAYING DATA
        treeview = ttk.Treeview(inactive)
        verscrlbar = ttk.Scrollbar(inactive,  orient ="vertical", command = treeview.yview)
        verscrlbar.grid(column=2, row=0, sticky=N+S)  
    
        ttk.Style().configure("Treeview",rowheight=60)
        treeview["columns"]=("One")
        treeview.column("#0",width=50)
        treeview.column("One",width=200)
        treeview.grid(row=0,column=1,sticky=E+N+W+S,padx=15, pady=10)
        treeview.heading("#0",text="Reference")
        treeview.heading("One",text="Rules")
    
        for header, rule in merged_list:
            treeview.insert("",END,text=header, value=(wrap(rule),))
            
    #Scrollbar for inactive
    scroll = ttk.Combobox(top_frame, value=INkeys)
    scroll.grid(row=0, column=1,padx=5, pady=0)
    scroll.current(0)
    scroll.bind("<<ComboboxSelected>>", INSelected)
    
### CREATING NARROW THERPS FUNCTION    
def NTs(event):
    ### creating main container for NT
    Nt = Toplevel()
    NTClick = Nt_drop.get()
    Nt.title(NTClick)
    Nt.iconbitmap("icon.ico")
    Nt.geometry('{}x{}'.format(725, 600))
    Nt.grid_rowconfigure(0, weight=1)
    Nt.grid_columnconfigure(1, weight=1)
    top_frame = Frame(Nt, pady=0)
    top_frame.grid(row=0, sticky=N+E+S+W)
    back= Button(top_frame,text="Back",command=Nt.destroy)
    back.grid(row=0,column=0,sticky=E+N)

    Therps = Narrows[Narrows["Keys"] == Nt_drop.get()]
    Therps = Therps.iloc[0,1:]
    Therps = Therps.apply(str)
    Therps_list = []
    for item in Therps:
        Therps_list.append(item)
    ### Getting OP Column headings
    headers = Narrows.keys()
    headers = headers.to_list()
    headers = headers[1:]

    merged_list = [(headers[i], Therps_list[i]) for i in range(0, len(headers))]

    ### DISPLAYING DATA
    treeview = ttk.Treeview(Nt)
    verscrlbar = ttk.Scrollbar(Nt,  orient ="vertical", command = treeview.yview)
    verscrlbar.grid(column=2, row=0, sticky=N+S)  

    ttk.Style().configure("Treeview",rowheight=80)
    treeview["columns"]=("One")
    treeview.column("#0",minwidth=0,width=135, stretch=False)
    treeview.column("One",width=200)
    treeview.grid(row=0,column=1,sticky=E+N+W+S,padx=15, pady=10)
    treeview.heading("#0",text="Reference")
    treeview.heading("One",text="Rules")

    for header, rule in merged_list:
        treeview.insert("",END,text=header, value=(wrap(rule),))
    
###CREATING EXCEPTIONS
def Exceptions():
    e = Toplevel()
    e.title("Exceptions")
    e.iconbitmap("icon.ico")
    e.geometry('{}x{}'.format(200, 50))
    top_frame = Frame(e, pady=10)
    top_frame.grid(row=0, sticky=N+E+S+W)
    back= Button(top_frame,text="Back",command=e.destroy)
    back.grid(row=0,column=0,sticky=E+N,pady=3)
    label = Label(top_frame,text="NDC:").grid(row=0,column=1)
    entry = Entry(e).grid(row=0,column=2)

          
###CREATING SINGLE LINE INJECTION FUNCTION
def SL(event):
    return

####CREATING OUTPATIENT
def OPSelected(event):
    OP = Toplevel()
    OPclick = OP_button.get()
    OP.title(OPclick)
    OP.iconbitmap("icon.ico")
    OP.geometry('{}x{}'.format(725, 600))
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
    center.grid(row=1, sticky=E+W)
    # btm_frame.grid(row=2)
    # btm_frame2.grid(row=3)
    back= Button(top_frame,text="Back",command=OP.destroy)
    back.grid(row=0,column=0,sticky=E)
    
    
    ## Pulling in OP data
    # DosageForm = data[data["Keys"] == OP_button.get()][["Dosage_Form", "Dosage_Abbrev"]]
    DosageForm = data[data["Keys"] == OP_button.get()]
    DosageForm = DosageForm.iloc[0,1:]
    DosageForm = DosageForm.apply(str)
    OP_list = []
    for item in DosageForm:
        OP_list.append(item)   
    ### Getting OP Column headings
    headers = data.keys()
    headers = headers.to_list()
    headers = headers[1:]

    merged_list = [(headers[i], OP_list[i]) for i in range(0, len(headers))]
    
    ### DISPLAYING DATA
    treeview = ttk.Treeview(OP)
    verscrlbar = ttk.Scrollbar(OP,  orient ="vertical", command = treeview.yview)
    verscrlbar.grid(column=2, row=0, sticky=N+S)  

    ttk.Style().configure("Treeview",rowheight=60)
    treeview["columns"]=("One")
    treeview.column("#0",width=50)
    treeview.column("One",width=200)
    treeview.grid(row=0,column=1,sticky=E+N+W+S,padx=15, pady=10)
    treeview.heading("#0",text="Reference")
    treeview.heading("One",text="Rules")
    
    for header, rule in merged_list:
        treeview.insert("",END,text=header, value=(wrap(rule),))

#### CREATING INPATIENT
IPkeys = ["To be built?"]

def IPSelected(event):
    print("YES")


### CREATING MAIN WINDOW ###
        
root = Tk()
root.title("Federal Business Rules")
root.geometry('{}x{}'.format(325, 200))
root.iconbitmap("icon.ico")


# create all of the main containers
top_frame = Frame(root)
center = Frame(root)
# btm_frame = Frame(root)
# btm_frame2 = Frame(root, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


top_frame.grid(row=0,sticky=N+E+S+W)
center.grid(row=1,sticky=W+N+E+S, pady=10)
# center.grid(row=3,sticky=W+N+E+S,pady=10)
# btm_frame.grid(row=2, sticky=W+N+E+S, pady=10)
# btm_frame2.grid(row=4)

#### CREATING LABELS
label1 = Label(top_frame, text = "Federal Pharmacy Business Rules")
label1.grid(row=0,column=0, columnspan=3, sticky=N, padx=25, pady=10)

OPlabel = Label(top_frame, text="Outpatient")
OPlabel.grid(row=1, column=0, padx=5, pady=0, sticky=W)
        
IPlabel = Label(top_frame, text="Inpatient")
IPlabel.grid(row=1, column=2,padx=15, pady=0, sticky=W)

NTlabel = Label(center, text="Narrow Therapeutic")
NTlabel.grid(row=0, column=0, padx=5,sticky=W)

SLlabel = Label(center, text="Single-Line Inj")
SLlabel.grid(row=0, column=1, padx=15,sticky=W)


#Scroll Dropdown OP
OP_button = ttk.Combobox(top_frame, value=OPkeys)
OP_button.grid(row=2, column=0,padx=5, pady=0,sticky=W)
OP_button.current(0)
OP_button.bind("<<ComboboxSelected>>", OPSelected)

    
#Scroll Dropdown IP
IP_button = ttk.Combobox(top_frame, value=IPkeys)
IP_button.grid(row=2, column=2,padx=15, pady=0,sticky=W)
IP_button.current(0)
IP_button.bind("<<ComboboxSelected>>", IPSelected)


###Scroll Dropdown for NT
Nt_drop = ttk.Combobox(center, value=NTkeys)
Nt_drop.grid(row=1, column=0,padx=5, pady=0,sticky=W)
Nt_drop.current(0)
Nt_drop.bind("<<ComboboxSelected>>", NTs)

SLkeys=["To be built?"]
####Scroll Dropdown for Singline INJ
Sl_drop = ttk.Combobox(center, value=SLkeys)
Sl_drop.grid(row=1, column=1,padx=15, pady=0,sticky=W)
Sl_drop.current(0)
Sl_drop.bind("<<ComboboxSelected>>")

####Scroll Dropdown for Inactive

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
viewMenu.add_command(label="Exceptions", command=Exceptions)
viewMenu.add_command(label="Inactive", command=inactive)

root.mainloop()