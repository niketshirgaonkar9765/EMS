from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import os
import sqlite3
class SalesClass:
    def __init__(self,root): 
        self.root=root
        self.root.title("Electronics Showroom Management System | Developed By Niket")
        self.root.geometry("1465x530+24+260")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)
        
        self.bill_list=[]
        self.var_invoice=StringVar()
#====TITLE==================       
        title=Label(self.root,text="Customer Bill Reports",padx=10,compound=LEFT,font=("callibri",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

#====WIDGETS================     
        lbl_inno=Label(self.root,text="Invoice Number:",font=("callibri",18,'bold'),bg='white').place(x=30,y=70)
        self.txt_inno=Entry(self.root,textvariable=self.var_invoice,font=("callibri",18),bg='lightyellow')
        self.validate_inv= self.root.register(self.checkinvoice)  #validation register
        self.txt_inno.config(validate = "key",validatecommand = (self.validate_inv,"%P"))
        self.txt_inno.place(x=250,y=70,width=300)
        
#====BUTTONS=================
        self.btn_search=Button(self.root,text="Search",font=("callibri",18,"bold"),bg="#2196f3",activebackground='#2196f3',fg="black",cursor="hand2",command=self.search)
        self.btn_search.place(x=590,y=70,width=110,height=32)
        self.btn_clr=Button(self.root,text="Clear",font=("callibri",18,"bold"),bg="lightgray",activebackground='lightgray',fg="black",cursor="hand2",command=self.clear)  
        self.btn_clr.place(x=710,y=70,width=110,height=32)
        
#====SALES FRAME================       
        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=140,width=230,height=350)
        
        scrolly=Scrollbar(sales_frame,orient=VERTICAL)
        self.sales_list=Listbox(sales_frame,font=("callibri",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)
#====BILL FRAME===================
        bill_frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=320,y=140,width=550,height=350)
        
        title2=Label(bill_frame,text="Customer Bill Area",font=("callibri",20,"bold"),bg="orange").pack(side=TOP,fill=X)
        
        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.billarea=Text(bill_frame,bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.billarea.yview)
        self.billarea.pack(fill=BOTH,expand=1)
        
#====IMAGE=====================
        self.bill_img=Image.open("images/bills.jfif")
        self.bill_img=self.bill_img.resize((510,440),Image.ANTIALIAS)
        self.bill_img=ImageTk.PhotoImage(self.bill_img)
        
        self.lbl_bg=Label(self.root,image=self.bill_img).place(x=920,y=80,width=510,height=440)
        
        self.show()
        
#======================================
    def checkinvoice(self,inv):
        if inv.isdigit():
            return True
        if len(str(inv))== 0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Invoice number!",parent=self.root)
            return False
        
    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        #print(os.listdir('bills'))
        for i in os.listdir('bills'):
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
                
    def get_data(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        #print(file_name)
        self.billarea.delete('1.0',END)
        fp=open(f'bills/{file_name}','r')
        for i in fp:
            self.billarea.insert(END,i)
        fp.close()
        
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice number should be required!",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bills/{self.var_invoice.get()}.txt','r')
                self.billarea.delete('1.0',END)
                for i in fp:
                    self.billarea.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid invoice number!",parent=self.root)
        
    def clear(self):
        self.show()
        self.var_invoice.set("")
        self.billarea.delete('1.0',END)
        
if __name__=="__main__":
    root=Tk()
    obj=SalesClass(root)
    root.mainloop()
