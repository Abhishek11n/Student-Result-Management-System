from tkinter import *
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
class RMS:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg="white")

        # Title
        title = Label(self.root, text="Student Result Management System", font=("goudy old style", 15, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # Menu
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1250, height=80)

        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add__course)
        btn_course.place(x=20, y=5, width=160, height=40)
        
        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_student)
        btn_student.place(x=370, y=5, width=160, height=40)

        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_result)
        btn_result.place(x=690, y=5, width=160, height=40)

        btn_view_student_result = Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_report)
        btn_view_student_result.place(x=970, y=5, width=180, height=40)


        self.center_frame = Frame(self.root, bg="#ff99ff", bd=2, relief=RIDGE)
        self.center_frame.place(x=300, y=200, width=700, height=300)

        center_label = Label(self.center_frame, text="Welcome to the Student Result Management System",
                             font=("goudy old style", 20, "bold"), bg="#99ffff", fg="#033054")
        center_label.pack(pady=20)

        instructions = Label(self.center_frame, text="This application allows you to manage courses, students, and results.\n"
                                                    "Use the menu options above to navigate through different functionalities.",
                             font=("goudy old style", 18), justify=CENTER)
        instructions.pack(pady=10)
       

    def add__course (self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)
    
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

root = Tk()
obj = RMS(root)
root.mainloop()
