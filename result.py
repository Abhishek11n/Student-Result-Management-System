from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x450+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # Title
        title = Label(self.root, text="Add Student Result", font=("goudy old style", 15, "bold"), bg="orange", fg="#262626")
        title.place(x=10, y=15, height=50, width=1180)

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        self.fetch_roll()

        # Labels
        lbl_select = Label(self.root, text="Select Student", font=("goudy old style", 20, "bold"), bg="white")
        lbl_select.place(x=50, y=100)
        
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="white")
        lbl_name.place(x=50, y=160)
        
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="white")
        lbl_course.place(x=50, y=220)
        
        lbl_marks = Label(self.root, text="Marks Obtained", font=("goudy old style", 20, "bold"), bg="white")
        lbl_marks.place(x=50, y=280)
        
        lbl_full_marks = Label(self.root, text="Full Marks", font=("goudy old style", 20, "bold"), bg="white")
        lbl_full_marks.place(x=50, y=340)
        
        # Combobox and Entries
        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list, font=("goudy old style", 15, 'bold'), state='readonly', justify=CENTER)
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")
        
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=500, y=100, width=90, height=28)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, 'bold'), bg="lightyellow", state='readonly')
        txt_name.place(x=280, y=160, width=300)
        
        txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, 'bold'), bg="lightyellow", state='readonly')
        txt_course.place(x=280, y=220, width=300)
        
        txt_marks = Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 20, 'bold'), bg="lightyellow")
        txt_marks.place(x=280, y=280, width=300)
        
        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 20, 'bold'), bg="lightyellow")
        txt_full_marks.place(x=280, y=340, width=300)
        
        # Buttons
        btn_add = Button(self.root, text="Submit", font=("times new roman", 15), bg='lightgreen', activebackground="lightgreen", cursor='hand2', command=self.add)
        btn_add.place(x=300, y=400, width=120, height=35)

        btn_clear = Button(self.root, text="Clear", font=("times new roman", 15), bg='lightgray', activebackground="white", cursor='hand2', command=self.clear)
        btn_clear.place(x=430, y=400, width=120, height=35)

    # ===============
    def fetch_roll(self):
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])  
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")        
        finally:
            con.close()

    def search(self):
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name, course FROM student WHERE roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()
    
    def add(self):
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            # Validate data before proceeding
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please first search student record", parent=self.root)
                return

            if not self.var_marks.get().isdigit() or not self.var_full_marks.get().isdigit():
                messagebox.showerror("Error", "Marks and Full Marks should be numbers", parent=self.root)
                return

            # Check if result already exists for this student in this course
            cur.execute("SELECT * FROM result WHERE roll=? AND course=?", (self.var_roll.get(), self.var_course.get()))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Result for this student already exists", parent=self.root)
            else:
                # Calculate percentage and insert data
                per = (int(self.var_marks.get()) * 100) / int(self.var_full_marks.get())
                cur.execute("INSERT INTO result (roll, name, course, marks_ob, full_marks, per) VALUES (?, ?, ?, ?, ?, ?)", (
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_marks.get(),
                    self.var_full_marks.get(),
                    str(per)
                ))
                con.commit()
                messagebox.showinfo("Success", "Result Added Successfully", parent=self.root)
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")

if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()
