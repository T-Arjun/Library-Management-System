import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector as sql

from tkinter import Entry, Tk
import tkinter.messagebox as MessageBox

root=Tk()
root.geometry('600x500')
root.configure(bg='gray26')
root.resizable(False,False)
#c.execute('''create table books
#         (book_code integer(3) not NULL primary key,
#          book_name varchar(50),
#          price int(3),
#          status varchar(2) ''')
    
# adding data to table books    

def add_to_books():
    root1=Toplevel()
    root1.geometry('600x250')
    Label(root1,text='BOOK DETAILS',font=20,pady=10).grid(row=0,column=1)

    bookcode=Label(root1,text='Book Code').grid(row=1,column=0)
    bookcode=Entry(root1,width=60)
    bookcode.grid(row=1,column=1) 

    book_name=Label(root1,text='Book Name').grid(row=2,column=0)
    name=Entry(root1,width=60) 
    name.grid(row=2,column=1)

    Price=Label(root1,text='Price').grid(row=3,column=0)
    price=Entry(root1,width=60)
    price.grid(row=3,column=1) 


    passwd=Label(root1,text='Password' ).grid(row=5,column=0)
    passwd=Entry(root1,width=60,show = "*")
    passwd.grid(row=5,column=1)


    def add():
    #connection setup
        conn=sql.connect(host='localhost',user='root',passwd =passwd.get(),auth_plugin='mysql_native_password')                                     
        if conn.is_connected():
            print('Succesfully conected.')
        else:
            print('ERROR! connecting the server.')
        c=conn.cursor()
        c.execute('use library')
        c.execute('''insert into books(book_code,book_name,price) 
                values({},'{}',{})'''.format(int(bookcode.get()),name.get(),int(price.get())))
        
        conn.commit()
        c.close()
        conn.close()
        
        bookcode.delete(0,'end')
        name.delete(0,'end')
        price.delete(0,'end')
        MessageBox.showinfo("Insert Status" ,"inserted Successfully");

    button_ok=Button(root1,text='OK',padx=7,pady=7,bg='#add8e6',command=add).grid(row=6,column=1)
    

  
        


#DATA ENTRY FOR TABLE books



def search_name_window():
    rare=Toplevel()
    rare.geometry('600x250')

    Label(rare,text='BORROWER DETAILS',font=20,pady=10).grid(row=0,column=1)

    book_code=Label(rare,text='BOOK_CODE').grid(row=1,column=0)
    code=Entry(rare,width=60)
    code.grid(row=1,column=1) 

    borrower_name=Label(rare,text='NAME').grid(row=2,column=0)
    name=Entry(rare,width=60)
    name.grid(row=2,column=1)



def del_window():
    new_window = Toplevel(root)
    new_window.geometry('250x150')
   
    lbl = Label(new_window , text="this is new window")
    
    
    Label(new_window,text='DELETE',font=20).grid(row=0,column=5)
    Label(new_window,text='   ',).grid(row=1,column=3)
    Label(new_window,text='CODE').grid(row=1,column=4)
    code=Entry(new_window,width=20)
    code.grid(row=1,column=5)




    password=Label(new_window,text='Password',font=20).grid(row=7,column=5)
    password=Label(new_window,text='   ',).grid(row=9,column=3)
    password=Label(new_window,text='please type').grid(row=9,column=4)
    password=Entry(new_window,width=20)
    password.grid(row=9,column=5)

    

    def _del():
        conn=sql.connect(host='localhost',user='root',password=password.get(),auth_plugin='mysql_native_password')
        print(password)
        c=conn.cursor()                                     
        c.execute('use library')
        c.execute('''delete from books where book_code = {} '''.format(int(code.get())))
        conn.commit()
        c.close()
        conn.close()
        
        code.delete(0,'end')
        MessageBox.showinfo("Delete Status" ,"Deleted Successfully")

    delete=Button(new_window,text='DELETE',command=_del,bg='turquoise')
    delete.grid(row=10,column=5)  
    
    Label(del_window,text='Password').grid(row=5,column=5)



def dele_window():
    carrier = Toplevel(root)
    carrier.geometry('250x150')
   
    lbl = Label(carrier, text="this is new window")
    
    
    Label(carrier,text='DELETE',font=20).grid(row=0,column=5)
    Label(carrier,text='   ',).grid(row=1,column=3)
    Label(carrier,text='CODE').grid(row=1,column=4)
    code=Entry(carrier,width=20)
    code.grid(row=1,column=5)




    password=Label(carrier,text='Password',font=20).grid(row=7,column=5)
    password=Label(carrier,text='   ',).grid(row=9,column=3)
    password=Label(carrier,text='please type').grid(row=9,column=4)
    password=Entry(carrier,width=20)
    password.grid(row=9,column=5) 

    def _del_():
        conn=sql.connect(host='localhost',user='root',password=password.get(),auth_plugin='mysql_native_password')
        print(password)
        c=conn.cursor()                                     
        c.execute('use library')
        c.execute('''delete from borrower_details where code = {} '''.format(int(code.get())))
        c.execute('''update books 
                  set status = 'A'
                  where book_code={}'''.format(int(code.get())))
        conn.commit()
        c.close()
        conn.close()
        book_code.delete(0,'end')
        MessageBox.showinfo("Delete Status" ,"Deleted Successfully")

    delete=Button(carrier,text='DELETE',command=_del_,bg='turquoise')
    delete.grid(row=10,column=5)  
    
    Label(dele_window,text='Password').grid(row=5,column=5)

