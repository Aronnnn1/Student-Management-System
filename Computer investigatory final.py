from tkinter import *
from tkinter import messagebox
import random
import mysql.connector
def createdb():
    mydb1 = mysql.connector.connect(host="localhost",user="root",password="psbe")
    mycursor1=mydb1.cursor()
    mycursor1.execute("create database if not exists prefinal")
    mydb1.commit()
    mycursor1.execute("use prefinal")
    mycursor1.execute("show tables")
    k=mycursor1.fetchall()
    cnt1=0
    cnt2=0
    cnt3=0
    cnt4=0
    for i in k:
        if "pr" in i:
            cnt1+=1
        elif "se" in i:
            cnt2+=1
        elif "p_u" in i:
            cnt3+=1
        elif "fees" in i:
            cnt4+=1
    if cnt1==0:
        mycursor1.execute('''CREATE TABLE pr(ano varchar(5) PRIMARY KEY NOT NULL,
stname varchar(25), class varchar(4), percent varchar(10), gender varchar(8), dob 
date, fname varchar(25), mname varchar(25), fno varchar(10), mno varchar(10), 
fmail varchar(25), mmail varchar(25), fjob varchar(20), mjob varchar(20), al1 
VARCHAR(60), al2 VARCHAR(60), al3 VARCHAR(60), al4 VARCHAR(60), sib 
varchar(25), fees varchar(10))''')
    if cnt2==0:
        mycursor1.execute('''CREATE TABLE se(ano varchar(5) PRIMARY KEY NOT NULL, 
stname varchar(25), class varchar(4), percent varchar(10), gender varchar(8), dob 
date, fname varchar(25), mname varchar(25), fno varchar(10), mno varchar(10), 
fmail varchar(25), mmail varchar(25), fjob varchar(20), mjob varchar(20), al1 
VARCHAR(60), al2 VARCHAR(60), al3 VARCHAR(60), al4 VARCHAR(60), sib 
varchar(25), fees varchar(10))''')
    if cnt3==0:
        mycursor1.execute('''CREATE TABLE p_u(ano varchar(5) PRIMARY KEY NOT NULL, 
stname varchar(25), class varchar(4), percent varchar(10), gender varchar(8), dob 
date, fname varchar(25), mname varchar(25), fno varchar(10), mno varchar(10), 
fmail varchar(25), mmail varchar(25), fjob varchar(20), mjob varchar(20), al1 
VARCHAR(60), al2 VARCHAR(60), al3 VARCHAR(60), al4 VARCHAR(60), sib 
varchar(25), fees varchar(10))''')
    if cnt4==0:
        mycursor1.execute("CREATE TABLE FEES (class varchar(4) PRIMARY KEY, fees varchar(10))")
        mycursor1.execute("insert into FEES(class, fees) values('{}','{}')".format('1','85775'))
        mycursor1.execute("insert into FEES(class, fees) values('{}','{}')".format('2','85775'))
        mycursor1.execute("insert into FEES(class, fees) values('{}','{}')".format('3','86355'))
        mycursor1.execute("insert into FEES(class, fees) values('{}','{}')".format('4','87640'))
        mycursor1.execute("insert into FEES(class, fees) values('{}','{}')".format('5','89970'))
        mycursor1.execute("insert into FEES(class, fees) values('{}','{}')".format('6','94180'))
        mycursor1.execute("insert into FEES(class, fees) values('{}','{}')".format('7','94180'))
        mycursor1.execute("insert into FEES(class, fees) values('{}','{}')".format('8','96120'))
        mycursor1.execute("insert into FEES(class, fees) values('{}','{}')".format('9','97970'))
        mycursor1.execute("insert into FEES(class, fees) values('{}','{}')".format('10','98640'))
        mycursor1.execute("insert into FEES(class, fees) values('{}','{}')".format('11','185090'))
        mycursor1.execute("insert into FEES(class, fees) values('{}','{}')".format('12','137200'))
        mydb1.commit()
createdb()
mydb = mysql.connector.connect(host="localhost",user="root",password="psbe",database="prefinal")
mycursor = mydb.cursor()
master=Tk()
master.title("Welcome Page")
master.geometry("200x200")
user="Admin123"
pwd="Sc_adm@123"
val16=""
ladm=["0"]
admno="0"
l=[]
root=""
root2=""
rt=""
rt1=""
record=""

