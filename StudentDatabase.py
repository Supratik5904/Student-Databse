import sqlite3
from tkinter import*
from tkinter import messagebox as mb
percent=None
equivalentMarks=None
grade=None
totalMarks=300
home=None
root=None
newWindow=None
searchWindow=None
Id=None
Name=None
sec=None
passw=None
name=None
roll=None
presentClass=None
math=None
science=None
english=None
equivalentMarks=None
stud_id=None
printWindow=None
window=Tk()
window.title("Teacher Login")
window.geometry("1000x1000")
window.resizable(0,0)
window.configure()
LB1=Label(window,text="Teacher ID",fg="navy",font=("Arial",14,"bold"))
LB1.grid(row=0,column=2,padx=10,pady=10)
ID=Entry(window,fg="navy",font=("Arial",14,"bold"))
ID.grid(row=0,column=3,padx=10,pady=10)

LB2=Label(window,text="Password",fg="navy",font=("Arial",14,"bold"))
LB2.grid(row=0,column=4,padx=10,pady=10)
Pass=Entry(window,show="*",fg="navy",font=("Arial",14,"bold"))
Pass.grid(row=0,column=5,padx=10,pady=10)

def final():
    global root
    global printWindow
    printWindow.withdraw()
    root.deiconify()

def disp():
    global root
    global searchWindow
    global printWindow
    global stud_id
    global percent
    global grade
    global name
    global roll
    global presentClass
    global math
    global science
    global english
    global equivalentMarks
    s=stud_id.get()
    conn=sqlite3.connect("Student.db")
    rows=conn.execute("select * from student where Roll='"+s+"'")
    count=0
    for row in rows:
        count+=1
        
    if count==1:
        searchWindow.withdraw()
        printWindow=Tk()
        printWindow.resizable(0,0)
        printWindow.geometry("1000x1000")
        printWindow.configure()
        conn=sqlite3.connect("Student.db")
        cur = conn.cursor()
        cur.execute("select * from student")
        for Rows in cur:
            
            lbres1=Label(printWindow,text="Name:"+str(Rows[0]),fg="navy",font=("Arial",14,"bold"))
            lbres1.grid(row=0,column=0,pady=10,padx=10)
            lbres2=Label(printWindow,text="Roll:"+str(Rows[1]),fg="navy",font=("Arial",14,"bold"))
            lbres2.grid(row=0,column=1,pady=10,padx=10)
            lbres3=Label(printWindow,text="Class:"+str(Rows[2]),fg="navy",font=("Arial",14,"bold"))
            lbres3.grid(row=1,column=0,pady=10,padx=10)
            lbres4=Label(printWindow,text="Maths:"+str(Rows[3]),fg="navy",font=("Arial",14,"bold"))
            lbres4.grid(row=1,column=1,pady=10,padx=10)
            lbres5=Label(printWindow,text="Science:"+str(Rows[4]),fg="navy",font=("Arial",14,"bold"))
            lbres5.grid(row=2,column=0,pady=10,padx=10)
            lbres6=Label(printWindow,text="English:"+str(Rows[5]),fg="navy",font=("Arial",14,"bold"))
            lbres6.grid(row=2,column=1,pady=10,padx=10)
            lbres7=Label(printWindow,text="Total Marks:"+str(Rows[6]),fg="navy",font=("Arial",14,"bold"))
            lbres7.grid(row=3,column=0,pady=10,padx=10)
            lbres8=Label(printWindow,text="Grade:"+str(Rows[7]),fg="navy",font=("Arial",14,"bold"))
            lbres8.grid(row=3,column=1,pady=10,padx=10)
        
        
def search():
    global searchWindow
    global root
    global stud_id 
    root.withdraw()
    searchWindow=Tk()
    searchWindow.geometry("1000x1000")
    searchWindow.title("Student Data")
    searchWindow.resizable(0,0)
    searchWindow.configure()
    label=Label(searchWindow,text="Roll",fg="navy",font=("Arial",14,"bold"))
    label.grid(row=0,column=3,padx=10,pady=10)
    stud_id=Entry(searchWindow,fg="navy",font=("Arial",14,"bold"))
    stud_id.grid(row=0,column=4,padx=10,pady=10)
    btn_search=Button(searchWindow,text="Search",fg="navy",font=("Arial",14,"bold"),command=disp) 
    btn_search.grid(row=1,column=4,padx=10,pady=10)
    
            

