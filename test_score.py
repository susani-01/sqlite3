import sqlite3
from tkinter import *

def addtolist():
    newName = sName.get()
    newGrade = sGrade.get()
    cursor.execute("""INSERT INTO Score(name,score) VALUES(?,?)""",(newName,newGrade))

    db.commit()
    sName.delete(0,END)
    sGrade.delete(0,END)
    sName.focus()

def clearlist():
    sName.delete(0,END)
    sGrade.delete(0,END)
    sName.focus()

with sqlite3.connect("testScore.db") as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Score(id integer PRIMARY KEY,name text,score integer);""")

window = Tk()
window.title("TestScore")
window.geometry("800x800")

label = Label(window,text = "Student Name")
label.place(x=30,y=40)
sName = Entry(window,width = 20,text = '')
sName.place(x=130,y=40)
sName.focus()

label2 = Label(window,text = "Student Grade")
label2.place(x = 30,y =  90  )
sGrade = Entry(window,width = 20)
sGrade.place(x = 130,y = 90 )
sGrade.focus()

btn1= Button(window,text="Add",bg = 'yellow',command = addtolist)
btn1.place(x = 130,y = 130)

btn2 = Button(window,text = "clear",bg = 'yellow', command = clearlist)
btn2.place(x = 190, y = 130)

db.commit()
db.close
window.mainloop()






    