#To enter student details
def parent():
    master.withdraw()
    global root
    root=Toplevel(master)
    root.geometry('800x800')
    
    root.title("Admission Application Form")
    label=Label(root, text="Admission Application form",width=20,font=("bold", 20))
    label.place(x=220,y=53)
    
    label1=Label(root, text="Student Name",width=26,font=("bold", 10)).place(x=10,y=130)
    parent.entry1=Entry(root,fg="grey",width=25,justify="center")
    parent.entry1.insert(0,"(Full name)")
    parent.entry1.place(x=230,y=130)
    
    
    label2=Label(root, text="Class",width=20,font=("bold", 10)).place(x=10,y=165)
    parent.entry2=Entry(root,fg="grey",width=25,justify="center")
    parent.entry2.insert(0,"(Applying for)")
    parent.entry2.place(x=230,y=165)
    
    
    label3=Label(root, text="Percentage",width=24,font=("bold", 10)).place(x=10,y=200)
    parent.entry3=Entry(root,fg="grey",width=25,justify="center")
    parent.entry3.insert(0,"(previous class)")
    parent.entry3.place(x=230,y=200)
    
    
    label4=Label(root, text="Gender",width=21,font=("bold", 10)).place(x=10,y=235)
    parent.r=StringVar(value='1')
    Radiobutton(root,text="Male",variable=parent.r,value="Male").place(x=225,y=235)
    Radiobutton(root,text="Female",variable=parent.r,value="Female").place(x=285,y=235)
    
    
    label5=Label(root, text="Date of Birth",width=25,font=("bold", 10)).place(x=10,y=270)
    parent.entry5=Entry(root,fg="grey",width=25,justify="center")
    parent.entry5.insert(0,"(YYYY-MM-DD format)")
    parent.entry5.place(x=230,y=270)
   
    
    label6=Label(root, text="Father's Name",width=26,font=("bold", 10)).place(x=10,y=305)
    parent.entry6=Entry(root,fg="grey",width=25,justify="center")
    parent.entry6.insert(0,"(Full name)")
    parent.entry6.place(x=230,y=305)
    
    
    label7=Label(root, text="Mother's Name",width=27,font=("bold", 10)).place(x=10,y=340)
    parent.entry7=Entry(root,fg="grey",width=25,justify="center")
    parent.entry7.insert(0,"(Full name)")
    parent.entry7.place(x=230,y=340)
    
    
    label8=Label(root, text="Father's Number",width=28,font=("bold", 10)).place(x=10,y=375)
    parent.entry8=Entry(root,fg="grey",width=25,justify="center")
    parent.entry8.insert(0,"(10 digit number)")
    parent.entry8.place(x=230,y=375)
    
    
    label9=Label(root, text="Mother's Number",width=28,font=("bold", 10)).place(x=10,y=410)
    parent.entry9=Entry(root,fg="grey",width=25,justify="center")
    parent.entry9.insert(0,"(10 digit number)")
    parent.entry9.place(x=230,y=410)
    
    
    label10=Label(root, text="Father's Occupation",width=30,font=("bold", 10)).place(x=10,y=445)
    parent.entry10=Entry(root,fg="grey",width=25,justify="center")
    parent.entry10.place(x=230,y=445)
    
    
    label11=Label(root, text="Mother's Occupation",width=30,font=("bold", 10)).place(x=10,y=480)
    parent.entry11=Entry(root,fg="grey",width=25,justify="center")
    parent.entry11.place(x=230,y=480)
    

    label12=Label(root, text="Father's Email ID",width=28,font=("bold", 10)).place(x=10,y=515)
    parent.entry12=Entry(root,fg="grey",width=25,justify="center")
    parent.entry12.insert(0,"( ____@____ )")
    parent.entry12.place(x=230,y=515)
    
    
    label13=Label(root, text="Mother's Email ID",width=28,font=("bold", 10)).place(x=10,y=550)
    parent.entry13=Entry(root,fg="grey",width=25,justify="center")
    parent.entry13.insert(0,"( ____@____ )")
    parent.entry13.place(x=230,y=550)
    
    
    label14=Label(root, text="Address",width=21,font=("bold", 10)).place(x=10,y=585)
    parent.entry14_1=Entry(root,fg="grey",width=25,justify="center")
    parent.entry14_2=Entry(root,fg="grey",width=25,justify="center")
    parent.entry14_3=Entry(root,fg="grey",width=25,justify="center")
    parent.entry14_4=Entry(root,fg="grey",width=25,justify="center")
    parent.entry14_4.insert(0,"(City - Pincode)")
    parent.entry14_1.place(x=230,y=585)
    parent.entry14_2.place(x=230,y=605)
    parent.entry14_3.place(x=230,y=625)
    parent.entry14_4.place(x=230,y=645)
    
    
    
    label15=Label(root, text="Name of sibling in school",width=33,font=("bold", 10)).place(x=10,y=680)
    parent.entry15=Entry(root,fg="grey",width=25,justify="center")
    parent.entry15.insert(0,"(Enter none if no siblings)")
    parent.entry15.place(x=230,y=680)
    

    label16=Label(root, text="Project by Aaron B Ajay & Aditi Akella",width=33,font=("bold", 8), fg="#808080").place(x=1,y=760)
    Submit = Button(root, text="Submit", command=sub).place(x=70,y=720)

    root.mainloop()