def borrower_details():
#a=Toplevel()
#connection setup
#CHANGE THE USER AND PASSWORD HERE
    mydb=sql.connect(host='localhost',user='root',passwd ='supermanLIKESgotham7234',auth_plugin='mysql_native_password',db='library')
    cursor = mydb.cursor()
    s = "SELECT * from borrower_details"
    cursor.execute(s)
    rows = cursor.fetchall()
    total = cursor.rowcount
    print("Total data entries :" +str(total))




    win=Tk()
    frm = Frame(win)
    frm.pack(side=tk.LEFT , padx=20 )
    tv = ttk.Treeview(win , columns = (1,2,3,4,5,6), show = "headings", height="5")
        


    tv.pack()
    tv.heading(1,text="Code")
    tv.heading(2,text="Book name")
    tv.heading(3,text="Address")
    tv.heading(4,text="phone-number")
    tv.heading(5,text="issue-date")
    tv.heading(6,text="issue-period")
    for i in rows :
        tv.insert('' , 'end' , values = i)
    win.title("Search Box")
    win.geometry("1500x365")
    win.resizable(True,True) 

    win.mainloop()
      

   
def records():
    #record=Toplevel()
    #connection setup
    #CHANGE THE USER AND PASSWORD HERE
    mydb=sql.connect(host='localhost',user='root',passwd ='supermanLIKESgotham7234',auth_plugin='mysql_native_password',db='library')
    cursor = mydb.cursor()
    s = "SELECT * from books"
    cursor.execute(s)
    rows = cursor.fetchall()
    total = cursor.rowcount
    print("Total data entries :" +str(total))




    win=Tk()
    frm = Frame(win)
    frm.pack(side=tk.LEFT , padx=20 )
    tv = ttk.Treeview(win , columns = (1,2,3,4), show = "headings", height="5")
    


    tv.pack()
    tv.heading(1,text="Code")
    tv.heading(2,text="Book name")
    tv.heading(3,text="price")
    tv.heading(4,text="status")

    for i in rows :
        tv.insert('' , 'end' , values = i)
    win.title("Search Box")
    win.geometry("850x365")
    win.resizable(False,False) 
    win.mainloop()
    
#DATA ENTRY FOR TABLE borrower_details
def new_window():
    top=Toplevel()
    top.geometry('600x250')

    Label(top,text='BORROWER DETAILS',font=20,pady=10).grid(row=0,column=1)

    book_code=Label(top,text='BOOK_CODE').grid(row=1,column=0)
    code=Entry(top,width=60)
    code.grid(row=1,column=1) 

    borrower_name=Label(top,text='NAME').grid(row=2,column=0)
    name=Entry(top,width=60)
    name.grid(row=2,column=1)

    borrower_address=Label(top,text='ADDRESS').grid(row=3,column=0)
    address=Entry(top,width=60)
    address.grid(row=3,column=1)

    phone_no=Label(top,text='PHONE N0').grid(row=4,column=0)
    phone=Entry(top,width=60)
    phone.grid(row=4,column=1)

    issue_date=Label(top,text='ISSUE_DATE').grid(row=5,column=0)
    issuedate=Entry(top,width=60)
    issuedate.insert(0,'yyyymmdd')
    issuedate.grid(row=5,column=1)

    Period=Label(top,text='ISSUE_PERIOD').grid(row=6,column=0)
    period=Entry(top,width=60)
    period.grid(row=6,column=1)

    passwd=Label(top,text='password').grid(row=7,column=0)
    passwd=Entry(top,width=60)
    passwd.grid(row=7,column=1)

    

    
    
    
    
    #adding data to table borrower_details
    def update():
        #connection setup
        conn=sql.connect(host='localhost',user='root',passwd =passwd.get(),auth_plugin='mysql_native_password')
        if conn.is_connected():
            print('Succesfully conected.')
        else:
            print('ERROR! connecting the server.')
        c=conn.cursor()
        c.execute('use library')
        c.execute('''insert into borrower_details
                  values({},'{}','{}',{},'{}',{})'''.format(int(code.get()),name.get(),address.get(),int(phone.get()),issuedate.get(),int(period.get())))
    
    
        c.execute('''update books 
                  set status = 'NA'
                  where book_code={}'''.format(int(code.get())))
    
    
        conn.commit()
        c.close()
        conn.close()
    
    
        code.delete(0,len(code.get()))
        name.delete(0,len(name.get()))
        address.delete(0,len(address.get()))
        phone.delete(0,len(phone.get()))
        issuedate.delete(0,len(issuedate.get()))
        period.delete(0,len(period.get()))

        MessageBox.showinfo("Update Status" ,"UPDATED Successfully");
    

    

    b_update=Button(top,text='UPDATE',command=update,bg='yellow',padx=10,pady=10)
    b_update.grid(row=9,column=1)
    
b_menu=Button(root,text=' Add book details',command=add_to_books,bg='peach puff',padx=5,pady=5,font=10)
b_menu.grid(row=0,column=0, padx=207, pady=15)  

b_records=Button(root,text=' Show book records',command=records,bg='peach puff',padx=5,pady=5,font=10)
b_records.grid(row=2,column=0,padx=60, pady=15)

b_records=Button(root,text='Show borrower_details',command=borrower_details,bg='peach puff',fg='black',padx=15,pady=10,font=10)
b_records.grid(row=4,column=0,padx=60, pady=15)

b_borrower=Button(root,text='Update borrower details',command=new_window,bg='peach puff',fg='black',padx=10,pady=8,font=10)
b_borrower.grid(row=6,column=0, padx=60, pady=15)

b_delete=Button(root,text='Delete a record',command=del_window,padx=5,pady=8,bg='red',fg='lightcyan',font=10)
b_delete.grid(row=7,column=0 , padx=0, pady=15)

b_delete=Button(root,text='Delete a borrower detail',command=dele_window,padx=5,pady=8,bg='red',fg='lightcyan',font=10)
b_delete.grid(row=8,column=0, padx=0, pady=15)

root.mainloop()





