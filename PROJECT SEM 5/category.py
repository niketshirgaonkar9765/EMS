from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
class CategoryClass:
    def __init__(self,root): 
        self.root=root
        self.root.title("Electronics Showroom Management System | Developed By Niket")
        self.root.geometry("1465x530+24+260")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)

#====VARIABLES===================
        self.var_catid=StringVar()
        self.var_name=StringVar()
        self.var_searchtxt=StringVar()
        self.var_searchby=StringVar()
#====TITLE======================
        title=Label(self.root,text="Manage Category Details",padx=10,compound=LEFT,font=("callibri",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

#====LABELS======================
        lbl_invoice=Label(self.root,text="Enter Category Name:",font=("callibri",18,'bold'),bg='white').place(x=15,y=70)
        lbl_cid=Label(self.root,text="Category ID:",font=("callibri",18,'bold'),bg='white').place(x=15,y=120)
        
#====ENTRIES=====================
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=("callibri",16,'bold'),bg='lightyellow')
        self.txt_name.place(x=350,y=70,width=400)
        self.txt_cid=Entry(self.root,textvariable=self.var_catid,font=("callibri",16,'bold'),bg='lightyellow')
        self.txt_cid.place(x=350,y=120,width=400)
        self.txt_cid.config(state='readonly')

#====BUTTONS=====================
        self.btn_add=Button(self.root,text="Add",font=("callibri",20,"bold"),bg="#2196f3",activebackground='#2196f3',fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=210,y=180,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("callibri",20,"bold"),bg="#2196f3",activebackground='#2196f3',fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=340,y=180,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("callibri",20,"bold"),bg="#4caf50",activebackground='#4caf50',fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=470,y=180,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("callibri",20,"bold"),bg="#4caf50",activebackground='#4caf50',fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=600,y=180,width=110,height=40)
        
#====search frame================
        searchframe=LabelFrame(self.root,text="Search Category",font=("callibri",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchframe.place(x=800,y=60,width=640,height=70)
        
        cmb_search=ttk.Combobox(searchframe,textvariable=self.var_searchby,values=("cid","name"),font=("callibri",15),state='readonly',justify=CENTER)
        cmb_search.place(x=10,y=8,width=180,height=30)
        cmb_search.set("Select")
        
        self.txt_search=Entry(searchframe,textvariable=self.var_searchtxt,font=("callibri",15),bg='lightyellow')
        self.txt_search.place(x=200,y=8,width=270,height=30)
        
        self.btn_search=Button(searchframe,text="Search",font=("callibri",15,"bold"),bg="#2196f3",fg="white",activebackground="#2196f3",cursor="hand2",command=self.search)
        self.btn_search.place(x=480,y=8,width=130,height=30)
        
#====CONTENT=====================
        self.C_Frame=Frame(self.root,bd=4,relief=RIDGE)
        self.C_Frame.place(x=800,y=140,width=640,height=360)
        
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.categoryTable=ttk.Treeview(self.C_Frame,columns=("cid","name"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)
        
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.heading("cid",text="Category ID")
        self.categoryTable.heading("name",text="Name")
        self.categoryTable["show"]='headings'
        
        self.categoryTable.column("cid",width=100)
        self.categoryTable.column("name",width=250)
        self.categoryTable.pack(fill=BOTH,expand=1)
        
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        
#====IMAGE====================
        self.menulogo=Image.open("images/2.jfif")
        self.menulogo=self.menulogo.resize((390,270),Image.ANTIALIAS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)
        
        self.lbl_bg=Label(self.root,image=self.menulogo).place(x=120,y=230,width=390,height=270)
        
#====FUNCTIONS================
#====ADD DATA=================
    def add(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category name should be required!",parent=self.root)
            else:
                cur.execute("select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already exist!",parent=self.root)
                else:
                    cur.execute("insert into category(name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Category added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
#====UPDATE DATA=================
    def update(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_catid.get()=="":
                messagebox.showerror("Error","Please select Category from the list!",parent=self.root)
            else:
                cur.execute("select * from category where cid=?",(self.var_catid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select Category from the list!",parent=self.root)
                else:
                    cur.execute("update category set name=? where cid=?",(
                        self.var_name.get(),
                        self.var_catid.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Category updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
            
#====DELETE DATA==================
    def delete(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_catid.get()=="":
                messagebox.showerror("Error","Please select Category from the list!",parent=self.root)
            else:
                cur.execute("select * from category where cid=?",(self.var_catid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please try again",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_catid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category deleted Successfully",parent=self.root)
                        self.show()
                        self.var_catid.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
#====CLEAR====================
    def clear(self):
        self.show()
        self.var_catid.set("")
        self.var_name.set("")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.txt_cid.config(state='readonly')
        self.show()
        
        
#====SHOW=====================
    def show(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            row=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in row:
                self.categoryTable.insert('',END,values=row)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
#====GET DATA====================
    def get_data(self,ev):
        r=self.categoryTable.focus()
        content=self.categoryTable.item(r)
        row=content["values"]
        #print(row)
        self.var_catid.set(row[0])
        self.var_name.set(row[1])
            
#====SEARCH======================
    def search(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required!",parent=self.root)
            else:
                cur.execute("select * from category where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                row=cur.fetchall()
                if len(row)!=0:
                    self.categoryTable.delete(*self.categoryTable.get_children())
                    for row in row:
                        self.categoryTable.insert('',END,values=row)         
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
            
if __name__=="__main__":
    root=Tk()
    obj=CategoryClass(root)
    root.mainloop()
