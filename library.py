
from tkinter import *
import sqlite3
from tkinter import messagebox

window = Tk()
window.geometry("350x400")
window.configure(bg="black")
window.title("LIBRARY MANAGEMENT SYSTEM")

conn = sqlite3.connect('library.db')
cursor = conn.cursor()
#conn.execute('''ALTER TABLE libs ADD unique_id INTEGER''')
# table created -- cursor.execute("CREATE TABLE libs(NAME TEXT, CLASS TEXT, ROLL INTEGER, CONTACT INTEGER, DATE TEXT, TIME TEXT, BNAME TEXT, BID INTEGER)")
#to check columns(not needed)-------
"""print('\nColumns in library table:')
data=cursor.execute('''SELECT * FROM libs''')
for column in data.description:
    print(column[0])"""

#defining buttons------

def win_add():
    add = Toplevel()
    add.title("ADD A RECORD")
    add.geometry("700x500")
    
    #labels------

    la1 = Label(add, text="NAME OF STUDENT",font=("Courier", 15))
    la1.place(x = 10, y = 20)

    la2 = Label(add, text="CLASS",font=("Courier", 15))
    la2.place(x = 10, y = 70)

    la3 = Label(add, text="ROLL NUMBER",font=("Courier", 15))
    la3.place(x = 10, y = 120)

    la4 = Label(add, text="CONTACT NUMBER",font=("Courier", 15))
    la4.place(x = 10, y = 170)

    la5 = Label(add, text="DATE",font=("Courier", 15))
    la5.place(x = 10, y = 220)

    la6 = Label(add, text="TIME",font=("Courier", 15))
    la6.place(x = 10, y = 270)

    la7 = Label(add, text="BOOK NAME",font=("Courier", 15))
    la7.place(x = 10, y = 320)

    la8 = Label(add, text="BOOK ID",font=("Courier", 15))
    la8.place(x = 10, y = 370)

    la9 = Label(add, text="UNIQUE ID",font=("Courier", 15))
    la9.place(x = 10, y = 420)

    #entry boxes------

    ea1 = Entry(add, font=("Courier", 15), width=35)
    ea1.place(x = 200, y=20)

    ea2 = Entry(add, font=("Courier", 15), width=35)
    ea2.place(x = 200, y=70)

    ea3 = Entry(add, font=("Courier", 15), width=35)
    ea3.place(x = 200, y=120)

    ea4 = Entry(add, font=("Courier", 15), width=35)
    ea4.place(x = 200, y=170)

    ea5 = Entry(add, font=("Courier", 15), width=35)
    ea5.place(x = 200, y=220)

    ea6 = Entry(add, font=("Courier", 15), width=35)
    ea6.place(x = 200, y=270)

    ea7 = Entry(add, font=("Courier", 15), width=35)
    ea7.place(x = 200, y=320)

    ea8 = Entry(add, font=("Courier", 15), width=35)
    ea8.place(x = 200, y=370)

    ea9 = Entry(add, font=("Courier", 15), width=35)
    ea9.place(x = 200, y=420)

    def save_rec():
       conn = sqlite3.connect('library.db')
       cursor = conn.cursor() 
       cursor.execute('''INSERT INTO libs VALUES(:NAME,:CLASS,:ROLL,:CONTACT,:DATE,:TIME,:BNAME,:BID,:unique_id)''',
                        {
                            'NAME':ea1.get(),
                            'CLASS':ea2.get(),
                            'ROLL':ea3.get(),
                            'CONTACT':ea4.get(),
                            'DATE':ea5.get(),
                            'TIME':ea6.get(),
                            'BNAME':ea7.get(),
                            'BID':ea8.get(),
                            'unique_id':ea9.get()
                        
                        })
       conn.commit()
       conn.close()

       ea1.delete(0,END)
       ea2.delete(0,END)
       ea3.delete(0,END)
       ea4.delete(0,END)
       ea5.delete(0,END)
       ea6.delete(0,END)
       ea7.delete(0,END)
       ea8.delete(0,END)
       ea9.delete(0,END)

       messagebox.showinfo("ADD RECORD" ,"RECORD HAS BEEN ADDED")

       add.destroy()

    #button in add window------

    ba1 = Button(add, text="SAVE RECORD" ,height= 2, width=25, command=save_rec)
    ba1.grid(columnspan = 3, padx = 20, pady=20, ipadx=30)
    ba1.place(x=225,y=450)

    
