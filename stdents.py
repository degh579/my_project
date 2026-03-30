from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

# ================== الاتصال ==================
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="as1"
    )

# ================== إضافة بيانات ==================
def add_data():
    if e1.get() == '' or e2.get() == '' or e3.get() == '':
        messagebox.showwarning('تحذير', 'مفيش بيانات')
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO students (studentID, studentname, phone) VALUES (%s, %s, %s)',
        (e1.get(), e2.get(), e3.get())
    )

    conn.commit()
    conn.close()

    load_data()
    clear_data()
    messagebox.showinfo('تم', 'تمت الإضافة')

# ================== تحميل البيانات ==================
def load_data():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    tree.delete(*tree.get_children())

    for row in rows:
        tree.insert("", END, values=row)

    conn.close()

# ================== اختيار صف ==================
def select_data(event):
    selected = tree.focus()
    values = tree.item(selected, 'values')
    if values:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

        e1.insert(0, values[0])  # studentID
        e2.insert(0, values[1])  # studentName
        e3.insert(0, values[2])  # studentPhone

# ================== حذف ==================
def delete_data():
    selected = tree.focus()
    values = tree.item(selected, 'values')
    if not values:
        messagebox.showwarning('تحذير', 'اختاري صف أولاً')
        return

    student_id = values[0]
    confirm = messagebox.askyesno('تأكيد', 'هل متأكدة من الحذف؟')
    if not confirm:
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE studentID = %s', (student_id,))
    conn.commit()
    conn.close()

    load_data()
    clear_data()
    messagebox.showinfo('تم', 'تم الحذف')

# ================== تفريغ الحقول ==================
def clear_data():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)



# ================== البحث المباشر ==================
def search_data(*args):
    query = search_var.get()
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE studentname LIKE %s OR phone LIKE %s",
        (f'%{query}%', f'%{query}%')
    )
    rows = cursor.fetchall()
    tree.delete(*tree.get_children())

    for row in rows:
        tree.insert("", END, values=row)

    conn.close()





# ================== الواجهة ==================
root = Tk()
root.title('Student System')
root.geometry('600x400')

# الحقول
Label(root, text="StudentID").grid(row=0, column=0, sticky="e", padx=10, pady=5)
Label(root, text="StudentName").grid(row=1, column=0, sticky="e", padx=10, pady=5)
Label(root, text="StudentPhone").grid(row=2, column=0, sticky="e", padx=10, pady=5)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)
e3.grid(row=2, column=1, padx=10, pady=5)

# الأزرار
Button(root, text="Add", command=add_data, bg="green", fg="white").grid(row=0, column=2, padx=5)
Button(root, text="Delete", command=delete_data, bg="red", fg="white").grid(row=1, column=2, padx=5)
Button(root, text="Clear", command=clear_data).grid(row=2, column=2, padx=5)

# حقل البحث
Label(root, text="Search:").grid(row=3, column=1, sticky="e", padx=10)
search_var = StringVar()
search_var.trace_add('write', search_data)
Entry(root, textvariable=search_var).grid(row=3, column=1, sticky="w", padx=5)


# جدول البيانات
tree = ttk.Treeview(root, columns=("studentID", "studentname", "studentphone"), show="headings")
tree.heading("studentID", text="StudentID")
tree.heading("studentname", text="StudentName")
tree.heading("studentphone", text="StudentPhone")

tree.column("studentID", width=100, anchor="center")
tree.column("studentname", width=150, anchor="w")
tree.column("studentphone", width=120, anchor="w")

tree.grid(row=3, column=0, columnspan=3, padx=10, pady=20)

tree.bind("<<TreeviewSelect>>", select_data)

# تحميل البيانات عند فتح البرنامج
load_data()

root.mainloop()