from tkinter import * 
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile

class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1950x1080+-6+-6")
        self.root.title("Electronics Showroom Management System | Developed By Niket")
        self.root.config(bg="white")
        
        self.var_name=StringVar()
        self.cart_list=[]
        self.chk_print=0
        #=================title================
        self.title=Label(self.root,text="ELECTRONICS SHOWROOM MANAGEMENT SYSTEM",font=("callibri",40,"bold"),bg="#010c48",fg="white",padx=20).place(x=0,y=0,relwidth=1,height=90)
        
        self.bg=ImageTk.PhotoImage(file="images/logo.jpg")
        bg=Label(self.title,image=self.bg).place(x=5,y=5,height=90,width=90)
        
        #================logout=============
        btn_logout=Button(self.root,text="Logout",font=("callibri",15,"bold"),bg="yellow",cursor="hand2",command=self.logout).place(x=1460,y=6,height=35,width=80)
        
        #================clock=====================
        self.lbl_clock=Label(self.root,text="Welcome to Electronics Showroom Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("callibri",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=90,relwidth=1,height=30)
        
#====PRODUCT FRAME============================================================
        productframe1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        productframe1.place(x=6,y=130,width=410,height=655)
        
        ptitle=Label(productframe1,text="All Products",font=("callibri",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        
    #====SEARCH FRAME=========================================================
        self.var_search=StringVar()
        productframe2=Frame(productframe1,bd=2,relief=RIDGE,bg="white")
        productframe2.place(x=2,y=42,width=398,height=150)
        
        lbl_search=Label(productframe2,text="Search Product | By Name",font=("callibri",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        
        btn_show=Button(productframe2,text="Show All",font=("callibri",12,"bold"),bg="lightblue",activebackground='lightblue',cursor="hand2",command=self.show).place(x=100,y=100,height=32,width=80)
        btn_search=Button(productframe2,text="Search",font=("callibri",12,"bold"),bg="pink",activebackground='pink',cursor="hand2",command=self.search).place(x=200,y=100,height=32,width=80)
        
        lbl_name=Label(productframe2,text="Product Name:",font=("callibri",15,"bold"),bg="white",fg="black").place(x=2,y=50)
        self.txt_name=Entry(productframe2,textvariable=self.var_search,font=("callibri",15),bg='lightyellow')
        self.txt_name.place(x=150,y=50,width=230)
     
    #====Product frame========================================================
        productframe3=Frame(productframe1,bd=3,relief=RIDGE)
        productframe3.place(x=2,y=200,width=398,height=400)
        
        scrolly=Scrollbar(productframe3,orient=VERTICAL)
        scrollx=Scrollbar(productframe3,orient=HORIZONTAL)
        self.supplierTable=ttk.Treeview(productframe3,columns=("pid","name","price","qty","status"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.heading("pid",text="PID")
        self.supplierTable.heading("name",text="NAME")
        self.supplierTable.heading("price",text="PRICE")
        self.supplierTable.heading("qty",text="QUANTITY")
        self.supplierTable.heading("status",text="STATUS")
        self.supplierTable["show"]='headings'
        
        self.supplierTable.column("pid",width=100)
        self.supplierTable.column("name",width=250)
        self.supplierTable.column("price",width=80)
        self.supplierTable.column("qty",width=80)
        self.supplierTable.column("status",width=60)
        self.supplierTable.pack(fill=BOTH,expand=1)
        
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        
        lbl_note=Label(productframe1,text="Note: 'Enter 0 quantity to remove product from the cart.'",font=("callibri",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
        
#====CUSTOMER FRAME============================================================
        self.var_name=StringVar()
        self.var_contact=StringVar()
        customerframe1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        customerframe1.place(x=420,y=130,width=550,height=75)
        
        ctitle=Label(customerframe1,text="Customer Details",font=("callibri",15,"bold"),bg="lightgray").pack(side=TOP,fill=X)
        
        lbl_name=Label(customerframe1,text="Name:",font=("callibri",15),bg="white",fg="black").place(x=5,y=35)
        self.txt_name=Entry(customerframe1,textvariable=self.var_name,font=("callibri",15),bg='lightyellow')
        self.txt_name.place(x=70,y=35,width=200)
        
        lbl_con=Label(customerframe1,text="Contact No.:",font=("callibri",15),bg="white",fg="black").place(x=280,y=35)
        self.txt_con=Entry(customerframe1,textvariable=self.var_contact,font=("callibri",15),bg='lightyellow')
        self.validate_contact= self.root.register(self.checkcontact)  #validation register
        self.txt_con.config(validate = "key",validatecommand = (self.validate_contact,"%P"))
        self.txt_con.place(x=400,y=35,width=120)
        
#====CALCULATOR AND CART======================================================    
        calcartframe=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        calcartframe.place(x=420,y=220,width=550,height=380)
    
#====CART====================================================================    
        cartframe=Frame(calcartframe,bd=3,relief=RIDGE)
        cartframe.place(x=5,y=6,width=530,height=360)
        self.carttitle=Label(cartframe,text="Cart    Total Products: [0]",font=("callibri",15),bg="lightgray")
        self.carttitle.pack(side=TOP,fill=X)
        
        scrolly=Scrollbar(cartframe,orient=VERTICAL)
        scrollx=Scrollbar(cartframe,orient=HORIZONTAL)
        self.cartTable=ttk.Treeview(cartframe,columns=("pid","name","price","qty"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)
        
        self.cartTable.pack(fill=BOTH,expand=1)
        self.cartTable.heading("pid",text="PRODUCT ID")
        self.cartTable.heading("name",text="NAME")
        self.cartTable.heading("price",text="PRICE")
        self.cartTable.heading("qty",text="QUANTITY")
        self.cartTable["show"]='headings'
        
        self.cartTable.column("pid",width=60)
        self.cartTable.column("name",width=250)
        self.cartTable.column("price",width=80)
        self.cartTable.column("qty",width=50)
        self.cartTable.pack(fill=BOTH,expand=1)
        
        self.cartTable.bind("<ButtonRelease-1>",self.get_data_cart)
        
#=====ADD CART widget frame=========================================
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        
        addcart=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        addcart.place(x=420,y=605,width=550,height=180)
        
        lbl_pname=Label(addcart,text="Product Name",font=("callibri",15),bg="white").place(x=5,y=5)
        self.txt_pname=Entry(addcart,textvariable=self.var_pname,font=("callibri",15),bg='lightyellow',state='readonly')
        self.txt_pname.place(x=5,y=35,width=190,height=25)
        
        lbl_pprice=Label(addcart,text="Price Per Qty",font=("callibri",15),bg="white").place(x=210,y=5)
        self.txt_pprice=Entry(addcart,textvariable=self.var_price,font=("callibri",15),bg='lightyellow',state='readonly')
        self.txt_pprice.place(x=210,y=35,width=150,height=25)
        
        lbl_pqty=Label(addcart,text="Quantity",font=("callibri",15),bg="white").place(x=380,y=5)
        self.txt_pqty=Entry(addcart,textvariable=self.var_qty,font=("callibri",15),bg='lightyellow')
        self.validate_qty= self.root.register(self.checkquantity)  #validation register
        self.txt_pqty.config(validate = "key",validatecommand = (self.validate_qty,"%P"))
        self.txt_pqty.place(x=380,y=35,width=150,height=25)
        
        self.lbl_instock=Label(addcart,text="In Stock:",font=("callibri",20),bg="white")
        self.lbl_instock.place(x=5,y=70)
        
        btn_clear=Button(addcart,text="Clear",font=("callibri",15,"bold"),bg="lightgray",activebackground='lightgray',cursor="hand2",command=self.clear_cart).place(x=100,y=120,height=40,width=150)
        btn_add=Button(addcart,text="Add/Update Cart",font=("callibri",15,"bold"),bg="orange",activebackground='orange',cursor="hand2",command=self.add_update_cart).place(x=270,y=120,height=40,width=180)
        
#==========footer==============
        #footer=Label(self.root,text="NVS Electronics Showroom | Developed By Niket\nFor any technical issues, mail us : shirgaonkarniket14@gmail.com",font=("callibri",12,"bold"),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

#====BILLING AREA=============================================================
        billframe=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        billframe.place(x=975,y=130,width=550,height=470)
        
        btitle=Label(billframe,text="Customer Bill Area",font=("callibri",20,"bold"),bg="#f44336",fg="black").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billframe,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_billarea=Text(billframe,yscrollcommand=scrolly.set) 
        self.txt_billarea.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_billarea.yview)
        
#====BILLING BUTTONS==========================================================
        billmenuframe=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        billmenuframe.place(x=975,y=605,width=550,height=180)
        
        self.lbl_amount=Label(billmenuframe,text="Bill Amount\n0",font=("callibri",15,"bold"),bg="#3f51b5")
        self.lbl_amount.place(x=5,y=5,width=175,height=90)
        self.lbl_discount=Label(billmenuframe,text="Discount\n5%",font=("callibri",15,"bold"),bg="#8bc34a")
        self.lbl_discount.place(x=183,y=5,width=175,height=90)
        self.lbl_net=Label(billmenuframe,text="Net Pay\n0",font=("callibri",15,"bold"),bg="#607d8b")
        self.lbl_net.place(x=361,y=5,width=175,height=90)
        
        btn_print=Button(billmenuframe,text="Print",font=("callibri",15,"bold"),bg="lightgreen",activebackground='lightgreen',cursor="hand2",command=self.print_bill).place(x=5,y=100,height=70,width=175)
        btn_clear=Button(billmenuframe,text="Clear All",font=("callibri",15,"bold"),bg="gray",activebackground='gray',cursor="hand2",command=self.clearall).place(x=183,y=100,height=70,width=175)
        btn_generate=Button(billmenuframe,text="Generate Bill/\nSave Bill",font=("callibri",15,"bold"),bg="#009688",activebackground='#009688',cursor="hand2",command=self.generatebill).place(x=361,y=100,height=70,width=175)
        
#==========footer==============
        footer=Label(self.root,text="Electronics Showroom Management System | Developed By Niket\nFor any technical issues, mail us : nikworld14@gmail.com",font=("callibri",12,"bold"),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.show()
        #self.bill_top()
        self.updatedatetime()
#====FUNCTIONS================================================================
    def checkquantity(self,qua):
        if qua.isdigit():
            return True
        if len(str(qua))== 0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Entry")
            return False
        
    def checkcontact(self,con):
        if con.isdigit():
            return True
        elif len(str(con))== 0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Contact number!")
            return False
        
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        
    def clear_cal(self):
        self.var_cal_input.set('')
        
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
            
    def show(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            #self.supplierTable=ttk.Treeview(productframe3,columns=("pid","name","price","qty","status"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
            cur.execute("select pid,name,price,quantity,status from product where status='Active'")
            row=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in row:
                self.supplierTable.insert('',END,values=row)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    #====SEARCH=========================================================
    def search(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search input should be required!",parent=self.root)
            else:
                cur.execute("select pid,name,price,quantity,status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                row=cur.fetchall()
                if len(row)!=0:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in row:
                        self.supplierTable.insert('',END,values=row)         
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
        
    def get_data(self,ev):
        r=self.supplierTable.focus()
        content=self.supplierTable.item(r)
        row=content["values"]
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_instock.config(text=f"In Stock: {str(row[3])}")
        self.var_stock.set(row[3])
        self.var_qty.set('1')
        
    def get_data_cart(self,ev):
        r=self.cartTable.focus()
        content=self.cartTable.item(r)
        row=content["values"]
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_instock.config(text=f"In Stock: {str(row[4])}")
        self.var_stock.set(row[4])
        
        
        
    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror("Error","Please select product from the list!",parent=self.root)
        elif self.var_qty.get()=='':
            messagebox.showerror("Error","Quantity is required!",parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error","Invalid Quantity!",parent=self.root)
        else:
            #price_cal=(int(self.var_qty.get())*float(self.var_price.get()))
            #price_cal=float(price_cal)
            price_cal=self.var_price.get()
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
            
            #========================update cart===========================
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno('Confirm',"Product already present\nDo you want to update/remove from the cart list",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_qty.get()
            else:
                self.cart_list.append(cart_data)
                
            self.showcart()
            self.bill_update()
            
            
    def bill_update(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
        self.discount=(self.bill_amnt*5)/100
        self.net_pay=self.bill_amnt-self.discount
        self.lbl_amount.config(text=f'Bill Amount\n{str(self.bill_amnt)}')
        self.lbl_net.config(text=f'Net Pay\n{str(self.net_pay)}')
        self.carttitle.config(text=f"Cart    Total Products: [{str(len(self.cart_list))}]")
        
    def showcart(self):
        try:
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cart_list:
                self.cartTable.insert('',END,values=row)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    def generatebill(self):
        if self.var_name.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error","Customer details are required!",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error","Cart is empty!\n Please add product to the cart.")
        else:
            #=====bill TOP=====
            self.bill_top()
            #=====bill MIDDLE=====
            self.bill_middle()
            #=====bill BOTTOM=====
            self.bill_bottom()
            
            fp=open(f'bills/{str(self.invoice)}.txt','w')
            fp.write(self.txt_billarea.get('1.0',END))
            fp.close()
            messagebox.showinfo('Saved',"Bill generated successfully!",parent=self.root)
            self.chk_print=1
        
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t       Electronics Showroom Management System
\t      Phone No.: 9765564101 , Vengurla-416516
{str("="*65)}
 Customer Name: {self.var_name.get()}
 Phone No.:{self.var_contact.get()}
 Invoice NO.: {str(self.invoice)}\t\t\t\t\tDate: {str(time.strftime("%d-%m-%Y"))}
{str("="*65)}\n
 Product Name \t\t\t\tQty  Price(Rs.)  Total Price(Rs.)
{str("="*65)}
        '''
        self.txt_billarea.delete('1.0',END)
        self.txt_billarea.insert('1.0',bill_top_temp)
        
    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*65)}\n
 Bill Amount\t\t\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\t\t\tRs.{self.net_pay}
{str("="*65)}\n
        '''
        self.txt_billarea.insert(END,bill_bottom_temp)
        
    def bill_middle(self):
        con=sqlite3.connect(database="ES.db")
        cur=con.cursor()
        try:
            for row in self.cart_list:
                
                pid=row[0]
                name=row[1]
                quantity=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'
                price=row[2]
                total=float(row[2])*int(row[3])
                total=str(total)
                self.txt_billarea.insert(END,"\n "+name+" \t\t\t\t "+row[3]+"   "+price+"\t\t "+total)
                #======update quantity in product table===========
                cur.execute('update product set quantity=?,status=? where pid=?',(
                    quantity,
                    status,
                    pid
                    ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_instock.config(text=f"In Stock:")
        self.var_stock.set('')
        
    def clearall(self):
        self.chk_print=0
        del self.cart_list[:]
        self.var_name.set('')
        self.var_contact.set('')
        self.txt_billarea.delete('1.0',END)
        self.carttitle.config(text=f"Cart    Total Products: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.showcart()
        
    def updatedatetime(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Electronics Showroom Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(10,self.updatedatetime)
        
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print',"Please wait while printing",parent=self.root)
            newfile=tempfile.mktemp('.txt')
            open(newfile,'w').write(self.txt_billarea.get('1.0',END))
            os.startfile(newfile,'print')
        else:
            messagebox.showerror('Print',"Please generate bill, to print the receipt",parent=self.root)
            
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
            
            
if __name__=="__main__": 
    root=Tk()
    obj=BillClass(root)
    root.mainloop()