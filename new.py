from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="as1"
    )
try:
    conn = mysql.connector.connect(
        host="localhost",      # السيرفر
        user="root",           # اليوزر
        password="",           # الباسورد (لو فاضي سيبيه "")
        database="as1"  # اسم الداتابيز
    )

    print("Sucess✅")

except mysql.connector.Error as err:
    print("Fail", err)

    

def add_student():
    conn = connect_db()
    cursor = conn.cursor()

    sql = 'INSERT INTO students (phone, studentid, studentname) VALUES (%s, %s,%s)'
    cursor.execute(sql, (e1.get(),e2.get(),e3.get()))

    conn.commit()
    conn.close()

    print('Done')

#اضااااااااااااافه   الصنف 
def add_data():
    if e1.get()== '' or e2.get() ==  ''  or e3.get() == ' ' :
        messagebox.showwarning (' No data Insert ' ) 
        return
    conn= connect_db()
    cursor = conn.cursor()  
    cursor.execute (
        'INSERT INTO students (studentID, studentname, studentphone) VALUES (%s, %s,%s)',
     (e1.get(),e2.get(),e3.get())
                   )
    
    conn.commit()
    conn.close()
    load_data()
    clear_data()
    messagebox.showinfo ('Done Add', 'DONE')


# تحميل البيانات
def load_data():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    tree.delete(*tree.get_children())
    # مسح القديم
    for item in tree.get_children():
        tree.delete(item)

    # إضافة البيانات
    for row in rows:
        tree.insert("", END, values=row)

    conn.close()  

# اختيار الصنف 
def select (event):
    selected = tree.focus()
    values = tree.item(selected , 'values') 
    if  values :
        e1.delete(0,END) 
        e2.delete(0,END)  
        e3.delete(0,END)
        e1.insert(0,values[1])
        e2.insert(0,values[2])
        #e3.insert(0,values[3])
#      حذذذذذذذذف الدااااااااااتاااا

def  delete_data():
    selected = tree.focus()
    values= tree.item(selected , 'values')
    if not values :
        messagebox.showwarning ('choose the data ', 'Attenion ') 
        return 
    studentid = values[0]   
    confirm = messagebox.askyesno('sure delete ' , 'shoor')
    if not confirm :
        return 
    conn= connect_db()
    cursor= conn.cursor() 
    cursor.execute('delete  from students where id  = %s' ,(id,) )
    conn.commit()
    conn.close ()
    load_data()
    clear_data()
    messagebox.showinfo ('delete done ', 'done ')

# تفرييييغ الداتا 
def clear_data():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

#      الواجهههة    
root = Tk()
root .geometry ('500x500')
root.title('courses')

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
l1= Label(root, text="studentID",anchor="w").grid (row= 0 , column = 0 ,sticky="e",padx=10, pady=10)
l2= Label(root, text='sudentName',anchor="w").grid (row= 1 , column = 0 , sticky="e",padx=10, pady=10)
l3= Label(root, text="studentphone",anchor="w").grid (row= 2 , column = 0 , sticky="e",padx=10, pady=10)


e1.grid(row= 0 , column=1)
e2.grid(row= 1 , column=1)
e3.grid(row= 2 , column=1)


# زر تحميل 
btn = Button(root, text="Add", command= add_student).grid(row=3, column=0, pady=10)

#btn1 = Button(root, text="عرض البيانات", command=load_data)
btn1= Button(root , text = 'Edit ' , command =select ).grid(row=3, column=1,pady=10)
btn2= Button(root , text = 'delete ' , command  = delete_data ).grid(row=3, column=2,pady=10)
btn3 = Button (root , text ='clear ' , command = clear_data ).grid(row=3, column=3,pady=10)


# جدول
tree = ttk.Treeview(root, columns=("id", "Name",'studentphone'), show="headings")
tree.heading("id", text="studentID")
tree.heading("Name", text="studentName")
tree.heading("studentphone", text="studentphone")


tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

tree.bind("<<TreeviewSelect>>", select)
# تحميل البيانات
load_data()
root.mainloop()









































'''
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)    
sql = "INSERT INTO students (phone, studentid, studentname) VALUES (%s, %s,%s)"
values = ('01060615139',5,"Ahlam")

cursor.execute(sql, values)
conn.commit()

print("تم الإضافة ✅")    
''' 