#To enter login details
def ver():
    master.withdraw()
    global entry1
    global entry2
    global root2
    root2=Toplevel(master)
    root2.geometry("300x250")
    root2.title("Admin Login Page")
    label=Label(root2,text="Admin Login Page",font=("bold", 20)).place(x=40,y=20)
    lab1=Label(root2,text="Username",font=("bold", 13)).place(x=20,y=90)
    entry1=Entry(root2,fg="grey",width=25,justify="center")
    entry1.place(x=110,y=90)
    lab2=Label(root2,text="Password",font=("bold", 13)).place(x=20,y=130)
    entry2=Entry(root2,fg="grey",width=25,justify="center")
    entry2.place(x=110,y=130)
    lab3=Label(root2, text="Project by Aaron B Ajay & Aditi Akella",width=33,font=("bold", 8), fg="#808080").place(x=1,y=220)
    Submit = Button(root2, text="Submit",command=cond).place(x=110,y=170)
    root2.mainloop()

#To verify login details
def cond():
    global user
    global pwd
    global root2
    if user==entry1.get() and pwd==entry2.get():
        choice()
    else:
        messagebox.showinfo("","Incorrect Username or Password")

#To enter admin choice
def choice():
    global root2
    global rt
    root2.withdraw()
    rt=Toplevel(master)
    rt.geometry("300x300")
    rt.title("Admin Page")
    bt1=Button(rt,text="Search student record",command=rec,padx=50,pady=10).place(x=50,y=50)
    bt2=Button(rt,text="Edit student record",command=edit,padx=56,pady=10).place(x=50,y=125)
    bt2=Button(rt,text="Delete student record",command=del1,padx=50,pady=10).place(x=50,y=200)
    
#To enter student name to display record
def rec():
    global rt
    global record
    rt.withdraw()
    record=Toplevel(master)
    record.geometry("320x250")
    record.title("Record Search")
    label=Label(record,text="Record Search",font=("bold", 20)).place(x=50,y=20)
    lab1=Label(record,text="Student Name",font=("bold", 11)).place(x=10,y=90)
    rec.e1=Entry(record,fg="grey",width=25,justify="center")
    rec.e1.place(x=130,y=90)
    Submit = Button(record, text="Submit",command=s1).place(x=110 ,y=140)
    record.mainloop()

#To enter student name to edit record
def edit():
    global rt
    global rt1
    rt.withdraw()
    rt1=Toplevel(master)
    rt1.geometry("320x250")
    rt1.title("Edit Record")
    label=Label(rt1,text="Edit Record",font=("bold", 20)).place(x=50,y=20)
    lab1=Label(rt1,text="Student Name",font=("bold", 11)).place(x=10,y=90)
    edit.e1=Entry(rt1,fg="grey",width=25,justify="center")
    edit.e1.place(x=130,y=90)
    Submit = Button(rt1, text="Submit",command=s2).place(x=110 ,y=140)
    rt1.mainloop()

#To enter student name to delete record
def del1():
    global rt
    global rt1
    rt.withdraw()
    rt1=Toplevel(master)
    rt1.geometry("320x250")
    rt1.title("Delete Record")
    label=Label(rt1,text="Delete Record",font=("bold", 20)).place(x=50,y=20)
    lab1=Label(rt1,text="Student Name",font=("bold", 11)).place(x=10,y=90)
    edit.e1=Entry(rt1,fg="grey",width=25,justify="center")
    edit.e1.place(x=130,y=90)
    Submit = Button(rt1, text="Submit",command=s3).place(x=110 ,y=140)
    rt1.mainloop()

