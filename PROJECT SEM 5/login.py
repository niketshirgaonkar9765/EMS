from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import os
import email_pass
import smtplib
import time

class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Electronics Showroom Management System | Developed By Niket")
        self.root.geometry("1950x1080+-8+-5")
        self.root.config(bg="snow")
        self.otp=''
        
#=====login frame=====
        self.sellerID=StringVar()
        self.password=StringVar()
        
        frame1=Frame(self.root,bg="azure",borderwidth=4,relief="ridge")
        frame1.place(x=550,y=120,width=450,height=490)
        
        title=Label(frame1,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="azure",fg="black").place(x=0,y=30,relwidth=1)
        
        fname=Label(frame1,text="User ID:",font=("callibri",18,"bold"),bg="azure",fg="black").place(x=20,y=110)
        self.txt_name=Entry(frame1,font=("callibri",18),bg="lightgray")
        self.txt_name.place(x=20,y=160,width=400)
        
        fname=Label(frame1,text="Password:",font=("callibri",18,"bold"),bg="azure",fg="black").place(x=20,y=220)
        self.txt_pass=Entry(frame1,font=("callibri",18),show="*",bg="lightgray")
        self.txt_pass.place(x=20,y=260,width=400)
        
        btn_login=Button(frame1,text="Login",font=("callibri",20,"bold"),bg="blue",fg="White",activebackground='green',activeforeground='white',cursor="hand2",command=self.login)   
        btn_login.place(x=130,y=320,width=180,height=40)
        
        or_=Label(frame1,text="---------------- OR ----------------",font=("callibri",14),bg="azure",fg="black").place(x=0,y=390,relwidth=1)
        btn_forget=Button(frame1,text="Forget Password?",font=("callibri",16,"bold"),borderwidth=0,bg="azure",fg="black",activebackground='white',cursor="hand2",command=self.forgetwin)   #,command=self.forget_pass
        btn_forget.place(x=0,y=430,relwidth=1)
        
        frame2=Frame(self.root,bg="azure",borderwidth=4,relief="ridge")
        frame2.place(x=550,y=630,width=450,height=50)
        
        lbl=Label(frame2,text="Welcome to Electronics Showroom Management System\nDeveloped By Niket",font=("callibri",12,"bold"),bg="azure",fg="black").place(x=0,y=0,relwidth=1,relheight=1)
        
    def login(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        
        try:
            if self.txt_name.get()=="" or self.txt_pass.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select Usertype from seller where sid=? and Password=?",(self.txt_name.get(),self.txt_pass.get(),))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid Username & Password!",parent=self.root)
                    
                else:
                    if user[0]=="Admin":
                        messagebox.showinfo("Success",f"Welcome, {self.txt_name.get()}",parent=self.root)
                        self.root.destroy()
                        os.system("python dashboard.py")#import dashboard
                    else:
                        messagebox.showinfo("Success",f"Welcome, {self.txt_name.get()}",parent=self.root)
                        self.root.destroy()
                        os.system("python billing.py")
                con.close()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            
    def forgetwin(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.txt_name.get()=="":
                messagebox.showerror("Error","User ID must be required!",parent=self.root)
            else:
                cur.execute("select Email from seller where sid=?",(self.txt_name.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid User ID, try again!",parent=self.root)
                else:
                    #=====variables=====
                    self.var_otp=StringVar()
                    self.var_newpass=StringVar()
                    self.var_confirm=StringVar()
                    chk=self.send_email(email[0])
                    if chk!='s':
                        messagebox.showerror("Error","Connection error!,try again.",parent=self.root)
                    else:
                        self.forgetwindow=Toplevel()
                        self.forgetwindow.title("Reset Password")
                        self.forgetwindow.geometry("440x448+550+150")
                        self.forgetwindow.focus_force()
                        self.forgetwindow.grab_set()
                        self.forgetwindow.config(bg="azure")
                        
                        t=Label(self.forgetwindow,text="Reset Password",font=("callibri",20,"bold"),bg="cyan").place(x=0,y=10,relwidth=1)
                        
                        lbl_reset=Label(self.forgetwindow,text="Enter OTP sent on Registered Email ID:",font=("callibri",15),bg="azure",fg="black").place(x=30,y=70)
                        self.txt_otp=Entry(self.forgetwindow,textvariable=self.var_otp,font=("callibri",16),bg="lightgray")
                        self.txt_otp.place(x=30,y=120,width=200,height=30)
                        
                        self.btn_otpconfirm=Button(self.forgetwindow,text="Confirm",font=("callibri",15,"bold"),bg="navy",fg="White",activebackground='navy',activeforeground='white',cursor="hand2",command=self.validateotp)   
                        self.btn_otpconfirm.place(x=250,y=120,width=150,height=30)
                        
                        self.lblnewpass=Label(self.forgetwindow,text="Enter New Password:",font=("callibri",15),bg="azure",fg="black").place(x=30,y=180)
                        self.txt_newpass=Entry(self.forgetwindow,textvariable=self.var_newpass,font=("callibri",16),bg="lightgray",show="*")
                        self.txt_newpass.place(x=30,y=220,width=250)
                        
                        self.lblconfirm=Label(self.forgetwindow,text="Confirm Password:",font=("callibri",15),bg="azure",fg="black").place(x=30,y=270)
                        self.txt_confirm=Entry(self.forgetwindow,textvariable=self.var_confirm,font=("callibri",16),bg="lightgray",show="*")
                        self.txt_confirm.place(x=30,y=310,width=250)
                        
                        self.btn_submit=Button(self.forgetwindow,text="Reset",state=DISABLED,font=("callibri",18,"bold"),bg="navy",fg="White",activebackground='navy',activeforeground='white',cursor="hand2",command=self.updatepass)   
                        self.btn_submit.place(x=140,y=380,width=160,height=40)
                        
                        
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    
    def updatepass(self):
        if self.var_newpass.get()=="" or self.var_confirm.get()=="":
            messagebox.showerror("Error","Password is required!",parent=self.forgetwindow)
        elif self.var_newpass.get()!=self.var_confirm.get():
            messagebox.showerror("Error","New Password and Confirm Password must be same!",parent=self.forgetwindow)
        else:
            con=sqlite3.connect(database="ES.db")
            cur=con.cursor()
            try:
                cur.execute("Update seller SET Password=? where sid=?",(self.var_newpass.get(),self.txt_name.get()))
                con.commit()
                messagebox.showinfo("Success","Password reset successfully!",parent=self.forgetwindow)
                self.forgetwindow.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            
    def validateotp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_submit.config(state=NORMAL)
            self.btn_otpconfirm.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP!",parent=self.forgetwindow)
            
    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_
        s.login(email_,pass_)
        
        self.otp=int(time.strftime("%H%M%S"))
        subj='ES_Reset password OTP'
        msg=f'Dear Sir/Madam, \n\nOTP for Reset Password is {str(self.otp)}.\n\nWith Regards.\n ES Team'
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'
root=Tk()
obj=login_system(root)
root.mainloop()
