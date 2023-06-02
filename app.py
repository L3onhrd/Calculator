'''
1. input => 
- bridge design 
- mass
- position of weight 
- radius (to find moment of inertia)
- length 
- height 
- weight (or force )
2. output => 
- stand or not stand
- maximum force of the bridge (if not stand)
- bridge moment of inertia 
- Bridge torque ( (Weight * (length*length)) / (8*height) )
3. bridge design => 
- 300 kg max load (3 adults 3 anak sd primary kls 1 estmation) 
4. Type of bridge 

'''

from tkinter import *
import sqlite3
from tkinter import ttk

from os.path import realpath


# this will create the database file 
connection = sqlite3.connect("AllCalculator.db")
# Create the cursor to interact with the database
cursor = connection.cursor()
DATABASE_NAME = realpath('AllCalculator.db')

command1 = """CREATE TABLE IF NOT EXISTS
    Calculator(CalcID INTEGER PRIMARY KEY, Mass FLOAT, Acceleration FLOAT, Force FLOAT, Radius FLOAT, Inertia FLOAT, Length FLOAT, Height FLOAT, Torque FLOAT, ResultB STR)"""
cursor.execute(command1)

window = Tk()
window.title('Calculator Application')

window.geometry('683x768')  # 360p

window.configure(bg="blue") #To Change the Window Color

#Create a frame to hold the treeview
my_Frame=Frame(window, height = 68, width = 1, background="yellow")
my_Frame.place(x=10, y=500)
   
TREE = ttk.Treeview(my_Frame, columns=(1,2,3,4,5,6,7,8,9,10), show="headings", height="10")
TREE.column(1, stretch=NO, width=85)
TREE.column(2, stretch=NO, width=50)
TREE.column(3, stretch=NO, width=80)
TREE.column(4, stretch=NO, width=70)
TREE.column(5, stretch=NO, width=50)
TREE.column(6, stretch=NO, width=55)
TREE.column(7, stretch=NO, width=50)
TREE.column(8, stretch=NO, width=50)
TREE.column(9, stretch=NO, width=70)
TREE.column(10, stretch=NO, width=100)

#tree.column("# 1",anchor=CENTER, stretch=NO, width=100)
TREE.pack()

TREE.heading(1, text="Calculation ID")
TREE.heading(2, text="Mass")
TREE.heading(3, text="Acceleration")
TREE.heading(4, text="Force")
TREE.heading(5, text="Radius")
TREE.heading(6, text="Inertia")
TREE.heading(7, text="Length")
TREE.heading(8, text="Height")
TREE.heading(9, text="Torque")
TREE.heading(10, text="Result")







lbl1 = Label(window, text="Bridge force & inertia calculator", font = "Arial 20")
lbl1.place(x=100, y=10)
lbl1.configure(background='yellow',  width=28)

lbl2 = Label(window, text="Mass", font = "Arial 10")
lbl2.place(x=10, y=70)
lbl2.configure(background='yellow',  width=7)

MassInput = StringVar() # This will hold the input in the Username Textbox    
txtMassInput= Entry(window, width=20, textvariable=MassInput)
txtMassInput.place(x=90, y=72)

lbl3 = Label(window, text="Acceleration", font = "Arial 10")
lbl3.place(x=10, y=100)
lbl3.configure(background='yellow',  width=9)

AccInput = StringVar() # This will hold the input in the Username Textbox    
txtAccInput= Entry(window, width=20, textvariable=AccInput)
txtAccInput.place(x=90, y=102)

lbl4 = Label(window, text="Force", font = "Arial 10")
lbl4.place(x=10, y=130)
lbl4.configure(background='yellow',  width=7)
lblForceOut  = Label(window, text="", font = "Arial 10")
lblForceOut.place(x=90, y = 132)
lblForceOut.configure(background='white', width = 15) 

lbl5 = Label(window, text="Radius", font = "Arial 10")
lbl5.place(x=10, y=160)
lbl5.configure(background='yellow',  width=7)

RadiusInput = StringVar() # This will hold the input in the Username Textbox    
txtRadiusInput= Entry(window, width=20, textvariable=RadiusInput)
txtRadiusInput.place(x=90, y=162)

lbl6 = Label(window, text="Inertia", font = "Arial 10")
lbl6.place(x=10, y=190)
lbl6.configure(background='yellow',  width=7)
lblInertiaOut  = Label(window, text="", font = "Arial 10")
lblInertiaOut.place(x=90, y = 192)
lblInertiaOut.configure(background='white', width = 15)

lbl8 = Label(window, text="Length", font = "Arial 10")
lbl8.place(x=10, y=220)
lbl8.configure(background='yellow',  width=7)
LengthInput = StringVar() # This will hold the input in the Username Textbox    
txtLengthInput= Entry(window, width=20, textvariable=LengthInput)
txtLengthInput.place(x=90, y=222)