#To insert student record into table 
def add():
    m=None
    if 1<=int(stu_class)<=5:
        query1= """INSERT INTO pr(ano, stname, class, percent, gender, dob, fname, mname, fno, mno, fmail, mmail, fjob, mjob,
al1, al2, al3, al4, sib, fees) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
'{}', '{}', '{}', '{}', '{}')""".format(admno, stu_name, stu_class, percent, gender, dob, fname, mname, fno, mno, fmail, mmail, fjob, mjob, add1, add2, add3, add4, sib, m)
        mycursor.execute(query1)
        query4=("update pr,FEES set pr.fees=FEES.fees where pr.class=FEES.class")
        mycursor.execute(query4)
        mydb.commit()
    elif 6<=int(stu_class)<=10:
        query2= """INSERT INTO se(ano, stname, class, percent, gender, dob, fname, mname, fno, mno, fmail, mmail, fjob, mjob,
al1, al2, al3, al4, sib, fees) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
'{}', '{}', '{}', '{}', '{}', '{}')""".format(admno, stu_name, stu_class, percent, gender, dob, fname, mname, fno, mno, fmail, mmail, fjob, mjob, add1, add2, add3, add4, sib, m)
        mycursor.execute(query2)
        query5=("update se,FEES set se.fees=FEES.fees where se.class=FEES.class")
        mycursor.execute(query5)
        mydb.commit()
    elif 11<=int(stu_class)<=12:
        query3= """INSERT INTO p_u(ano, stname, class, percent, gender, dob, fname, mname, fno, mno, fmail, mmail, fjob, mjob,
al1, al2, al3, al4, sib, fees) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
'{}', '{}', '{}', '{}', '{}')""".format(admno, stu_name, stu_class, percent, gender, dob, fname, mname, fno, mno, fmail, mmail, fjob, mjob, add1, add2, add3, add4, sib, m)
        mycursor.execute(query3)
        query6=("update p_u,FEES set p_u.fees=FEES.fees where p_u.class=FEES.class")
        mycursor.execute(query6)
        mydb.commit()

#To delete student record from table
def delete():
    global rt1
    rt1.withdraw()
    mycursor.execute("select * from pr where ano='{}'".format(l[0],))
    data=mycursor.fetchone()
    if data!=None:
        mycursor.execute("delete from pr where ano='{}'".format(l[0],))
        mydb.commit()
    else:
        mycursor.execute("select * from se where ano='{}'".format(l[0],))
        data=mycursor.fetchone()
        if data!=None:
            mycursor.execute("delete from se where ano='{}'".format(l[0],))
            mydb.commit()
        else:
            mycursor.execute("delete from p_u where ano='{}'".format(l[0],))
            mydb.commit()

#To insert student record into table after editing
def add1():
    global l
    m=None
    delete()
    if 1<=int(l[2])<=5:
        query1= """INSERT INTO pr(ano, stname, class, percent, gender, dob, fname, mname, fno, mno, fmail, mmail, fjob, mjob,
al1, al2, al3, al4, sib, fees) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
'{}', '{}', '{}', '{}', '{}')""".format(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17], l[18], m)
        mycursor.execute(query1)
        query4=("update pr,FEES set pr.fees=FEES.fees where pr.class=FEES.class")
        mycursor.execute(query4)
        mydb.commit()
    elif 6<=int(l[2])<=10:
        query2= """INSERT INTO se(ano, stname, class, percent, gender, dob, fname, mname, fno, mno, fmail, mmail, fjob, mjob,
al1, al2, al3, al4, sib, fees) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}',
'{}', '{}', '{}', '{}', '{}')""".format(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17], l[18], m)
        mycursor.execute(query2)
        query5=("update se,FEES set se.fees=FEES.fees where se.class=FEES.class")
        mycursor.execute(query5)
        mydb.commit()
    elif 11<=int(l[2])<=12:
        query3= """INSERT INTO p_u(ano, stname, class, percent, gender, dob, fname, mname, fno, mno, fmail, mmail, fjob, mjob,
al1, al2, al3, al4, sib, fees) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
'{}', '{}', '{}', '{}', '{}')""".format(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17], l[18], m)
        mycursor.execute(query3)
        query6=("update p_u,FEES set p_u.fees=FEES.fees where p_u.class=FEES.class")
        mycursor.execute(query6)
        mydb.commit()

#To search for student record to display
def s1():
    global l
    global val16
    val16=rec.e1.get()
    q1= (" select * from pr where stname='{}'".format(val16,))
    mycursor.execute(q1)
    data=mycursor.fetchone()
    if data!=None:
        for i in data:
            l.append(i)
        display()
    else:
        q2= (" select * from se where stname='{}'".format(val16,))
        mycursor.execute(q2)
        data=mycursor.fetchone()
        if data!=None:
            for i in data:
                l.append(i)
            display()
        else:
            q3= (" select * from p_u where stname='{}'".format(val16,))
            mycursor.execute(q3)
            data=mycursor.fetchone()
            if data!=None:
                for i in data:
                    l.append(i)
                display()
            else:
                messagebox.showinfo("","Record not found")

