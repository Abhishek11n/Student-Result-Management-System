import sqlite3
def create_db():
    con=sqlite3.connect(database="Student Result Management System.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Course(Cid INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Duration text,Charges text,Description text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student(Roll INTEGER PRIMARY KEY AUTOINCREMENT,Name text, Email text, Gender text, DOB text,Contact text,Admission text,Course text,State text,City text,PinCode text,Address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,course text,marks_ob text,full_marks text,per text)")
    con.commit()

    con.close()
create_db()