def win_rem():
    rem = Toplevel()
    rem.title("REMOVE A RECORD")
    rem.geometry("700x500")

    #labels------

    lr1 = Label(rem, text="CONTACT NUMBER",font=("Courier", 15))
    lr1.place(x = 10, y = 70)

    lr2 = Label(rem, text="BOOK NAME",font=("Courier", 15))
    lr2.place(x = 10, y = 120)

    lr3 = Label(rem, text="BOOK ID",font=("Courier", 15))
    lr3.place(x = 10, y = 170)

    #entry boxes------

    er1 = Entry(rem, font=("Courier", 15), width=35)
    er1.place(x = 200, y=70)

    er2 = Entry(rem, font=("Courier", 15), width=35)
    er2.place(x = 200, y=120)

    er3 = Entry(rem, font=("Courier", 15), width=35)
    er3.place(x = 200, y=170)

    def del_rec():
        
        conn = sqlite3.connect('library.db')

        cursor = conn.cursor()
        
        cursor.execute('''DELETE FROM libs WHERE CONTACT = ''' + er1.get() + """ AND BNAME = """ + er2.get())
        er1.delete(0,END)
        er2.delete(0,END)
        
        conn.commit()

        conn.close()
    
        rem.destroy()

    #button in remove window------

    br1 = Button(rem, text="DELETE RECORD" ,height= 2, width=25, command=del_rec)
    br1.grid(columnspan = 3, padx = 20, pady=20, ipadx=30)
    br1.place(x=225,y=225)

def show_rec():
    show = Toplevel()
    show.title("SHOW RECORDS")
    show.geometry("1900x500")

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor() 
    cursor.execute('''SELECT * FROM libs''')

    

    records = cursor.fetchall()
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " , " + str(record[1]) + " , " + str(record[2]) + " , " + str(record[3]) + " , " + str(record[4]) + " , " + str(record[5]) + " , " + str(record[6]) + " , " + str(record[7]) + "\n"
    
    ls1 = Label(show, text = print_records, font=("courier 15"))
    ls1.place(x=0,y=0)