#To search for student record to edit
def s2():
    global l
    global val16
    val16=edit.e1.get()
    q1= (" select * from pr where stname='{}'".format(val16,))
    mycursor.execute(q1)
    data=mycursor.fetchone()
    if data!=None:
        for i in data:
            l.append(i)
        disp1()
    else:
        q2= (" select * from se where stname='{}'".format(val16,))
        mycursor.execute(q2)
        data=mycursor.fetchone()
        if data!=None:
            for i in data:
                l.append(i)
            disp1()
        else:
            q3= (" select * from p_u where stname='{}'".format(val16,))
            mycursor.execute(q3)
            data=mycursor.fetchone()
            if data!=None:
                for i in data:
                    l.append(i)
                disp1()
            else:
                messagebox.showinfo("","Record not found")

#To search for student record to delete
def s3():
    global l
    global val16
    val16=edit.e1.get()
    q1= (" select * from pr where stname='{}'".format(val16,))
    mycursor.execute(q1)
    data=mycursor.fetchone()
    if data!=None:
        for i in data:
            l.append(i)
        messagebox.showinfo("","Record deleted")
        delete()
    else:
        q2= (" select * from se where stname='{}'".format(val16,))
        mycursor.execute(q2)
        data=mycursor.fetchone()
        if data!=None:
            for i in data:
                l.append(i)
            messagebox.showinfo("","Record deleted")
            delete()
        else:
            q3= (" select * from p_u where stname='{}'".format(val16,))
            mycursor.execute(q3)
            data=mycursor.fetchone()
            if data!=None:
                for i in data:
                    l.append(i)
                messagebox.showinfo("","Record deleted")
                delete()
            else:
                messagebox.showinfo("","Record not found")
                
b1=Button(master,text="Parent",command=parent,padx=50,pady=10).place(x=30,y=30)
b2=Button(master,text="Admin",command=ver,padx=50,pady=10).place(x=30,y=100)

#Toplevel to edit record
def disp1():
    global rt1
    rt1.withdraw()
    master.withdraw()
    d=Toplevel(master)
    d.geometry('800x800')
    
    d.title("Edit Student Record")
    label=Label(d, text="Edit Student Record",width=20,font=("bold", 20))
    label.place(x=220,y=53)
    
    label1=Label(d, text="Student Name",width=26,font=("bold", 10)).place(x=10,y=130)
    disp1.entry1=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry1.insert(0,l[1])
    disp1.entry1.place(x=230,y=130)
    
    
    label2=Label(d, text="Class",width=20,font=("bold", 10)).place(x=10,y=165)
    disp1.entry2=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry2.insert(0,l[2])
    disp1.entry2.place(x=230,y=165)
    
    
    label3=Label(d, text="Percentage",width=24,font=("bold", 10)).place(x=10,y=200)
    disp1.entry3=Entry(d,fg="#7E7E7E",width=25,justify="center")
    m=list(l[3])
    perc = ''
    for i in m:
        if i.isnumeric():
            perc = perc + i
    k = perc
    disp1.entry3.insert(0,k)
    disp1.entry3.place(x=230,y=200)
    
    
    label4=Label(d, text="Gender",width=21,font=("bold", 10)).place(x=10,y=235)
    disp1.r=StringVar()
    if l[4]=="MALE":
        disp1.r.set("Male")
    else:
        disp1.r.set("Female")
    Radiobutton(d,text="Male",variable=disp1.r,value="Male").place(x=225,y=235)
    Radiobutton(d,text="Female",variable=disp1.r,value="Female").place(x=285,y=235)
    
    
    label5=Label(d, text="Date of Birth",width=25,font=("bold", 10)).place(x=10,y=270)
    disp1.entry5=Entry(d,fg="#AAAAAA",width=25,justify="center")
    disp1.entry5.insert(0,l[5])
    disp1.entry5.place(x=230,y=270)
   
    
    label6=Label(d, text="Father's Name",width=26,font=("bold", 10)).place(x=10,y=305)
    disp1.entry6=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry6.insert(0,l[6])
    disp1.entry6.place(x=230,y=305)
    
    
    label7=Label(d, text="Mother's Name",width=27,font=("bold", 10)).place(x=10,y=340)
    disp1.entry7=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry7.insert(0,l[7])
    disp1.entry7.place(x=230,y=340)
    
    
    label8=Label(d, text="Father's Number",width=28,font=("bold", 10)).place(x=10,y=375)
    disp1.entry8=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry8.insert(0,l[8])
    disp1.entry8.place(x=230,y=375)
    
    
    label9=Label(d, text="Mother's Number",width=28,font=("bold", 10)).place(x=10,y=410)
    disp1.entry9=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry9.insert(0,l[9])
    disp1.entry9.place(x=230,y=410)
    
    
    label10=Label(d, text="Father's Occupation",width=30,font=("bold", 10)).place(x=10,y=445)
    disp1.entry10=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry10.insert(0,l[12])
    disp1.entry10.place(x=230,y=445)
    
    
    label11=Label(d, text="Mother's Occupation",width=30,font=("bold", 10)).place(x=10,y=480)
    disp1.entry11=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry11.insert(0,l[13])
    disp1.entry11.place(x=230,y=480)
    

    label12=Label(d, text="Father's Email ID",width=28,font=("bold", 10)).place(x=10,y=515)
    disp1.entry12=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry12.insert(0,l[10])
    disp1.entry12.place(x=230,y=515)
    
    
    label13=Label(d, text="Mother's Email ID",width=28,font=("bold", 10)).place(x=10,y=550)
    disp1.entry13=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry13.insert(0,l[11])
    disp1.entry13.place(x=230,y=550)
       
    label14=Label(d, text="Address",width=21,font=("bold", 10)).place(x=10,y=585)
    disp1.entry14_1=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry14_2=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry14_3=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry14_4=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry14_1.insert(0,l[14])
    disp1.entry14_2.insert(0,l[15])
    disp1.entry14_3.insert(0,l[16])
    disp1.entry14_4.insert(0,l[17])
    disp1.entry14_1.place(x=230,y=585)
    disp1.entry14_2.place(x=230,y=605)
    disp1.entry14_3.place(x=230,y=625)
    disp1.entry14_4.place(x=230,y=645)
        
    label15=Label(d, text="Name of sibling in school",width=33,font=("bold", 10)).place(x=10,y=680)
    disp1.entry15=Entry(d,fg="#7E7E7E",width=25,justify="center")
    disp1.entry15.insert(0,l[18])
    disp1.entry15.place(x=230,y=680)
    
    Submit = Button(d, text="Submit", command=sub1).place(x=70,y=720)

    d.mainloop()
    
