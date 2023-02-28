from tkinter import * 
from PIL import Image,ImageTk
from seller import SellerClass
from supplier import SupplierClass
from category import CategoryClass
from product import ProductClass
from sales import SalesClass
import sqlite3
from tkinter import messagebox
import os
import time

class ES:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1950x1080+-8+-6")
        self.root.title("Electronics Showroom Management System | Developed By Niket")
        self.root.config(bg="white")
        
#=================title================
        self.title=Label(self.root,text="ELECTRONICS SHOWROOM MANAGEMENT SYSTEM",font=("callibri",40,"bold"),bg="#010c48",fg="white",padx=20).place(x=0,y=0,relwidth=1,height=130)
        
        self.bg=ImageTk.PhotoImage(file="images/logo.jpg")
        bg=Label(self.title,image=self.bg).place(x=5,y=15,height=90,width=90)
        
#================logout=============
        btn_logout=Button(self.root,text="Logout",font=("callibri",15,"bold"),bg="yellow",activebackground='yellow',cursor="hand2",command=self.logout).place(x=1460,y=6,height=35,width=80)
        
#================clock=====================
        self.lbl_clock=Label(self.root,text="Welcome to Electronics Showroom Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("callibri",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=130,relwidth=1,height=30)
        
#================Menubar================
        self.menulogo=Image.open("images/1.jpeg")
        self.menulogo=self.menulogo.resize((550,499),Image.ANTIALIAS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)
        
        self.lbl_bg=Label(self.root,image=self.menulogo).place(x=15,y=250,width=550,height=499)
        
        menu=LabelFrame(self.root,text="Menus",font=("times new roman",15),bd=2,relief=RIDGE,bg="white")
        menu.place(x=8,y=160,width=1520,height=80)
        
        btn_seller=Button(menu,text="Seller",font=("callibri",18,"bold"),bg="#0b5377",fg="white",activebackground="#0b5377",activeforeground='white',cursor="hand2",command=self.seller).place(x=25,y=1,width=215,height=40)
        btn_supplier=Button(menu,text="Supplier",font=("callibri",18,"bold"),bg="#0b5377",fg="white",activebackground="#0b5377",activeforeground='white',cursor="hand2",command=self.supplier).place(x=275,y=1,width=215,height=40)
        btn_category=Button(menu,text="Category",font=("gcallibri",18,"bold"),bg="#0b5377",fg="white",activebackground="#0b5377",activeforeground='white',cursor="hand2",command=self.category).place(x=525,y=1,width=215,height=40)
        btn_products=Button(menu,text="Products",font=("callibri",18,"bold"),bg="#0b5377",fg="white",activebackground="#0b5377",activeforeground='white',cursor="hand2",command=self.product).place(x=775,y=1,width=215,height=40)
        btn_sales=Button(menu,text="Sales",font=("callibri",18,"bold"),bg="#0b5377",fg="white",activebackground="#0b5377",activeforeground='white',cursor="hand2",command=self.sales).place(x=1025,y=1,width=215,height=40)
        btn_exit=Button(menu,text="Exit",font=("callibri",18,"bold"),bg="#0b5377",fg="white",activebackground="#0b5377",activeforeground='white',cursor="hand2",command=self.exit_).place(x=1275,y=1,width=215,height=40)
        
#=====update details======
        self.lbl_seller=Label(self.root,text="Total Sellers\n0",font=("callibri",25,"bold"),bd=10,relief=RIDGE,bg="slateblue",fg="white")
        self.lbl_seller.place(x=550,y=300,width=300,height=200)
        
        self.lbl_supplier=Label(self.root,text="Total Suppliers\n0",font=("callibri",25,"bold"),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_supplier.place(x=860,y=260,width=300,height=200)
        
        self.lbl_category=Label(self.root,text="Total Categories\n0",font=("callibri",25,"bold"),bd=10,relief=RIDGE,bg="indigo",fg="white")
        self.lbl_category.place(x=1170,y=300,width=300,height=200)
        
        self.lbl_product=Label(self.root,text="Total Products\n0",font=("callibri",25,"bold"),bd=10,relief=RIDGE,bg="navy",fg="white")
        self.lbl_product.place(x=700,y=520,width=300,height=200)
        
        self.lbl_sales=Label(self.root,text="Total Sales\n0",font=("callibri",25,"bold"),bd=10,relief=RIDGE,bg="hotpink",fg="white")
        self.lbl_sales.place(x=1010,y=520,width=300,height=200)
        
#==========footer==============
        footer=Label(self.root,text="Electronics Showroom Management System | Developed By Niket\nFor any technical issues, mail us : nikworld14@gmail.com",font=("callibri",12,"bold"),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.updatedashboard()
        self.updatedatetime()
        
#===========Functions=====================
    def seller(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SellerClass(self.new_win)
        
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SupplierClass(self.new_win)
        
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CategoryClass(self.new_win)
        
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ProductClass(self.new_win)
        
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SalesClass(self.new_win)
        
    def updatedashboard(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f"Total Products\n{str(len(product))}")  
            
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Suppliers\n{str(len(supplier))}")
            
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f"Total Categories\n{str(len(category))}")
            
            cur.execute("select * from seller")
            seller=cur.fetchall()
            self.lbl_seller.config(text=f"Total Sellers\n{str(len(seller))}")
            
            bill=len(os.listdir('bills'))
            self.lbl_sales.config(text=f'Total Sales\n{str(bill)}')
            
            self.lbl_product.after(10,self.updatedashboard)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def updatedatetime(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Electronics Showroom Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(10,self.updatedatetime)
        
    def exit_(self):
        oj=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if oj==True:
            self.root.destroy()
            
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
        
if __name__=="__main__": 
    root=Tk()
    obj=ES(root)
    root.mainloop()