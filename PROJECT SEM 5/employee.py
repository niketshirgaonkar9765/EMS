from tkinter import * 
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import ttk,messagebox
import sqlite3

class employeeclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1465x530+24+250")
        self.root.title("Inventory Management System | Developed By Niket")
        self.root.config(bg="white")
        self.root.resizable(False,False)
        self.root.focus_force()
        
#====Variables==================================================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_empno=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        
#====search frame================================================
        searchframe=LabelFrame(self.root,text="Search Employee",font=("callibri",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchframe.place(x=435,y=20,width=600,height=70)
        
        cmb_search=ttk.Combobox(searchframe,textvariable=self.var_searchby,values=("eid","Email","Name","Contact"),font=("callibri",15),state='readonly',justify=CENTER)
        cmb_search.place(x=10,y=8,width=180,height=30)
        cmb_search.set("Select")
        
        self.txt_search=Entry(searchframe,textvariable=self.var_searchtxt,font=("callibri",15),bg='lightyellow')
        self.txt_search.place(x=200,y=8,width=255,height=30)
        
        self.btn_search=Button(searchframe,text="Search",font=("callibri",15,"bold"),bg="#2196f3",fg="black",activebackground="#2196f3",cursor="hand2",command=self.search)
        self.btn_search.place(x=465,y=8,width=110,height=30)
        
#====title======================================================
        title=Label(self.root,text="Employee Details",padx=10,compound=CENTER,font=("callibri",20,"bold"),bg="#033054",fg="white").place(x=0,y=100,relwidth=1,height=50)
        
        lbl_empno=Label(self.root,text="Employee No.:",font=("callibri",15,'bold'),bg='white').place(x=50,y=160)
        self.txt_empno=Entry(self.root,textvariable=self.var_empno,font=("callibri",15),bg='lightyellow')
        self.txt_empno.place(x=200,y=160,width=200)
        
        lbl_name=Label(self.root,text="Employee Name:",font=("callibri",15,'bold'),bg='white').place(x=480,y=160)
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=("callibri",15),bg='lightyellow')
        self.txt_name.place(x=650,y=160,width=350)
        
        lbl_contact=Label(self.root,text="Contact No.:",font=("callibri",15,'bold'),bg='white').place(x=1070,y=160)
        self.txt_contact=Entry(self.root,textvariable=self.var_contact,font=("callibri",15),bg='lightyellow')
        self.txt_contact.place(x=1200,y=160,width=200)
        
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
        self.txt_dob=Entry(self.root,textvariable=self.var_dob,font=("callibri",15),bg='lightyellow')
        self.txt_dob.place(x=630,y=260,width=150)
        
        lbl_doj=Label(self.root,text="Date of Join:",font=("callibri",15,'bold'),bg='white').place(x=950,y=260)
        self.txt_doj=Entry(self.root,textvariable=self.var_doj,font=("callibri",15),bg='lightyellow')
        self.txt_doj.place(x=1090,y=260,width=150)
        
        lbl_pass=Label(self.root,text="Password:",font=("callibri",15,'bold'),bg='white').place(x=50,y=310)
        self.txt_pass=Entry(self.root,textvariable=self.var_pass,font=("callibri",15),bg='lightyellow')
        self.txt_pass.place(x=200,y=310,width=200)
        
        lbl_utype=Label(self.root,text="User Type:",font=("callibri",15,'bold'),bg='white').place(x=480,y=310)
        self.txt_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),font=("callibri",15),state='readonly',justify=CENTER)
        self.txt_utype.place(x=630,y=310,width=150)
        self.txt_utype.set("Select User")
        
        
        lbl_sal=Label(self.root,text="Salary:",font=("callibri",15,'bold'),bg='white').place(x=950,y=310)
        self.txt_sal=Entry(self.root,textvariable=self.var_salary,font=("callibri",15),bg='lightyellow')
        self.txt_sal.place(x=1090,y=310,width=150)
        
#=====Buttons=============================================
        self.btn_add=Button(self.root,text="Save",font=("callibri",15,"bold"),bg="#2196f3",activebackground='#2196f3',fg="black",cursor="hand2",command=self.add)
        self.btn_add.place(x=510,y=350,width=110,height=30)
        self.btn_update=Button(self.root,text="Update",font=("callibri",15,"bold"),bg="#4caf50",activebackground='#4caf50',fg="black",cursor="hand2",command=self.update)
        self.btn_update.place(x=630,y=350,width=110,height=30)
        self.btn_delete=Button(self.root,text="Delete",font=("callibri",15,"bold"),bg="#f44336",activebackground='#f44336',fg="black",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=750,y=350,width=110,height=30)
        self.btn_clear=Button(self.root,text="Clear",font=("callibri",15,"bold"),bg="#607d8b",activebackground='#607d8b',fg="black",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=870,y=350,width=110,height=30)
 