#To display student record
def display():
    global l
    global record
    record.withdraw()
    r2=Toplevel(master)
    r2.geometry('800x750')
    
    r2.title("Record Display")
    label=Label(r2, text="Student Record Display",width=20,font=("bold", 20))
    label.place(x=220,y=53)
    
    la1=Label(r2, text="Admission Number",width=26,font=("bold", 10)).place(x=10,y=130)
    la2=Label(r2, text=l[0])
    la2.place(x=230,y=130)
    
    la3=Label(r2, text="Student Name",width=23,font=("bold", 10)).place(x=10,y=160)
    la4=Label(r2, text=l[1])
    la4.place(x=230,y=160)

    
    la5=Label(r2, text="Class",width=17,font=("bold", 10)).place(x=10,y=190)
    la6=Label(r2, text=l[2])
    la6.place(x=230,y=190)
    
    la7=Label(r2, text="Percentage",width=21,font=("bold", 10)).place(x=10,y=220)
    la8=Label(r2, text=l[3])
    la8.place(x=230,y=220)
    
    la9=Label(r2, text="Gender",width=18,font=("bold", 10)).place(x=10,y=250)
    la10=Label(r2, text=l[4])
    la10.place(x=230,y=250)
    
    la11=Label(r2, text="Date of Birth",width=22,font=("bold", 10)).place(x=10,y=280)
    la12=Label(r2, text=l[5])
    la12.place(x=230,y=280)
    
    la13=Label(r2, text="Father's Name",width=24,font=("bold", 10)).place(x=10,y=310)
    la14=Label(r2, text=l[6])
    la14.place(x=230,y=310)
    
    la15=Label(r2, text="Mother's Name",width=24,font=("bold", 10)).place(x=10,y=340)
    la16=Label(r2, text=l[7])
    la16.place(x=230,y=340)
    
    la17=Label(r2, text="Father's Number",width=25,font=("bold", 10)).place(x=10,y=370)
    la18=Label(r2, text=l[8])
    la18.place(x=230,y=370)
    
    la19=Label(r2, text="Mother's Number",width=25,font=("bold", 10)).place(x=10,y=400)
    la20=Label(r2, text=l[9])
    la20.place(x=230,y=400)
    
    la21=Label(r2, text="Father's Email ID",width=25,font=("bold", 10)).place(x=10,y=430)
    la22=Label(r2, text=l[10])
    la22.place(x=230,y=430)

    la23=Label(r2, text="Mother's Email ID",width=25,font=("bold", 10)).place(x=10,y=460)
    la24=Label(r2, text=l[11])
    la24.place(x=230,y=460)

    la25=Label(r2, text="Father's Occupation",width=27,font=("bold", 10)).place(x=10,y=490)
    la26=Label(r2, text=l[12])
    la26.place(x=230,y=490)
    
    la27=Label(r2, text="Mother's Occupation",width=27,font=("bold", 10)).place(x=10,y=520)
    la28=Label(r2, text=l[13])
    la28.place(x=230,y=520)
    
    la29=Label(r2, text="Address",width=18,font=("bold", 10)).place(x=10,y=550)
    la30=Label(r2, text=l[14])
    la31=Label(r2, text=l[15])
    la32=Label(r2, text=l[16])
    la33=Label(r2, text=l[17])
    la30.place(x=230,y=550)
    la31.place(x=230,y=570)
    la32.place(x=230,y=590)
    la33.place(x=230,y=610)

    la34=Label(r2, text="Name of sibling in school",width=30,font=("bold", 10)).place(x=10,y=640)
    la35=Label(r2, text=l[18])
    la35.place(x=230,y=640)

    la36=Label(r2, text="Fees",width=15,font=("bold", 10)).place(x=10,y=670)
    la37=Label(r2, text=l[19])
    la37.place(x=230,y=670)

