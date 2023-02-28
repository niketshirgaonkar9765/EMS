from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
class ProductClass:
    def __init__(self,root): 
        self.root=root
        self.root.title("Electronics Showroom Management System | Developed By Niket")
        self.root.geometry("1465x530+24+260")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)

#====VARIABLES================================================================
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_pid=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        product_frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=620,height=510)
        
        title=Label(product_frame,text="Manage Product Details",padx=10,compound=LEFT,font=("callibri",20,"bold"),bg="#033054",fg="white").pack(side=TOP,fill=X)
        
        lbl_product=Label(product_frame,text="Category:",font=("callibri",18,'bold'),bg='white').place(x=30,y=60)
        lbl_supplier=Label(product_frame,text="Supplier:",font=("callibri",18,'bold'),bg='white').place(x=30,y=120)
        lbl_name=Label(product_frame,text="Name of Product:",font=("callibri",18,'bold'),bg='white').place(x=30,y=180)
        lbl_pid=Label(product_frame,text="Product ID:",font=("callibri",18,'bold'),bg='white').place(x=30,y=240)
        lbl_price=Label(product_frame,text="Price:",font=("callibri",18,'bold'),bg='white').place(x=30,y=300)
        lbl_qty=Label(product_frame,text="Quantity:",font=("callibri",18,'bold'),bg='white').place(x=30,y=360)
        lbl_status=Label(product_frame,text="Status:",font=("callibri",18,'bold'),bg='white').place(x=30,y=420)
        
        self.txt_category=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,font=("callibri",18),state='readonly',justify=CENTER)
        self.txt_category.place(x=280,y=60,width=300)
        self.txt_category.current(0)
        
        self.txt_supplier=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.sup_list,font=("callibri",18),state='readonly',justify=CENTER)
        self.txt_supplier.place(x=280,y=120,width=300)
        self.txt_supplier.current(0)
        
        self.txt_name=Entry(product_frame,textvariable=self.var_name,font=("callibri",18),bg='lightyellow')
        self.txt_name.place(x=280,y=180,width=300)
        
        self.txt_pid=Entry(product_frame,textvariable=self.var_pid,font=("callibri",18),bg='lightyellow')
        self.txt_pid.place(x=280,y=240,width=300)
        self.txt_pid.config(state='readonly')
        
        self.txt_price=Entry(product_frame,textvariable=self.var_price,font=("callibri",18),bg='lightyellow')
        self.validate_price= self.root.register(self.checkprice)  #validation register
        self.txt_price.config(validate = "key",validatecommand = (self.validate_price,"%P"))
        self.txt_price.place(x=280,y=300,width=300)
        
        self.txt_qty=Entry(product_frame,textvariable=self.var_qty,font=("callibri",18),bg='lightyellow')
        self.validate_qty= self.root.register(self.checkquantity)  #validation register
        self.txt_qty.config(validate = "key",validatecommand = (self.validate_qty,"%P"))
        self.txt_qty.place(x=280,y=360,width=300)
        
        self.txt_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"),font=("callibri",18),state='readonly',justify=CENTER)
        self.txt_status.place(x=280,y=420,width=300)
        self.txt_status.set("Select Status")
        
#====BUTTONS==================================================================
        self.btn_add=Button(self.root,text="Add",font=("callibri",20,"bold"),bg="#2196f3",activebackground='#2196f3',fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=70,y=475,width=110,height=35)
        self.btn_update=Button(self.root,text="Update",font=("callibri",20,"bold"),bg="#2196f3",activebackground='#2196f3',fg="white",cursor="hand2",command=self.update)  
        self.btn_update.place(x=200,y=475,width=110,height=35)
        self.btn_delete=Button(self.root,text="Delete",font=("callibri",20,"bold"),bg="#4caf50",activebackground='#4caf50',fg="white",cursor="hand2",command=self.delete)  
        self.btn_delete.place(x=330,y=475,width=110,height=35)
        self.btn_clear=Button(self.root,text="Clear",font=("callibri",20,"bold"),bg="#4caf50",activebackground='#4caf50',fg="white",cursor="hand2",command=self.clear)  
        self.btn_clear.place(x=460,y=475,width=110,height=35)
        
       
        
