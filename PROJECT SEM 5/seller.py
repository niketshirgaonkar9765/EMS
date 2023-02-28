from tkinter import * 
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
import re
import sqlite3
    
class SellerClass:
            
    def __init__(self,root):
        self.root=root
        self.root.geometry("1465x530+24+260")
        self.root.title("Electronics Showroom Management System | Developed By Niket")
        self.root.config(bg="white")
        self.root.resizable(False,False)
        self.root.focus_force()
        
#====Variables===================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_sellno=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
    
        
#====search frame================
        searchframe=LabelFrame(self.root,text="Search Seller",font=("callibri",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchframe.place(x=435,y=20,width=600,height=70)
        
        cmb_search=ttk.Combobox(searchframe,textvariable=self.var_searchby,values=("sid","Email","Name","Contact"),font=("callibri",15),state='readonly',justify=CENTER)
        cmb_search.place(x=10,y=8,width=180,height=30)
        cmb_search.set("Select")
        
        self.txt_search=Entry(searchframe,textvariable=self.var_searchtxt,font=("callibri",15),bg='lightyellow')
        self.txt_search.place(x=200,y=8,width=255,height=30)
        
        self.btn_search=Button(searchframe,text="Search",font=("callibri",15,"bold"),bg="#2196f3",fg="black",activebackground="#2196f3",cursor="hand2",command=self.search)
        self.btn_search.place(x=465,y=8,width=110,height=30)
        
#====title=====================
        title=Label(self.root,text="Seller Details",padx=10,compound=CENTER,font=("callibri",20,"bold"),bg="#033054",fg="white").place(x=0,y=100,relwidth=1,height=50)
        
        lbl_sellno=Label(self.root,text="Seller ID.:",font=("callibri",15,'bold'),bg='white').place(x=50,y=160)
        self.txt_sellno=Entry(self.root,textvariable=self.var_sellno,font=("callibri",15),bg='lightyellow')
        self.validate_id= self.root.register(self.checkid)  #validation register
        self.txt_sellno.config(validate = "key",validatecommand = (self.validate_id,"%P"))
        self.txt_sellno.place(x=200,y=160,width=200)
        self.txt_sellno.config(state='readonly')
    
        lbl_name=Label(self.root,text="Seller Name:",font=("callibri",15,'bold'),bg='white').place(x=480,y=160)
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=("callibri",15),bg='lightyellow')
        self.txt_name.place(x=650,y=160,width=350)
        
        lbl_contact=Label(self.root,text="Contact No.:",font=("callibri",15,'bold'),bg='white').place(x=1070,y=160)
        self.txt_contact=Entry(self.root,textvariable=self.var_contact,font=("callibri",15),bg='lightyellow')
        self.txt_contact.place(x=1200,y=160,width=200)
        self.validate_contact= self.root.register(self.checkcontact)  #validation register
        self.txt_contact.config(validate = "key",validatecommand = (self.validate_contact,"%P"))

        lbl_email=Label(self.root,text="Email ID:",font=("callibri",15,'bold'),bg='white').place(x=50,y=210)
        self.txt_email=Entry(self.root,textvariable=self.var_email,font=("callibri",15),bg='lightyellow')
        self.txt_email.place(x=200,y=210,width=350)
        
        lbl_address=Label(self.root,text="Address:",font=("callibri",15,'bold'),bg='white').place(x=630,y=210)
        self.txt_address=Text(self.root,font=("callibri",15),bg='lightyellow')
        self.txt_address.place(x=740,y=210,width=660,height=28)
        
        lbl_gender=Label(self.root,text="Gender:",font=("callibri",15,'bold'),bg='white').place(x=50,y=260)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Male","Female","Other"),font=("callibri",15),state='readonly',justify=CENTER)
        self.txt_gender.place(x=200,y=260,width=150)
        self.txt_gender.set("Select Gender")
        
        lbl_dob=Label(self.root,text="Date of Birth:",font=("callibri",15,'bold'),bg='white').place(x=480,y=260)
        self.txt_dob=DateEntry(self.root,textvariable=self.var_dob,selectmode='day',year=2021,font=("callibri",15),bg='lightyellow',state='readonly')
        self.txt_dob.place(x=630,y=260,width=150)
        
        lbl_doj=Label(self.root,text="Date of Join:",font=("callibri",15,'bold'),bg='white').place(x=950,y=260)
        self.txt_doj=DateEntry(self.root,textvariable=self.var_doj,selectmode='day',year=2021,font=("callibri",15),bg='lightyellow',state='readonly')
        self.txt_doj.place(x=1090,y=260,width=150)
               
        lbl_pass=Label(self.root,text="Password:",font=("callibri",15,'bold'),bg='white').place(x=50,y=310)
        self.txt_pass=Entry(self.root,textvariable=self.var_pass,font=("callibri",15),bg='lightyellow')
        self.txt_pass.place(x=200,y=310,width=200)
        
        lbl_utype=Label(self.root,text="User Type:",font=("callibri",15,'bold'),bg='white').place(x=480,y=310)
        self.txt_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","seller"),font=("callibri",15),state='readonly',justify=CENTER)
        self.txt_utype.place(x=630,y=310,width=150)
        self.txt_utype.set("Select User")
        
        lbl_sal=Label(self.root,text="Salary:",font=("callibri",15,'bold'),bg='white').place(x=950,y=310)
        self.txt_sal=Entry(self.root,textvariable=self.var_salary,font=("callibri",15),bg='lightyellow')
        self.validate_sal= self.root.register(self.checksal)  #validation register
        self.txt_sal.config(validate = "key",validatecommand = (self.validate_sal,"%P"))
        self.txt_sal.place(x=1090,y=310,width=150)
        
#=====Buttons=======================
        self.btn_add=Button(self.root,text="Save",font=("callibri",15,"bold"),bg="#2196f3",activebackground='#2196f3',fg="black",cursor="hand2",command=lambda:[self.add(),self.checkemail(self.var_email)])
        self.btn_add.place(x=510,y=350,width=110,height=30)
        self.btn_update=Button(self.root,text="Update",font=("callibri",15,"bold"),bg="#4caf50",activebackground='#4caf50',fg="black",cursor="hand2",command=self.update)
        self.btn_update.place(x=630,y=350,width=110,height=30)
        self.btn_delete=Button(self.root,text="Delete",font=("callibri",15,"bold"),bg="#f44336",activebackground='#f44336',fg="black",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=750,y=350,width=110,height=30)
        self.btn_clear=Button(self.root,text="Clear",font=("callibri",15,"bold"),bg="#607d8b",activebackground='#607d8b',fg="black",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=870,y=350,width=110,height=30)
 
#=====content========================
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=0,y=400,relwidth=1,height=125)
        
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.SellerTable=ttk.Treeview(self.C_Frame,columns=("Seller ID","Name","Email_ID","Gender","Contact_No","dob","doj","Password","User_Type","Address","Salary"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SellerTable.xview)
        scrolly.config(command=self.SellerTable.yview)
        
        self.SellerTable.heading("Seller ID",text="Seller ID")
        self.SellerTable.heading("Name",text="Name")
        self.SellerTable.heading("Email_ID",text="Email ID")
        self.SellerTable.heading("Gender",text="Gender")
        self.SellerTable.heading("Contact_No",text="Contact No.")
        self.SellerTable.heading("dob",text="D.O.B.")
        self.SellerTable.heading("doj",text="D.O.J.")
        self.SellerTable.heading("Password",text="Password")
        self.SellerTable.heading("User_Type",text="User Type")
        self.SellerTable.heading("Address",text="Address")
        self.SellerTable.heading("Salary",text="Salary")
        self.SellerTable.pack(fill=BOTH,expand=1)
        self.SellerTable["show"]='headings'
        
        self.SellerTable.column("Seller ID",width=90)
        self.SellerTable.column("Name",width=250)
        self.SellerTable.column("Email_ID",width=250)
        self.SellerTable.column("Gender",width=90)
        self.SellerTable.column("Contact_No",width=100)
        self.SellerTable.column("dob",width=90)
        self.SellerTable.column("doj",width=90)
        self.SellerTable.column("Password",width=100)
        self.SellerTable.column("User_Type",width=90)
        self.SellerTable.column("Address",width=400)
        self.SellerTable.column("Salary",width=100)
        self.show()

        self.SellerTable.pack(fill=BOTH,expand=1)
        self.SellerTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#====FUNCTIONS======================
    
    def checkid(self,id):
        if id.isdigit():
            return True
        if len(str(id))== 0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Entry")
            return False
        
    def checkcontact(self,con):
        if con.isdigit():
            return True
        if len(str(con))== 0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Entry")
            return False
    
    def checksal(self,sal):
        if sal.isdigit():
            return True
        if len(str(sal))== 0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Entry")
            return False
        
    
    def checkemail(self,var_email):
        regex=r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex,self.var_email):
            return True
        else:
            messagebox.showwarning("Alert","Invalid E-mail enter by user")
            return False