def chkfloat(k):
    try:
        float(k)
        return ("1")
    except ValueError:
        return ("0")

#To validate entry fields when entering student record
def sub():
    global stu_name
    stu_name=parent.entry1.get().upper()
    l=stu_name.split()
    for x in l:
        if not(x.isalpha()):
            messagebox.showinfo("","Invalid Student Name")
            break
    else:
        global stu_class
        stu_class=parent.entry2.get()
        if not(stu_class.isdigit()) or int(stu_class)<1 or int(stu_class) >12:
            messagebox.showinfo("","Invalid Class")
        else:
            global percent
            percent=parent.entry3.get()
            if chkfloat(percent)=="0" or float(percent)<0.0 or float(percent)>100.0:
                messagebox.showinfo("","Invalid Percent")
            else:
                percent=str(percent)+"%"
                global gender
                gender=parent.r.get().upper()
                global dob
                dob=parent.entry5.get()
                l=dob.split("-")
                if not(l[0].isdigit()) or not(l[1].isdigit()) or not(l[2].isdigit()) or len(l[0])!=4 or len(l[1])!=2 or len(l[2])!=2 or int(l[0])<2000 or int(l[1])<1 or int(l[1])>12 or int(l[2])<1 or int(l[2])>31:
                    messagebox.showinfo("","Invalid Date of Birth")
                    
                else:
                    global fname
                    fname=parent.entry6.get().upper()
                    l=fname.split()
                    for x in l:
                        if not(x.isalpha()):
                            messagebox.showinfo("","Invalid Father Name")
                            break
                    else:
                        global mname
                        mname=parent.entry7.get().upper()
                        l=mname.split()
                        for x in l:
                            if not(x.isalpha()):
                                messagebox.showinfo("","Invalid Mother Name")
                                break
                        else:
                            global fno
                            fno=parent.entry8.get()
                            if len(fno)!=10 or not(fno.isdigit()):
                                messagebox.showinfo("","Invalid Father Phone Number")
                                
                            else:
                                global mno
                                mno=parent.entry9.get()
                                if len(mno)!=10 or not(fno.isdigit()):
                                    messagebox.showinfo("","Invalid Mother Phone Number")
                                    
                                else:
                                    global fjob
                                    fjob=parent.entry10.get().upper()
                                    l=fjob.split()
                                    for x in l:
                                        if not(x.isalpha()):
                                            messagebox.showinfo("","Invalid Father Occupation")
                                            break
                                    else:
                                        global mjob
                                        mjob=parent.entry11.get().upper()
                                        l=mjob.split()
                                        for x in l:
                                            if not(x.isalpha()):
                                                messagebox.showinfo("","Invalid Mother Occupation")
                                                break
                                        else:
                                            global fmail
                                            fmail=parent.entry12.get()
                                            if "@" not in fmail or ".com" not in fmail:
                                                messagebox.showinfo("","Invalid Father E-mail ID")
                                                
                                            else:
                                                global mmail
                                                mmail=parent.entry13.get()
                                                if "@" not in mmail or ".com" not in mmail:
                                                    messagebox.showinfo("","Invalid Mother E-mail ID")
                                                    
                                                else:
                                                    global add1
                                                    add1=parent.entry14_1.get()
                                                    global add2
                                                    add2=parent.entry14_2.get()
                                                    global add3
                                                    add3=parent.entry14_3.get()
                                                    global add4
                                                    add4=parent.entry14_4.get()
                                                    global sib
                                                    sib=parent.entry15.get().upper()
                                                    l=sib.split()
                                                    for x in l:
                                                        if not(x.isalpha()):
                                                            messagebox.showinfo("","Invalid Sibling Name")
                                                            
                                                    else:
                                                        global ladm
                                                        global admno
                                                        while admno in ladm:
                                                            admno=str(random.randint(1000,10000))
                                                        ladm.append(admno)
                                                        add()
                                                        messagebox.showinfo("","Thank you! Record added")

