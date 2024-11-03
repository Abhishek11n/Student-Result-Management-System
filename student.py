from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x450+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # Title
        title = Label(self.root, text="Manage Student Details", font=("goudy old style", 15, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, height=50, width=1180)
        
        # Variables
        self.var_roll= StringVar()
        self.var_Name = StringVar()
        self.var_Email = StringVar()
        self.var_Gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_adate = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pincode = StringVar()
        self.var_Address = StringVar()
        
        # Widgets
        lbl_Roll = Label(self.root, text="Roll No", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=80)
        lbl_Name = Label(self.root, text="Name", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=130)
        lbl_Email = Label(self.root, text="Email", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=180)
        lbl_Gender = Label(self.root, text="Gender", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=230)
        lbl_state = Label(self.root, text="State", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=280)
        txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, 'bold'), bg="lightyellow").place(x=150, y=280, width=100)
        lbl_city = Label(self.root, text="City", font=("goudy old style", 15, 'bold'), bg="white").place(x=300, y=280)
        txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, 'bold'), bg="lightyellow").place(x=360, y=280, width=100)
        lbl_pincode = Label(self.root, text="Pincode", font=("goudy old style", 15, 'bold'), bg="white").place(x=480, y=280)
        txt_pincode = Entry(self.root, textvariable=self.var_pincode, font=("goudy old style", 15, 'bold'), bg="lightyellow").place(x=570, y=280, width=100)
        lbl_Address = Label(self.root, text="Address", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=330)
        
        
        # Entry fields
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_roll.place(x=150, y=80, width=200)
        self.txt_Name = Entry(self.root, textvariable=self.var_Name, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_Name.place(x=150, y=130, width=200)
        self.txt_Email = Entry(self.root, textvariable=self.var_Email, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_Email.place(x=150, y=180)
        self.txt_Gender = ttk.Combobox(self.root, textvariable=self.var_Gender,values=("Select","Male","Female","Other"),font=("goudy old style", 15, 'bold'),state='readonly',justify=CENTER)
        self.txt_Gender.place(x=150, y=230,width=200)
        self.txt_Gender.current(0)

        #column2======
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 15, 'bold'), bg="white").place(x=360, y=80)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15, 'bold'), bg="white").place(x=360, y=130)
        lbl_addmistion = Label(self.root, text="Addmission", font=("goudy old style", 15, 'bold'), bg="white").place(x=360, y=180)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, 'bold'), bg="white").place(x=360, y=230)
        
         
        # Entry fields=====2
        self.course_list=[]
        #funtion call
        self.fetch_course()
        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_dob.place(x=480, y=80, width=200)
        self.txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_contact.place(x=480, y=130, width=200)
        self.txt_addmistion = Entry(self.root, textvariable=self.var_adate, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_addmistion.place(x=480, y=180)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course,values=self.course_list,font=("goudy old style", 15, 'bold'),state='readonly',justify=CENTER)
        self.txt_course.place(x=480, y=230,width=200)
        self.txt_course.set("Select")
        #text Address====
        self.txt_Address = Text(self.root, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_Address.place(x=150, y=330, width=400, height=60)

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
        lbl_search_roll = Label(self.root, text="Roll No", font=("goudy old style", 15, 'bold'), bg="white").place(x=720, y=80)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        txt_search_roll.place(x=870, y=80, width=180)
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2",command=self.search)
        btn_search.place(x=1070, y=80, width=120, height=28)

        # Content
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=130, width=440, height=300)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("Roll", "Name", "Email", "Gender", "DOB","Contact","Admission","Course","State","City","PinCode","Address"))
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
       
        self.CourseTable.heading("Roll", text="Roll no.")
        self.CourseTable.heading("Name", text="Name")
        self.CourseTable.heading("Email", text="Email")
        self.CourseTable.heading("Gender", text="Gender")
        self.CourseTable.heading("DOB", text="DOB")
        self.CourseTable.heading("Contact", text="Contact")
        self.CourseTable.heading("Admission", text="Admission")
        self.CourseTable.heading("Course", text="Course")
        self.CourseTable.heading("State", text="State")
        self.CourseTable.heading("City", text="City")
        self.CourseTable.heading("PinCode", text="PinCode")
        self.CourseTable.heading("Address", text="Address")

        self.CourseTable["show"] = 'headings'
        self.CourseTable.column("Roll", width=80)
        self.CourseTable.column("Name", width=80)
        self.CourseTable.column("Email", width=80)
        self.CourseTable.column("Gender", width=80)
        self.CourseTable.column("DOB", width=80)
        self.CourseTable.column("Contact", width=100)
        self.CourseTable.column("Admission", width=80)
        self.CourseTable.column("Course", width=80)
        self.CourseTable.column("State", width=80)
        self.CourseTable.column("City", width=80)
        self.CourseTable.column("PinCode", width=80)
        self.CourseTable.column("Address", width=100)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
       
        self.CourseTable.config(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
    
    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_Name.set(""),
        self.var_Email.set(""),
        self.var_Gender.set(""),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_adate.set(""),
        self.var_course.set(""),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pincode.set(""),
        self.txt_Address.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")
    def delete(self): 
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),)) 
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "please select student from the list", parent=self.root)
                else:  
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","student deletd Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def get_data(self, ev):
        self.txt_roll.config(state='readonly')
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]

        self.var_roll.set(row[0]),
        self.var_Name.set(row[1]),
        self.var_Email.set(row[2]),
        self.var_Gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_adate.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pincode.set(row[10]),
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END,row[11])
        

    def add(self):
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE Roll=?", (self.var_roll.get(),)) 
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Roll number already present", parent=self.root)
                else:
                    cur.execute("INSERT INTO student(Roll, Name,Email,Gender,DOB,Contact,Admission,Course,State,City,PinCode,Address) VALUES(?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ?)", (
                        self.var_roll.get(),
                        self.var_Name.get(),
                        self.var_Email.get(),
                        self.var_Gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_adate.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pincode.get(),
                        self.txt_Address.delete("1.0", END)
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Student Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def update(self):
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "roll number  should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),)) 
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select student from list", parent=self.root)
                else:
                    cur.execute("UPDATE student SET Name=?,Email=?,Gender=?,DOB=?,Contact=?,Admission=?,Course=?,State=?,City=?,PinCode=?,Address=? where roll=?",(
                        self.var_Name.get(),
                        self.var_Email.get(),
                        self.var_Gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_adate.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pincode.get(),
                        self.txt_Address.delete("1.0", END),
                        self.var_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "student updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Eroor",f"error due to {str(ex)}")
    def fetch_course(self):
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM course")
            rows = cur.fetchall()
        
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])  
           
           
        except Exception as ex:
            messagebox.showerror("Eroor",f"error duu to {str(ex)}")        
    
    def search(self):
        con = sqlite3.connect(database="Student Result Management System.db")
        cur = con.cursor()
        try:
            cur.execute(f"SELECT * FROM student Where Roll=?",(self.var_search.get(),))
            row = cur.fetchone()
            if row!=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
               
                self.CourseTable.insert('', END, values=row)
            else:
                messagebox.showerror("error","no record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("error",f"error due to {str(ex)}")
if __name__=="__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
