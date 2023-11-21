from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import messagebox as mb


x=True
root = Tk()
root.title("Exam System")

root.geometry("1280x720")




def Database():
    global conn, cursor
    conn = sqlite3.connect("db_member.db")
    cursor = conn.cursor()
    #create table students(roll_no int(10), name char(20),class int(10),section char(1));
    #create table member(member_id int(10), username varchar(10), password varchar(10), firstname char(10), lastname char(10));
    cursor.execute("CREATE TABLE IF NOT EXISTS 'member' (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")

USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()

def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=80)

    lab3 = Label(RegisterFrame, text="Create your account", font=('arial bold', 23),fg= "#0b8")
    lab3.grid(row=0,pady=10,columnspan=2,sticky=S)
    
    lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=5, columnspan=2)
    username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=3, column=1)
    lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=4, column=1)
    
    btn_login = Button(RegisterFrame, text="Register", bg= "#0b8",fg="#FFFFFF", font=('Arial Bold', 15), width=30, command=Register)
    btn_login.grid(row=8, columnspan=2,pady=10,sticky=E)
    
    lbl_login = Label(RegisterFrame, text="Sign in to your account",fg="#0b8", font=('Arial Bold', 18))
    lbl_login.grid(row=9,pady=15,columnspan=2,sticky=S)
    
    lbl_login.bind('<Button-1>', ToggleToLogin)

    


def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=100)

    #lab2 = Label(LoginFrame, text="Exami", font=('arial bold', 23),fg= "#0b8")
    #lab2.grid(row=0,pady=10,columnspan=2,sticky=S)
     
    lab1 = Label(LoginFrame, text="Sign in to your account", font=('arial bold', 23),fg= "#0b8")
    lab1.grid(row=1,pady=20,columnspan=2,sticky=S)
    
    lbl_username = Label(LoginFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=2)
    lbl_password = Label(LoginFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=3)
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=2, column=1)
    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3,column=1)
    
    btn_login = Button(LoginFrame, text="Sign in",fg="#FFFFFF",bg= "#0b8", font=('Arial Bold', 15),width=29, command=Login)
    btn_login.grid(row=8, columnspan=2,pady=10,sticky=E)
    
    lbl_register = Label(LoginFrame, text="Create Your Account",fg= "#0b8", font=('Arial Bold', 18))
    lbl_register.grid(row=9,pady=15,columnspan=2,sticky=S)
    
    lbl_register.bind('<Button-1>', ToggleToRegister)

    

def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()
        
def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()
 
def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()





def Register():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "":
        lbl_result2.config(text="Please complete the required field!", fg="blue")

        
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)", (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            FIRSTNAME.set("")
            LASTNAME.set("")
            lbl_result2.config(text="Your account successfully created", fg="green")
        cursor.close()
        conn.close()
            
def Login():
    global b1
    Database()
    
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="red",font=("ariel", 15))
        lbl_result1.place(x=50, y=265)
        
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="", fg="blue")
            lbl_result1.grid()

            root = tk.Tk()
            root.geometry('1280x720')
            root.configure(bg='white')
            label1 = Label(root, text='Welcome In Our Exam System',width=80, bg="#0b8",fg="white", font=("ariel", 20, "bold"))
            label1.place(x=0, y=2)
            b1 = Button(root, text="Start the Exam",font=("ariel bold", 15, "bold"),bg="#CD5C5C",fg="white", width=20, command=lambda:examstart())
            b1.place(x=0, y=50)

            def blink():
                if label4['fg'] == '#0b8':
                    label4.config(fg='white')
                else:
                    label4.config(fg='#0b8')
                root.after(500, blink)                 
     
            label4 = tk.Label(root, text='**Available Now',font=("ariel bold", 10, "bold"),fg="#0b8",bg='white')
            label4.place(x=250, y=58)
            
            root.after(500, blink)
            
            b2 = Button(root, text="Practice for Exam",font=("ariel bold", 15, "bold"),bg="#F08080",fg="white", width=20)
            b2.place(x=0, y=100)
            
            b3 = Button(root, text="Upcoming Exam",font=("ariel bold", 15, "bold"),bg="#FA8072",fg="white", width=20)
            b3.place(x=0, y=150)
            
            b4 = Button(root, text="Past Exam",font=("ariel bold", 15, "bold"),bg="#E9967A",fg="white", width=20)
            b4.place(x=0, y=200)
            
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")
            lbl_result1.grid(row=4)
LoginForm()

def examstart():
    
    root.destroy()
    import part_two.py
'''
def examstart():
    global x
    if x:
        root = tk.Tk()
        root.geometry("600x500")
        label1 = ttk.Label(root, text='Your Exam has been started')
        label1.place(x=5, y=5)
        q1 = radio("What is your name ?",["Sandeep", "Vijay"])
        x=False
'''  
    

'''
menubar = Menu(land)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit me", command=Exit, font=('arial', 10) )
menubar.add_cascade(label="Exit", menu=filemenu, font=('arial', 50))
land.config(menu=menubar)
'''

if __name__ == '__main__':
    root.mainloop()