#To validate entry fields when editing student record
def sub1():
    global l
    l[1]=disp1.entry1.get().upper()
    m=l[1].split()
    for x in m:
        if not(x.isalpha()):
            messagebox.showinfo("","Invalid Student Name")
            break
    else:
        l[2]=disp1.entry2.get()
        if not(l[2].isdigit()) or int(l[2])<1 or int(l[2]) >12:
            messagebox.showinfo("","Invalid Class")
        else:
            l[3]=disp1.entry3.get()
            if chkfloat(l[3])=="0" or float(l[3])<0.0 or float(l[3])>100.0:
                messagebox.showinfo("","Invalid Percent")
            else:
                l[3]=str(l[3])+"%"
                l[4]=disp1.r.get().upper()
                l[5]=disp1.entry5.get()
                m=l[5].split("-")
                if not(m[0].isdigit()) or not(m[1].isdigit()) or not(m[2].isdigit()) or len(m[0])!=4 or len(m[1])!=2 or len(m[2])!=2 or int(m[0])<2000 or int(m[1])<1 or int(m[1])>12 or int(m[2])<1 or int(m[2])>31:
                    messagebox.showinfo("","Invalid Date of Birth")
                    
                else:
                    l[6]=disp1.entry6.get().upper()
                    m=l[6].split()
                    for x in m:
                        if not(x.isalpha()):
                            messagebox.showinfo("","Invalid Father Name")
                            break
                    else:
                        l[7]=disp1.entry7.get().upper()
                        m=l[7].split()
                        for x in m:
                            if not(x.isalpha()):
                                messagebox.showinfo("","Invalid Mother Name")
                                break
                        else:
                            l[8]=disp1.entry8.get()
                            if len(l[8])!=10 or not(l[8].isdigit()):
                                messagebox.showinfo("","Invalid Father Phone Number")
                                
                            else:
                                l[9]=disp1.entry9.get()
                                if len(l[9])!=10 or not(l[9].isdigit()):
                                    messagebox.showinfo("","Invalid Mother Phone Number")
                                    
                                else:
                                    l[12]=disp1.entry10.get().upper()
                                    m=l[12].split()
                                    for x in m:
                                        if not(x.isalpha()):
                                            messagebox.showinfo("","Invalid Father Occupation")
                                            break
                                    else:
                                        l[13]=disp1.entry11.get().upper()
                                        m=l[13].split()
                                        for x in m:
                                            if not(x.isalpha()):
                                                messagebox.showinfo("","Invalid Mother Occupation")
                                                break
                                        else:
                                            l[10]=disp1.entry12.get()
                                            if "@" not in l[10] :
                                                messagebox.showinfo("","Invalid Father E-mail ID")
                                                
                                            else:
                                                l[11]=disp1.entry13.get()
                                                if "@" not in l[11]:
                                                    messagebox.showinfo("","Invalid Mother E-mail ID")
                                                    
                                                else:
                                                    l[14]=disp1.entry14_1.get()
                                                    l[15]=disp1.entry14_2.get()
                                                    l[16]=disp1.entry14_3.get()
                                                    l[17]=disp1.entry14_4.get()
                                                    l[18]=disp1.entry15.get().upper()
                                                    m=l[18].split()
                                                    for x in m:
                                                        if not(x.isalpha()):
                                                            messagebox.showinfo("","Invalid Sibling Name")
                                                    else:
                                                        add1()
                                                        messagebox.showinfo("","Record updated")
                                                        
master.mainloop()


stu_name=""
stu_class=""
percent=""
gender=""
dob=""
fname=""
mname=""
fno=""
mno=""
fmail=""
mmail=""
fjob=""
mjob=""
add1=""
add2=""
add3=""
add4=""
sib=""
mydb.close()