#====search frame================================================
        searchframe=LabelFrame(self.root,text="Search Product",font=("callibri",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchframe.place(x=670,y=10,width=760,height=70)
        
        cmb_search=ttk.Combobox(searchframe,textvariable=self.var_searchby,values=("category","supplier","name"),font=("callibri",15),state='readonly',justify=CENTER)
        cmb_search.place(x=10,y=8,width=220,height=30)
        cmb_search.set("Select")
        
        self.txt_search=Entry(searchframe,textvariable=self.var_searchtxt,font=("callibri",15),bg='lightyellow')
        self.txt_search.place(x=250,y=8,width=290,height=30)
        
        self.btn_search=Button(searchframe,text="Search",font=("callibri",15,"bold"),bg="#2196f3",fg="white",activebackground="#2196f3",cursor="hand2",command=self.search)   
        self.btn_search.place(x=560,y=8,width=130,height=30)
        
#====CONTENT=================================================================
        self.C_Frame=Frame(self.root,bd=4,relief=RIDGE)
        self.C_Frame.place(x=670,y=100,width=760,height=419)
        
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.productTable=ttk.Treeview(self.C_Frame,columns=("pid","category","supplier","name","price","quantity","status"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.heading("pid",text="Product ID")
        self.productTable.heading("category",text="Category")
        self.productTable.heading("supplier",text="Supplier")
        self.productTable.heading("name",text="Product name")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("quantity",text="Quantity")
        self.productTable.heading("status",text="Status")
        self.productTable["show"]='headings'
        
        self.productTable.column("pid",width=80)
        self.productTable.column("category",width=270)
        self.productTable.column("supplier",width=100)
        self.productTable.column("name",width=350)
        self.productTable.column("price",width=70)
        self.productTable.column("quantity",width=70)
        self.productTable.column("status",width=70)
        self.productTable.pack(fill=BOTH,expand=1)
        
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        
    def checkprice(self,price):
        if price.isdigit():
            return True
        if len(str(price))== 0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid price",parent=self.root)
            return False
        
    def checkquantity(self,qua):
        if qua.isdigit():
            return True
        if len(str(qua))== 0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid quantity",parent=self.root)
            return False
        
        
        
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            cur.execute("select name from category")
            cat=cur.fetchall() 
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select Category")
                for i in cat:
                    self.cat_list.append(i[0])
            
            cur.execute("select name from supplier")
            sup=cur.fetchall()        
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select Supplier")
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
            
    #====SAVE DATA===================================        
    def add(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_sup.get()=="Empty" or self.var_name.get()=="" or self.var_price.get()=="" or self.var_qty.get()=="" or self.var_status.get()=="Select Status":
                messagebox.showerror("Error","All fields should be required!",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product already exist!",parent=self.root)
                else:
                    cur.execute("insert into product(category,supplier,name,price,quantity,status) values(?,?,?,?,?,?)",(
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Product added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
                 
#====UPDATE DETAILS========================================        
    def update(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please select Product from list!",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select Product from list!",parent=self.root)
                else:
                    cur.execute("update product set category=?,supplier=?,name=?,price=?,quantity=?,status=? where pid=?",(
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_pid.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Product updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#====DELETE DATA===================================================            
    def delete(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please select Product from the list!",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select Product from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete product?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
#====CLEAR DATA======================================================
    def clear(self):
        self.show()
        self.var_cat.set("Select Category"),
        self.var_sup.set("Select Supplier"),
        self.var_name.set(""),
        self.var_pid.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Select"),

        self.var_searchby.set("Select Status")
        self.var_searchtxt.set("")
        
        self.show()
        #self.txt_empno.config(state=NORMAL)
        self.var_search.set("")
        
#=====SHOW ====================================================
    def show(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            row=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in row:
                self.productTable.insert('',END,values=row)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
#====GET DATA=================================================================
    def get_data(self,ev):
        r=self.productTable.focus()
        content=self.productTable.item(r)
        row=content["values"]
        #print(row)
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_pid.set(row[0])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
           
#====SEARCH=========================================================
    def search(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required!",parent=self.root)
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                row=cur.fetchall()
                if len(row)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in row:
                        self.productTable.insert('',END,values=row)         
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
            
        
if __name__=="__main__":
    root=Tk()
    obj=ProductClass(root)
    root.mainloop()