def withdraw1():
    global newWindow
    global Id
    global Name
    global sec
    global passw
    I=Id.get()
    N=Name.get()
    S=sec.get()
    P=passw.get()
    conn=sqlite3.connect("Teacher.db")
    conn.execute("create table if not exists teacher(ID text primary key,Name text,Section text,password text)")
    row=[(I,N,S,P)]
    conn.executemany("insert into teacher(ID,Name,Section,Password) Values(?,?,?,?)",row)
    conn.commit()

    if conn.total_changes==1:
        mb.showinfo("Success!","Successfully registered")
        newWindow.withdraw()
        window.deiconify()

    

def withdraw():
    global root
    global percent
    global grade
    global totalMarks
    global home
    global name
    global roll
    global presentClass
    global math
    global science
    global english
    global equivalentMarks
    
    n=name.get()
    d=presentClass.get()
    r=roll.get()
    mat=math.get()
    sci=science.get()
    eng=english.get()
    
    conn=sqlite3.connect("Student.db")
    conn.execute("create table if not exists student(Name text, Roll text primary key,Class text,Maths text,Science text,English text,Marks text,Grades text)")
    row=[(n,r,d,mat,sci,eng,equivalentMarks,grade)]
    conn.executemany("insert into student(Name,Roll,Class,Maths,Science,English,Marks,Grades) Values(?,?,?,?,?,?,?,?)",row)
    conn.commit()
    if conn.total_changes==1:
        mb.showinfo("Success!","Successfully entered")
        home.withdraw()
        root.deiconify()

def calculate():
    global percent
    global grade
    global totalMarks
    global home
    global name
    global roll
    global presentClass
    global math
    global science
    global english
    global equivalentMarks
    global grade
    
    

    a=int((math).get())
    b=int((science).get())
    c=int((english).get())
    n=name.get()
    d=presentClass.get()
    r=roll.get()
    mat=math.get()
    sci=science.get()
    eng=english.get()
    root.withdraw()
    home=Tk()
    home.title("Student marks")
    home.geometry("1000x1000")
    home.resizable(0,0)
    home.configure()
    equivalentMarks= a+b+c

    lbres1=Label(home,text="Name:"+n,fg="navy",font=("Arial",14,"bold"))
    lbres1.grid(row=1,column=1,padx=10,pady=10)

    lbres2=Label(home,text="Class:"+d,fg="navy",font=("Arial",14,"bold"))
    lbres2.grid(row=1,column=2,padx=10,pady=10)

    lbres3=Label(home,text="Roll Number:"+r,fg="navy",font=("Arial",14,"bold"))
    lbres3.grid(row=2,column=1,padx=10,pady=10)

    lbres4=Label(home,text="Mathematics:"+mat,fg="navy",font=("Arial",14,"bold"))
    lbres4.grid(row=2,column=2,padx=10,pady=10)

    lbres5=Label(home,text="Science:"+sci,fg="navy",font=("Arial",14,"bold"))
    lbres5.grid(row=3,column=1,padx=10,pady=10)

    lbres6=Label(home,text="English:"+eng,fg="navy",font=("Arial",14,"bold"))
    lbres6.grid(row=3,column=2,padx=10,pady=10)

    
    lb7=Label(home,text="Equivalent Marks:"+str(equivalentMarks),fg="navy",font=("Arial",14,"bold"))
    lb7.grid(row=4,column=1,padx=10,pady=10)
    
    percent=(equivalentMarks/totalMarks)*(100)


    if(percent>=90):
        grade="A"
    elif(90>percent>=80):
        grade="B"
    elif(80>percent>=70):
        grade="C"
    elif(70>percent>=60):
        grade="D"
    elif(60>percent>=50):
        grade="E"
    else:
        grade="F"
        
    lb8=Label(home,text="Grade:"+grade,fg="navy",font=("Arial",14,"bold"))
    lb8.grid(row=4,column=2,padx=10,pady=10)

    btn2=Button(home,text="OK",fg="navy",font=("Arial",14,"bold"),command=withdraw)
    btn2.grid(row=5,column=4,columnspan=2,padx=10,pady=10)


