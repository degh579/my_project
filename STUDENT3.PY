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
    if e_name.get() == '' or e_phone.get() == '':
        messagebox.showwarning('تحذير', 'مفيش بيانات')
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO students (studentid,studentname, studentphone) VALUES (%s, %s)',
        (e_name.get(), e_phone.get())
    )

    conn.commit()
    conn.close()

    load_data()
    clear_data()
    messagebox.showinfo('تم', 'تمت الإضافة')

# ================== تعديل بيانات ==================
def edit_data():
    selected = tree.focus()
    values = tree.item(selected, 'values')
    if not values:
        messagebox.showwarning('تحذير', 'اختاري صف أولاً')
        return

    student_id = values[0]

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        'UPDATE students SET studentname=%s, studentphone=%s WHERE studentID=%s',
        (e_name.get(), e_phone.get(), student_id)
    )
    '''
    cursor.execute(
        'UPDATE students SET studentname=%s, studentphone=%s WHERE studentID=%s',
        (e_name.get(), e_phone.get(), student_id)
    )
    conn.commit()
    conn.close()
    '''
    load_data()
    clear_data()
    messagebox.showinfo('تم', 'تم التعديل')

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
        e_id.config(state='normal')
        e_id.delete(0, END)
        e_id.insert(0, values[0])
        e_id.config(state='disabled')

        e_name.delete(0, END)
        e_name.insert(0, values[1])
        e_phone.delete(0, END)
        e_phone.insert(0, values[2])

# ================== تفريغ الحقول ==================
def clear_data():
    e_id.config(state='normal')
    e_id.delete(0, END)
    e_id.config(state='disabled')
    e_name.delete(0, END)
    e_phone.delete(0, END)
    search_var.set('')
    load_data()

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
root.title('Student System with Search')
root.geometry('700x450')

# الحقول
Label(root, text="StudentID").grid(row=0, column=0, sticky="e", padx=10, pady=5)
Label(root, text="StudentName").grid(row=1, column=0, sticky="e", padx=10, pady=5)
Label(root, text="StudentPhone").grid(row=2, column=0, sticky="e", padx=10, pady=5)

e_id = Entry(root, state='disabled')  # ID أوتوماتيك
e_name = Entry(root)
e_phone = Entry(root)

e_id.grid(row=0, column=1, padx=10, pady=5)
e_name.grid(row=1, column=1, padx=10, pady=5)
e_phone.grid(row=2, column=1, padx=10, pady=5)

# الأزرار
Button(root, text="Add", command=add_data, bg="green", fg="white").grid(row=0, column=2, padx=5)
Button(root, text="Edit", command=edit_data, bg="blue", fg="white").grid(row=1, column=2, padx=5)
Button(root, text="Delete", command=delete_data, bg="red", fg="white").grid(row=2, column=2, padx=5)
Button(root, text="Clear", command=clear_data,bg="red", fg="white").grid(row=3, column=2, pady=5)

# حقل البحث
Label(root, text="Search:").grid(row=3, column=0, sticky="e", padx=10)
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

tree.grid(row=4, column=0, columnspan=3, padx=10, pady=20)
tree.bind("<<TreeviewSelect>>", select_data)

# تحميل البيانات عند فتح البرنامج
load_data()

root.mainloop()