#=====content===============================================
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=0,y=400,relwidth=1,height=125)
        
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.EmpTable=ttk.Treeview(self.C_Frame,columns=("Emp ID","Name","Email_ID","Gender","Contact_No","dob","doj","Password","User_Type","Address","Salary"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmpTable.xview)
        scrolly.config(command=self.EmpTable.yview)
        

        self.EmpTable.heading("Emp ID",text="Emp ID")
        self.EmpTable.heading("Name",text="Name")
        self.EmpTable.heading("Email_ID",text="Email ID")
        self.EmpTable.heading("Gender",text="Gender")
        self.EmpTable.heading("Contact_No",text="Contact No.")
        self.EmpTable.heading("dob",text="D.O.B.")
        self.EmpTable.heading("doj",text="D.O.J.")
        self.EmpTable.heading("Password",text="Password")
        self.EmpTable.heading("User_Type",text="User Type")
        self.EmpTable.heading("Address",text="Address")
        self.EmpTable.heading("Salary",text="Salary")
        self.EmpTable.pack(fill=BOTH,expand=1)
        self.EmpTable["show"]='headings'
        
        self.EmpTable.column("Emp ID",width=90)
        self.EmpTable.column("Name",width=250)
        self.EmpTable.column("Email_ID",width=250)
        self.EmpTable.column("Gender",width=90)
        self.EmpTable.column("Contact_No",width=100)
        self.EmpTable.column("dob",width=90)
        self.EmpTable.column("doj",width=90)
        self.EmpTable.column("Password",width=100)
        self.EmpTable.column("User_Type",width=90)
        self.EmpTable.column("Address",width=400)
        self.EmpTable.column("Salary",width=100)
        self.show()

        self.EmpTable.pack(fill=BOTH,expand=1)
        self.EmpTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#====FUNCTIONS====================================

#====Get Data=====================================      
    def get_data(self,ev):
        r=self.EmpTable.focus()
        content=self.EmpTable.item(r)
        row=content["values"]
        self.var_empno.set(row[0]),
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
        
#====SAVE DATA===================================        
    def add(self):
        con=sqlite3.connect(database="IMS.db")
        cur=con.cursor()
        try:
            if self.var_empno.get()=="":
                messagebox.showerror("Error","Employee ID should be required!",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_empno.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Employee ID already exist!",parent=self.root)
                else:
                    cur.execute("insert into employee(eid,Name,Email,Gender,Contact,dob,doj,Password,Usertype,Salary,Address) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_empno.get(),
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
                    messagebox.showinfo("Success","Employee added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
                 
#====UPDATE DETAILS========================================        
    def update(self):
        con=sqlite3.connect(database="IMS.db")
        cur=con.cursor()
        try:
            if self.var_empno.get()=="":
                messagebox.showerror("Error","Employee ID should be required!",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_empno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select employee from list",parent=self.root)
                else:
                    cur.execute("update employee set Name=?,Email=?,Gender=?,Contact=?,dob=?,doj=?,Password=?,Usertype=?,Salary=?,Address=? where eid=?",(
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
                        self.var_empno.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Employee updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#====DELETE DATA===================================================            
    def delete(self):
        con=sqlite3.connect(database="IMS.db")
        cur=con.cursor()
        try:
            if self.var_empno.get()=="":
                messagebox.showerror("Error","Employee ID should be required!",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_empno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select Employee from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_empno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
#====CLEAR DATA======================================================
    def clear(self):
        self.show()
        self.var_empno.set(""),
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
        self.txt_empno.config(state=NORMAL)
        self.var_search.set("")
        
#=====SHOW ====================================================
    def show(self):
        con=sqlite3.connect(database="IMS.db")
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            row=cur.fetchall()
            self.EmpTable.delete(*self.EmpTable.get_children())
            for row in row:
                self.EmpTable.insert('',END,values=row)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
           
#====SEARCH=========================================================
    def search(self):
        con=sqlite3.connect(database="IMS.db")
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required!",parent=self.root)
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                row=cur.fetchall()
                if len(row)!=0:
                    self.EmpTable.delete(*self.EmpTable.get_children())
                    for row in row:
                        self.EmpTable.insert('',END,values=row)         
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
            
            
if __name__=="__main__": 
    root=Tk()
    obj=employeeclass(root)
    root.mainloop()