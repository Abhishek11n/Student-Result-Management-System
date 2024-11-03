from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x450+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # Title
        title = Label(self.root, text="Manage Course Details", font=("goudy old style", 15, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, height=50, width=1180)
        
        # Variables
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        
        # Widgets
        lbl_courseName = Label(self.root, text="Course Name", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=80)
        lbl_Duration = Label(self.root, text="Duration", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=130)
        lbl_Charges = Label(self.root, text="Charges", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=180)
        lbl_Description = Label(self.root, text="Description", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=230)
        
        # Entry fields
        self.txt_courseName = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_courseName.place(x=150, y=80, width=200)
        self.txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_duration.place(x=150, y=130, width=200)
        self.txt_Charges = Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_Charges.place(x=150, y=180)
        self.txt_Description = Text(self.root, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_Description.place(x=150, y=230, width=300, height=100)

        # Buttons
        self.btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)

        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#0607d8", fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # Search panel
        self.var_search = StringVar()
        lbl_search_CourseName = Label(self.root, text="Course Name ", font=("goudy old style", 15, 'bold'), bg="white").place(x=720, y=80)
        txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        txt_search_courseName.place(x=870, y=80, width=180)
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2",command=self.search)
        btn_search.place(x=1070, y=80, width=120, height=28)

        # Content
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=130, width=440, height=300)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("Cid", "Name", "Duration", "Charges", "Description"))
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
       
        self.CourseTable.heading("Cid", text="Course ID")
        self.CourseTable.heading("Name", text="Name")
        self.CourseTable.heading("Duration", text="Duration")
        self.CourseTable.heading("Charges", text="Charges")
        self.CourseTable.heading("Description", text="Description")

        self.CourseTable["show"] = 'headings'
        self.CourseTable.column("Cid", width=80)
        self.CourseTable.column("Name", width=80)
        self.CourseTable.column("Duration", width=80)
        self.CourseTable.column("Charges", width=80)
        self.CourseTable.column("Description", width=100)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        self.CourseTable.config(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
    
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_Description.delete('1.0', END)
        self.txt_courseName.config(state=NORMAL)
    def delete(self): 
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Course WHERE Name=?", (self.var_course.get(),)) 
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "please select course from the list", parent=self.root)
                else:  
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deletd Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def get_data(self, ev):
        self.txt_courseName.config(state='readonly')
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_Description.delete('1.0', END)
        self.txt_Description.insert(END, row[4])

    def add(self):
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Course WHERE Name=?", (self.var_course.get(),)) 
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Course Name already present", parent=self.root)
                else:
                    cur.execute("INSERT INTO Course(Name, Duration, Charges, Description) VALUES(?, ?, ?, ?)", (
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_Description.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def update(self):
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Course WHERE Name=?", (self.var_course.get(),)) 
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select course from list", parent=self.root)
                else:
                    cur.execute("UPDATE Course SET Duration=?, Charges=?, Description=? WHERE Name=?", (
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_Description.get("1.0", END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM Course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.show
    
    def search(self):
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            cur.execute(f"SELECT * FROM Course Where Name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}")
if __name__=="__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
