from tkinter import *
from tkinter import messagebox as ms
import sqlite3

import sys#this module provides acces to some variables that are ben maintained and used strongly nby the inmterpretor


with sqlite3.connect('practice.db') as db:
    c=db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS cst_login
            (fullname TEXT,
             username TEXT NOT NULL,
             email TEXT ,
             password TEXT NOT NULL);''')
print("TABLE created")
db.commit()
db.close()
class main:
    def __init__(self,master):

        self.master=master
        self.fullname=StringVar()
        self.username=StringVar()
        self.password=StringVar()
        self.email=StringVar()
        self.n_fullname=StringVar()
        self.n_username=StringVar()
        self.n_password=StringVar()
        self.n_email=StringVar()
        self.widgets()#create widgets
        

    def cst_login(self):
        while True:
            with sqlite3.connect("practice.db") as db:
                c=db.cursor()
            f_user=('SELECT * from cst_login WHERE username= ? AND password= ?')
            c.execute(f_user,[(self.username.get()),(self.password.get())])
            res=c.fetchall()
            if res:
               for i in res:
                   print("Login Success!",'\n')
                   print("Welcome "+i[0],'\n')
               break
            else:
                ms.showerror("Username and Password are not recognised",'\n')
                repeat=input("Do want to try again?(Y/N)")
                if repeat.lower()=="n":
                    break
                
        
    def cst_new_user(self):
            with sqlite3.connect('practice.db') as db:
                c=db.cursor()
            f_user=('select * from cst_login where username = ?');
            c.execute(f_user,[(self.username.get())])
            if c.fetchall():
                ms.showerror("Oops! Username Taken!!",'\n')
            else:
                 ms.showinfo("Succesfully Account Created!",'\n')
                 self.log()
            insertdata=('''INSERT INTO cst_login(fullname,username,email,password)VALUES (?,?,?,?)''');
            c.execute(insertdata,[(self.fullname.get()),(self.username.get()),(self.password.get()),(self.email.get())])
            db.commit()
        #Frame packing methods
       
    def log(self):
        self.fullname.set('')
        self.username.set('')
        self.password.set('')
        self.email.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_fullname.set('')
        self.n_username.set('')
        self.n_password.set('')
        self.n_email.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Fullname: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.fullname,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Label(self.logf,text = 'Password ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15)).grid(row=1,column=1)
        Label(self.logf,text = ' Email',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.email,bd = 5,font = ('',15)).grid(row=1,column=1)
        
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cst_login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()

        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Fullname: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.fullname,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=1,column=1)
        Label(self.crf,text = ' password ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Label(self.crf,text = ' Email',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.email,bd = 5,font = ('',15)).grid(row=1,column=1)
       
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cst_new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)

    

if __name__ == '__main__':
	#Create Object
	#and setup window
    root = Tk()
    root.title('Login Form')
    #root.geometry('400x350+300+300')
    main(root)
    root.mainloop()