lbl9 = Label(window, text="Height", font = "Arial 10")
lbl9.place(x=10, y=250)
lbl9.configure(background='yellow',  width=7)
HeightInput = StringVar() # This will hold the input in the Username Textbox    
txtHeightInput= Entry(window, width=20, textvariable=HeightInput)
txtHeightInput.place(x=90, y=252)

lbl10 = Label(window, text="Torque", font = "Arial 10")
lbl10.place(x=10, y=280)
lbl10.configure(background='yellow',  width=7)
lblTorqueOut  = Label(window, text="", font = "Arial 10")
lblTorqueOut.place(x=90, y = 282)
lblTorqueOut.configure(background='white', width = 15)

lbl7 = Label(window, text=" Bridge Type", font = "Arial 10")
lbl7.place(x=10, y=310)
lbl7.configure(background='yellow',  width=9)
lblBridgeType  = Label(window, text="Cable-Stayed Bridge", font = "Arial 10")
lblBridgeType.place(x=90, y = 312)
lblBridgeType.configure(background='white', width = 15) 

global F
F = "undefined"
global I
I = "undefined"
global ResultB

def CalculateForce():
    M = float(txtMassInput.get())
    A = float(txtAccInput.get())
    global F
    F = M * A 
    lblans = Label(window, text= F, font = "Arial 10")
    #global txtForceOutput 
    #txtForceOutput = print(F)
    lblans.place(x=90, y=130)
    lblans.configure(background='white',  width=15, text=f"{F : .2f}")
    if F > 2940:
        global ResultB
        ResultB = "bridge collapse"
    else: 
        ResultB = "load withstanded"

def CalculateInertia():
    M = float(txtMassInput.get())
    R = float(txtRadiusInput.get())
    global I
    I = M * R
    lblans2 = Label(window, text= I, font = "Arial 10")
    #global txtForceOutput 
    #txtForceOutput = print(F)
    lblans2.place(x=90, y=190)
    lblans2.configure(background='white',  width=15, text=f"{I: .2f}")

def CalculateTorque():
    Weight = F
    L = float(txtLengthInput.get())
    H = float(txtHeightInput.get())
    global T
    T = ( (Weight * (L*L)) / (8*H) )
    lblans3 = Label(window, text= T, font = "Arial 10")
    #global txtForceOutput 
    #txtForceOutput = print(F)
    lblans3.place(x=90, y=282)
    lblans3.configure(background='white',  width=15, text=f"{T: .2f}")


def clearValue():
    txtMassInput.delete(0, END)
    txtAccInput.delete(0, END)
    txtRadiusInput.delete(0, END)
    txtLengthInput.delete(0, END)
    txtHeightInput.delete(0, END)
    lblans = Label(window, text= "", font = "Arial 10")
    lblans.place(x=90, y=130)
    lblans.configure(background='white',  width=15)
    lblans2 = Label(window, text= "", font = "Arial 10")
    lblans2.place(x=90, y=190)
    lblans2.configure(background='white',  width=15)
    lblans3 = Label(window, text= "", font = "Arial 10")
    lblans3.place(x=90, y=282)
    lblans3.configure(background='white',  width=15)
    
def SAVE():
    '''
    if len(txtLengthInput.get()) == 0:
        txtLengthInput = 0
    if len(txtHeightInput.get()) == 0:
        txtHeightInput = 0
    if len(txtMassInput.get()) == 0:
        txtMassInput = 0
    if len(txtAccInput.get()) == 0:
        txtAccInput = 0
    if len(txtRadiusInput.get()) == 0:
        txtRadiusInput = 0
    '''
    Mout = txtMassInput.get() # this will grab the input
    Aout = txtAccInput.get()
    Fout = F
    Rout = txtRadiusInput.get()
    Iout = I
    Lout = float(txtLengthInput.get())
    Hout = float(txtHeightInput.get())
    Tout = T
    Bout = ResultB
    # I will not save it on my database table
    cursor.execute("INSERT INTO Calculator VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Mout, Aout, Fout, Rout, Iout, Lout, Hout, Tout, Bout))
    connection.commit()  # save data to disk
    populate()

def populate(): 
    cursor.execute("SELECT * FROM Calculator")
    result = cursor.fetchall()
    for record in TREE.get_children():
        TREE.delete(record)
    if len(result) != 0:
        for i in result:
            TREE.insert('', 'end', values=i)




# Add the command button CONVERT
cmdCalculateF = Button(window, text="Calculate Force", width=20, height=2, command=CalculateForce)
cmdCalculateF.place(x=260, y=70)

cmdClearV = Button(window, text="Clear Value", width=20, height=2, command=clearValue)
cmdClearV.place(x=260, y=115)

cmdSaveD = Button(window, text="Save Value", width=20, height=2, command=SAVE)
cmdSaveD.place(x=420, y=70)

cmdCalculateI = Button(window, text="Calculate Inertia", width=20, height=2, command=CalculateInertia)
cmdCalculateI.place(x=420, y=115)

cmdCalculateT = Button(window, text="Calculate Torque", width=20, height=2, command=CalculateTorque)
cmdCalculateT.place(x=340, y=160)




window.mainloop()