def u_rec():
    update = Toplevel()
    update.title("SEARCH RECORD TO UPDATE")
    update.configure(bg="black")
    update.geometry("650x250")

    # label in update screen------

    lu1 = Label(update, text="CONTACT NUMBER",font=("Courier", 15))
    lu1.configure(bg="black", fg="red")
    lu1.place(x = 10, y = 70)

    #entry box in update -------

    eu1 = Entry(update, font=("Courier", 15), width=35)
    eu1.place(x = 200, y=70)

    def find_r():
        find_rec = Toplevel()
        find_rec.title("UPDATE RECORD")
        find_rec.configure(bg="black")
        find_rec.geometry("700x500")

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor() 

        cursor.execute('''SELECT * FROM libs WHERE CONTACT = '''+ eu1.get())
        eu1.delete(0,END)

        records_find = cursor.fetchall()

        #label in find_rec----

        lfr1 = Label(find_rec, text="NAME OF STUDENT",font=("Courier", 15))
        lfr1.place(x = 10, y = 20)
        lfr1.configure(bg="black", fg="red")

        lfr2 = Label(find_rec, text="CLASS",font=("Courier", 15))
        lfr2.place(x = 10, y = 70)
        lfr2.configure(bg="black", fg="red")

        lfr3 = Label(find_rec, text="ROLL NUMBER",font=("Courier", 15))
        lfr3.place(x = 10, y = 120)
        lfr3.configure(bg="black", fg="red")

        lfr4 = Label(find_rec, text="CONTACT NUMBER",font=("Courier", 15))
        lfr4.place(x = 10, y = 170)
        lfr4.configure(bg="black", fg="red")

        lfr5 = Label(find_rec, text="DATE",font=("Courier", 15))
        lfr5.place(x = 10, y = 220)
        lfr5.configure(bg="black", fg="red")

        lfr6 = Label(find_rec, text="TIME",font=("Courier", 15))
        lfr6.place(x = 10, y = 270)
        lfr6.configure(bg="black", fg="red")

        lfr7 = Label(find_rec, text="BOOK NAME",font=("Courier", 15))
        lfr7.place(x = 10, y = 320)
        lfr7.configure(bg="black", fg="red")

        lfr8 = Label(find_rec, text="BOOK ID",font=("Courier", 15))
        lfr8.place(x = 10, y = 370)
        lfr8.configure(bg="black", fg="red")

        #entry boxes in find_rec

        efr1 = Entry(find_rec, font=("Courier", 15), width=35)
        efr1.place(x = 200, y=20)

        efr2 = Entry(find_rec, font=("Courier", 15), width=35)
        efr2.place(x = 200, y=70)

        efr3 = Entry(find_rec, font=("Courier", 15), width=35)
        efr3.place(x = 200, y=120)

        efr4 = Entry(find_rec, font=("Courier", 15), width=35)
        efr4.place(x = 200, y=170)

        efr5 = Entry(find_rec, font=("Courier", 15), width=35)
        efr5.place(x = 200, y=220)

        efr6 = Entry(find_rec, font=("Courier", 15), width=35)
        efr6.place(x = 200, y=270)

        efr7 = Entry(find_rec, font=("Courier", 15), width=35)
        efr7.place(x = 200, y=320)

        efr8 = Entry(find_rec, font=("Courier", 15), width=35)
        efr8.place(x = 200, y=370)

        #inserting in entry boxes

        for record in records_find:
            efr1.insert(0,record[0])
            efr2.insert(0,record[1])
            efr3.insert(0,record[2])
            efr4.insert(0,record[3])
            efr5.insert(0,record[4])
            efr6.insert(0,record[5])
            efr7.insert(0,record[6])
            efr8.insert(0,record[7])

        conn.commit()

        conn.close()

        def s_u_r():
            conn = sqlite3.connect('library.db')
            cursor = conn.cursor() 
            cursor.execute('''UPDATE libs SET 
            NAME = :NAME,
            CLASS = :CLASS,
            ROLL = :ROLL,
            CONTACT = :CONTACT,
            DATE = :DATE,
            TIME = :TIME,
            BNAME = :BNAME,
            BID = :BID''',

            {
            'NAME':efr1.get(),
            'CLASS':efr2.get(),
            'ROLL':efr3.get(),
            'CONTACT':efr4.get(),
            'DATE':efr5.get(),
            'TIME':efr6.get(),
            'BNAME':efr7.get(),
            'BID':efr8.get()
                                
             })

            conn.commit()
            conn.close()

            efr1.delete(0,END)
            efr2.delete(0,END)
            efr3.delete(0,END)
            efr4.delete(0,END)
            efr5.delete(0,END)
            efr6.delete(0,END)
            efr7.delete(0,END)
            efr8.delete(0,END)

            find_rec.destroy()
            update.destroy()

            messagebox.showinfo("UPDATE RECORD" ,"RECORD HAS BEEN UPDATED")

        #button in find_rec----

        bfr1 = Button(find_rec,text="SAVE UPDATED RECORD",height= 2, width=25, command=s_u_r) #sur = save updated record
        bfr1.grid(columnspan = 3, padx = 20, pady=20, ipadx=30)
        bfr1.place(x=225,y=425)

    #button in u_rec-----

    bu1 = Button(update, text= "FIND & UPDATE RECORD",height= 2, width=25, command= find_r)
    bu1.grid(columnspan = 3, padx = 20, pady=20, ipadx=30)
    bu1.place(x=225,y=150)


#buttons-----

b1 = Button(window, text="ADD RECORD" ,height= 2, width=25, command= win_add)
b1.grid(columnspan = 3, padx = 20, pady=20, ipadx=30)
b1.place(x= 90,y = 100)

b2 = Button(window, text= "REMOVE RECORD",height= 2, width=25, command=win_rem)
b2.grid(columnspan = 3, padx = 20, pady=20, ipadx=30)
b2.place(x= 90,y = 150)

b3 = Button(window, text= "SHOW RECORDS",height= 2, width=25, command=show_rec)
b3.grid(columnspan = 3, padx = 20, pady=20, ipadx=30)
b3.place(x= 90,y = 200)

b4= Button(window,text= "UPDATE RECORD",height= 2, width=25, command=u_rec )
b4.grid(columnspan = 3, padx = 20, pady=20, ipadx=30)
b4.place(x= 90,y = 250)

conn.commit()
conn.close()
mainloop()