def stud():
    global root
    global name
    global roll
    global presentClass
    global math
    global science
    global english
    id_=ID.get()
    p=Pass.get()
    conn=sqlite3.connect("Teacher.db")
    rows=conn.execute("select * from teacher where ID='"+id_+"' and Password='"+p+"'")
    count=0
    for row in rows:
        count+=1
        
    if count==1:
        window.withdraw()
        root=Tk()
        root.title("Student Datas")
        root.geometry("1000x1000")
        root.resizable(0,0)
        root.configure()

        lb1=Label(root,text="Student Name",fg="navy",font=("Arial",14,"bold"))
        lb1.grid(row=1,column=1,padx=10,pady=10)
        name=Entry(root,fg="navy",font=("Arial",14,"bold"))
        name.grid(row=1,column=2,padx=10,pady=10)

        lb2=Label(root,text="Roll",fg="navy",font=("Arial",14,"bold"))
        lb2.grid(row=1,column=3,padx=10,pady=10)
        roll=Entry(root,fg="navy",font=("Arial",14,"bold"))
        roll.grid(row=1,column=4,padx=10,pady=10)

        lb3=Label(root,text="Class",fg="navy",font=("Arial",14,"bold"))
        lb3.grid(row=2,column=1,padx=10,pady=10)
        presentClass=Entry(root,fg="navy",font=("Arial",14,"bold"))
        presentClass.grid(row=2,column=2,padx=10,pady=10)

        lb4=Label(root,text="Mathematics",fg="navy",font=("Arial",14,"bold"))
        lb4.grid(row=2,column=3,padx=10,pady=10)
        math=Entry(root,fg="navy",font=("Arial",14,"bold"))
        math.grid(row=2,column=4,padx=10,pady=10)

        lb5=Label(root,text="Science",fg="navy",font=("Arial",14,"bold"))
        lb5.grid(row=3,column=1,padx=10,pady=10)
        science=Entry(root,fg="navy",font=("Arial",14,"bold"))
        science.grid(row=3,column=2,padx=10,pady=10)

        lb6=Label(root,text="English",fg="navy",font=("Arial",14,"bold"))
        lb6.grid(row=3,column=3,padx=10,pady=10)
        english=Entry(root,fg="navy",font=("Arial",14,"bold"))
        english.grid(row=3,column=4,padx=10,pady=10)

        btn1=Button(root,text="Enter",fg="navy",font=("Arial",14,"bold"),command=calculate)
        btn1.grid(row=4,column=3,columnspan=2,padx=10,pady=10)

        btns=Button(root,text="Search Data",fg="navy",font=("Arial",14,"bold"),command=search)
        btns.grid(row=6,column=3,columnspan=2,padx=10,pady=10)

    else:
        mb.showerror("Error!","Teacher not registered")



BTN1=Button(window,text="Sign In",fg="navy",font=("Arial",14,"bold"),command=stud)
BTN1.grid(row=2,column=4,padx=10,pady=10)


def signUp():
    global newWindow
    global Id
    global Name
    global sec
    global passw
    window.withdraw()
    newWindow=Tk()
    LB3=Label(newWindow,text="Enter ID",fg="navy",font=("Arial",14,"bold"))
    LB3.grid(row=0,column=1,pady=10,padx=10)
    Id=Entry(newWindow,fg="navy",font=("Arial",14,"bold"))
    Id.grid(row=0,column=2,padx=10,pady=10)

    LB4=Label(newWindow,text="Enter Name",fg="navy",font=("Arial",14,"bold"))
    LB4.grid(row=0,column=3,pady=10,padx=10)
    Name=Entry(newWindow,fg="navy",font=("Arial",14,"bold"))
    Name.grid(row=0,column=4,padx=10,pady=10)

    LB5=Label(newWindow,text="Enter alloted section",fg="navy",font=("Arial",14,"bold"))
    LB5.grid(row=1,column=1,pady=10,padx=10)
    sec=Entry(newWindow,fg="navy",font=("Arial",14,"bold"))
    sec.grid(row=1,column=2,padx=10,pady=10)

    LB6=Label(newWindow,text="Enter Password",fg="navy",font=("Arial",14,"bold"))
    LB6.grid(row=1,column=3,pady=10,padx=10)
    passw=Entry(newWindow,show="*",fg="navy",font=("Arial",14,"bold"))
    passw.grid(row=1,column=4,padx=10,pady=10)

    
    

    BTN3=Button(newWindow,text="Sign Up",fg="navy",font=("Arial",14,"bold"),command=withdraw1)
    BTN3.grid(row=2,column=3,padx=0,pady=10)
    

BTN2=Button(window,text="Sign Up",fg="navy",font=("Arial",14,"bold"),command=signUp)
BTN2.grid(row=4,column=4,padx=0,pady=10)

