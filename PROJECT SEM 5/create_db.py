import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ES.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS seller(sid INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Email text,Gender text,Contact text,dob text,doj text,Password text,Usertype text,Address text,Salary text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,email text,desc text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name tex)")
    con.commit()
                                                                       
    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,category text,supplier text,name text,price text,quantity text,status text)")
    con.commit()
create_db()
    
    