#====Get Data===================    
    def get_data(self,ev):
        r=self.SellerTable.focus()
        content=self.SellerTable.item(r)
        row=content["values"]
        self.var_sellno.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),   
        self.txt_address.delete("1.0",END),
        self.txt_address.insert(END,row[9]),
        self.var_salary.set(row[10])
        
#====SAVE DATA=================       
    def add(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            #if self.var_sellno.get()=="":
                #messagebox.showerror("Error","Seller ID should be required!",parent=self.root)
            if self.var_name.get()=="":
                messagebox.showerror("Error","Seller name should be required!",parent=self.root)
            elif self.var_email.get()=="":
                messagebox.showerror("Error","Email ID should be required!",parent=self.root)
            elif self.var_contact.get()=="":
                messagebox.showerror("Error","Contact number should be required!",parent=self.root)
            elif len(self.var_contact.get())!=10:
                messagebox.showerror("Error","Contact number should be 10 digits!",parent=self.root)
            elif self.var_pass.get()=="":
                messagebox.showerror("Error","Password should be required!",parent=self.root)
            elif self.var_utype.get()=="Select User":
                messagebox.showerror("Error","User type should be required!",parent=self.root)
            #elif self.var_email.get()!=None:
                #x=self.checkemail(self.var_email.get())
            
            else:
                cur.execute("select * from seller where Name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Seller already exist!",parent=self.root)
                else:
                    cur.execute("insert into seller(Name,Email,Gender,Contact,dob,doj,Password,Usertype,Salary,Address) values(?,?,?,?,?,?,?,?,?,?)",(
                        #self.var_sellno.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.var_salary.get(),
                        self.txt_address.get("1.0",END)
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Seller added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
                 
#====UPDATE DETAILS======================   
    def update(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_sellno.get()=="":
                messagebox.showerror("Error","Please select Seller from the list",parent=self.root)
            else:
                cur.execute("select * from seller where sid=?",(self.var_sellno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select Seller from the list",parent=self.root)
                elif len(self.var_contact.get())!=10:
                    messagebox.showerror("Error","Contact number should be 10 digits!",parent=self.root)
                else:
                    cur.execute("update seller set Name=?,Email=?,Gender=?,Contact=?,dob=?,doj=?,Password=?,Usertype=?,Salary=?,Address=? where sid=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.var_salary.get(),
                        self.txt_address.get("1.0",END),
                        self.var_sellno.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Seller updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#====DELETE DATA===================           
    def delete(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_sellno.get()=="":
                messagebox.showerror("Error","Please select Seller from the list",parent=self.root)
            else:
                cur.execute("select * from seller where sid=?",(self.var_sellno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select Seller from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from seller where sid=?",(self.var_sellno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Seller deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
#====CLEAR DATA======================
    def clear(self):
        self.show()
        self.var_sellno.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select Gender"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set("Select User"),
        self.var_salary.set(""),
        self.txt_address.delete("1.0",END)
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        
        self.show()
        self.txt_sellno.config(state='readonly')
        self.var_searchtxt.set("")
        
#=====SHOW ======================
    def show(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            cur.execute("select * from seller")
            row=cur.fetchall()
            self.SellerTable.delete(*self.SellerTable.get_children())
            for row in row:
                self.SellerTable.insert('',END,values=row)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
           
#====SEARCH========================
    def search(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required!",parent=self.root)
            else:
                cur.execute("select * from seller where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                row=cur.fetchall()
                if len(row)!=0:
                    self.SellerTable.delete(*self.SellerTable.get_children())
                    for row in row:
                        self.SellerTable.insert('',END,values=row)         
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            

if __name__=="__main__": 
    root=Tk()
    obj=SellerClass(root)
    root.mainloop()