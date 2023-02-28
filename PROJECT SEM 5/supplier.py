from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class SupplierClass:
    def __init__(self,root): 
        self.root=root
        self.root.title("Electronics Showroom Management System | Developed By Niket")
        self.root.geometry("1465x530+24+260")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)
        
#====TITLE================
        title=Label(self.root,text="Manage Supplier Details",padx=10,compound=LEFT,font=("callibri",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        
#====VARIABLES============
        self.var_invoice=StringVar()
        self.var_supplier=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_searchtxt=StringVar()
        
#====LABELS================
        lbl_invoice=Label(self.root,text="Invoice No.:",font=("callibri",15,'bold'),bg='white').place(x=15,y=70)
        lbl_supplier=Label(self.root,text="Supplier Name:",font=("callibri",15,'bold'),bg='white').place(x=15,y=115)
        lbl_contact=Label(self.root,text="Contact No.:",font=("callibri",15,'bold'),bg='white').place(x=15,y=160)
        lbl_email=Label(self.root,text="Email ID:",font=("callibri",15,'bold'),bg='white').place(x=15,y=205)
        lbl_description=Label(self.root,text="Description:",font=("callibri",15,'bold'),bg='white').place(x=15,y=250)
#====ENTRIES===============
        self.txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("callibri",15,'bold'),bg='lightyellow')
        self.validate_inv= self.root.register(self.checkinvoice)  #validation register
        self.txt_invoice.config(validate = "key",validatecommand = (self.validate_inv,"%P"))
        self.txt_invoice.config(state='readonly')
        self.txt_invoice.place(x=175,y=70,width=300)
        
        self.txt_supplier=Entry(self.root,textvariable=self.var_supplier,font=("callibri",15,'bold'),bg='lightyellow')
        self.txt_supplier.place(x=175,y=115,width=300)
        
        self.txt_contact=Entry(self.root,textvariable=self.var_contact,font=("callibri",15,'bold'),bg='lightyellow')
        self.validate_contact= self.root.register(self.checkcontact)  #validation register
        self.txt_contact.config(validate = "key",validatecommand = (self.validate_contact,"%P"))
        self.txt_contact.place(x=175,y=160,width=300)
        
        self.txt_email=Entry(self.root,textvariable=self.var_email,font=("callibri",15,'bold'),bg='lightyellow')
        self.txt_email.place(x=175,y=205,width=300)
        
        self.txt_description=Text(self.root,font=("callibri",15,'bold'),bg='lightyellow')
        self.txt_description.place(x=175,y=250,width=500,height=130)
         
#====BUTTONS=================
        self.btn_add=Button(self.root,text="Save",font=("callibri",15,"bold"),bg="#2196f3",activebackground='#2196f3',fg="black",cursor="hand2",command=self.add)
        self.btn_add.place(x=175,y=420,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("callibri",15,"bold"),bg="#4caf50",activebackground='#4caf50',fg="black",cursor="hand2",command=self.update)
        self.btn_update.place(x=295,y=420,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("callibri",15,"bold"),bg="#f44336",activebackground='#f44336',fg="black",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=415,y=420,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("callibri",15,"bold"),bg="#607d8b",activebackground='#607d8b',fg="black",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=535,y=420,width=110,height=40)
        
#====SEARCH PANEL=============
        self.var_search=StringVar()
        lbl_search=Label(self.root,text="Invoice No.:",font=("callibri",15,'bold'),bg='white').place(x=750,y=70)
        self.txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("callibri",15,'bold'),bg='lightyellow')
        self.validate_inv= self.root.register(self.checkinvoice1)  #validation register
        self.txt_search.config(validate = "key",validatecommand = (self.validate_inv,"%P"))
        self.txt_search.place(x=870,y=70,width=180)
        
        btn_search=Button(self.root,text="Search",font=("callibri",15,"bold"),bg="#03a9f4",activebackground='#03a9f4',fg="black",cursor="hand2",command=self.search)
        btn_search.place(x=1070,y=70,width=120,height=28)
        
#====CONTENT==================
        self.C_Frame=Frame(self.root,bd=4,relief=RIDGE)
        self.C_Frame.place(x=750,y=120,width=640,height=345)
        
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.supplierTable=ttk.Treeview(self.C_Frame,columns=("invoice","name","contact","email","desc"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.heading("invoice",text="Invoice Number")
        self.supplierTable.heading("name",text="Supplier")
        self.supplierTable.heading("contact",text="Contact No.")
        self.supplierTable.heading("email",text="Email ID")
        self.supplierTable.heading("desc",text="Description")
        self.supplierTable["show"]='headings'
        
        self.supplierTable.column("invoice",width=100)
        self.supplierTable.column("name",width=250)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("email",width=250)
        self.supplierTable.column("desc",width=300)
        self.supplierTable.pack(fill=BOTH,expand=1)
        
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#====FUNCTIONS=================

    def checkinvoice(self,inv):
        if inv.isdigit():
            return True
        if len(str(inv))== 0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Invoice number!",parent=self.root)
            return False
        
    def checkinvoice1(self,inv):
        if inv.isdigit():
            return True
        if len(str(inv))== 0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Invoice number!",parent=self.root)
            return False
        
    def checkcontact(self,con):
        if con.isdigit():
            return True
        if len(str(con))== 0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Contact number!",parent=self.root)
            return False

#====SAVE DATA=================        
    def add(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            #if self.var_invoice.get()=="":
                #messagebox.showerror("Error","Invoice number should be required!",parent=self.root)
            if self.var_supplier.get()=="":
                messagebox.showerror("Error","Supplier name should be required!",parent=self.root)
            elif self.var_email.get()=="":
                messagebox.showerror("Error","Email ID should be required!",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice number already exist!",parent=self.root)
                else:
                    cur.execute("insert into supplier(name,contact,email,desc) values(?,?,?,?)",(
                        #self.var_invoice.get(),
                        self.var_supplier.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.txt_description.get("1.0",END)
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
#====UPDATE DATA===============
    def update(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_invoice.get()=="":
                messagebox.showerror("Error","Please select Supplier from the list",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select Supplier from the list",parent=self.root)
                else:
                    cur.execute("update supplier set name=?,contact=?,email=?,desc=? where invoice=?",(
                        self.var_supplier.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.txt_description.get("1.0",END),
                        self.var_invoice.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
#====DELETE DATA==============
    def delete(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_invoice.get()=="":
                messagebox.showerror("Error","Please select Supplier from the list",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select Supplier from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
#====CLEAR==============
    def clear(self):
        self.show()
        self.var_invoice.set("")
        self.var_supplier.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.txt_description.delete('1.0',END)
        #self.txt_invoice.config(state=NORMAL)
        self.txt_invoice.config(state='readonly')
        self.var_searchtxt.set("")
        self.show()
        
#====GET DATA============
    def get_data(self,ev):
        self.txt_invoice.config(state='readonly')
        r=self.supplierTable.focus()
        content=self.supplierTable.item(r)
        row=content["values"]
        #print(row)
        self.var_invoice.set(row[0])
        self.var_supplier.set(row[1])
        self.var_contact.set(row[2])
        self.var_email.set(row[3])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])
        
#====SHOW===============
    def show(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            row=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in row:
                self.supplierTable.insert('',END,values=row)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
#====SEARCH=============
    def search(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice number should be required!",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)         
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
if __name__=="__main__":
    root=Tk()
    obj=SupplierClass(root)
    root.mainloop()