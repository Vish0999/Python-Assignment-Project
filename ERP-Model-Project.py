import pyodbc
import sys



# ================= DATABASE CONNECTION =================
class Database:
    def __init__(self):
        server = r"Poonam\SQLEXPRESS01"
        database = "erp"

        self.conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={server};"
            f"DATABASE={database};"
            "Trusted_Connection=yes;"
        )
        self.cursor = self.conn.cursor()


# ================= ADMIN =================
class Admin(Database):

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        self.cursor.execute(
            "SELECT * FROM admin WHERE username=? AND password=?",
            (username, password)
        )

        if self.cursor.fetchone():
            print("Login Successful")
            self.menu()
        else:
            print("Invalid Credentials")

    def menu(self):
        while True:
            print("""
1. Add Teacher
2. Delete Teacher
3. Update Teacher
4. Add Exam Dept Member
5. Delete Exam Dept Member
6. Update Exam Dept Member
7. Show All Teachers
8. Show All Exam Dept Members
9. Logout
""")

            ch = input("Enter Choice: ")

            if ch == "1":
                name = input("Teacher Name: ")
                subject = input("Subject: ")
                username = input("Username: ")
                password = input("Password: ")

                self.cursor.execute(
                    "INSERT INTO teacher(teacher_name,subject_name,username,password) VALUES(?,?,?,?)",
                    (name, subject, username, password)
                )
                self.conn.commit()
                print("Teacher Added")

            elif ch == "2":
                tid = input("Teacher ID: ")
                self.cursor.execute("DELETE FROM teacher WHERE teacher_id=?", (tid,))
                self.conn.commit()
                print("Teacher Deleted")

            elif ch == "3":
                tid = input("Teacher ID: ")
                subject = input("New Subject: ")
                self.cursor.execute(
                    "UPDATE teacher SET subject_name=? WHERE teacher_id=?",
                    (subject, tid)
                )
                self.conn.commit()
                print("Teacher Updated")

            elif ch == "4":
                name = input("Exam Dept Name: ")
                username = input("Username: ")
                password = input("Password: ")

                self.cursor.execute(
                    "INSERT INTO exam_department(name,username,password) VALUES(?,?,?)",
                    (name, username, password)
                )
                self.conn.commit()
                print("Exam Department Member Added")

            elif ch == "5":
                eid = input("Exam Dept ID: ")
                self.cursor.execute("DELETE FROM exam_department WHERE exam_dept_id=?", (eid,))
                self.conn.commit()
                print("Exam Dept Member Deleted")

            elif ch == "6":
                eid = input("Exam Dept ID: ")
                new_name = input("New Name: ")
                self.cursor.execute(
                    "UPDATE exam_department SET name=? WHERE exam_dept_id=?",
                    (new_name, eid)
                )
                self.conn.commit()
                print("Updated Successfully")

            elif ch == "7":
                self.cursor.execute("SELECT teacher_id,teacher_name,subject_name FROM teacher")
                for row in self.cursor.fetchall():
                    print(row)

            elif ch == "8":
                self.cursor.execute("SELECT exam_dept_id,name FROM exam_department")
                for row in self.cursor.fetchall():
                    print(row)

            elif ch == "9":
                break


# ================= TEACHER =================
class Teacher(Database):

    def login(self):
        self.username = input("Username: ")
        password = input("Password: ")

        self.cursor.execute(
            "SELECT subject_name FROM teacher WHERE username=? AND password=?",
            (self.username, password)
        )

        row = self.cursor.fetchone()
        if row:
            self.subject = row[0]
            print("Login Successful")
            self.menu()
        else:
            print("Invalid Credentials")

    def menu(self):
        while True:
            print("""
1. Add Student
2. Delete Student
3. Take Attendance
4. Show All Students
5. Logout
""")
            ch = input("Choice: ")

            if ch == "1":
                name = input("Student Name: ")
                username = input("Username: ")
                password = input("Password: ")

                self.cursor.execute(
                    "INSERT INTO student(student_name,username,password) VALUES(?,?,?)",
                    (name, username, password)
                )
                self.conn.commit()
                print("Student Added")

            elif ch == "2":
                sid = input("Student ID: ")
                self.cursor.execute("DELETE FROM student WHERE student_id=?", (sid,))
                self.conn.commit()
                print("Student Deleted")

            elif ch == "3":
                self.take_attendance()

            elif ch == "4":
                self.cursor.execute("SELECT student_id,student_name FROM student")
                for row in self.cursor.fetchall():
                    print(row)

            elif ch == "5":
                break

    def take_attendance(self):
        self.cursor.execute("SELECT student_id,student_name FROM student")
        students = self.cursor.fetchall()

        for sid, name in students:
            status = input(f"{name} (P/A): ").lower()

            self.cursor.execute(
                "SELECT * FROM attendance WHERE student_id=? AND subject_name=?",
                (sid, self.subject)
            )

            record = self.cursor.fetchone()

            if record:
                if status == "p":
                    self.cursor.execute(
                        "UPDATE attendance SET total_classes=total_classes+1, attended_classes=attended_classes+1 WHERE student_id=? AND subject_name=?",
                        (sid, self.subject)
                    )
                else:
                    self.cursor.execute(
                        "UPDATE attendance SET total_classes=total_classes+1 WHERE student_id=? AND subject_name=?",
                        (sid, self.subject)
                    )
            else:
                if status == "p":
                    self.cursor.execute(
                        "INSERT INTO attendance(student_id,subject_name,total_classes,attended_classes) VALUES(?,?,1,1)",
                        (sid, self.subject)
                    )
                else:
                    self.cursor.execute(
                        "INSERT INTO attendance(student_id,subject_name,total_classes,attended_classes) VALUES(?,?,1,0)",
                        (sid, self.subject)
                    )

        self.conn.commit()
        print("Attendance Updated")


# ================= EXAM DEPARTMENT =================
class ExamDepartment(Database):

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        self.cursor.execute(
            "SELECT * FROM exam_department WHERE username=? AND password=?",
            (username, password)
        )

        if self.cursor.fetchone():
            print("Login Successful")
            self.menu()
        else:
            print("Invalid Credentials")

    def menu(self):
        while True:
            print("""
1. Add Timetable
2. Show Timetable
3. Update Timetable
4. Delete Timetable
5. Logout
""")
            ch = input("Choice: ")

            if ch == "1":
                subject = input("Subject: ")
                date = input("Exam Date (YYYY-MM-DD): ")
                time = input("Exam Time: ")

                self.cursor.execute(
                    "INSERT INTO exam_timetable(subject_name,exam_date,exam_time) VALUES(?,?,?)",
                    (subject, date, time)
                )
                self.conn.commit()
                print("Timetable Added")

            elif ch == "2":
                self.cursor.execute("SELECT * FROM exam_timetable")
                for row in self.cursor.fetchall():
                    print(row)

            elif ch == "3":
                eid = input("Exam ID: ")
                date = input("New Date: ")
                time = input("New Time: ")

                self.cursor.execute(
                    "UPDATE exam_timetable SET exam_date=?, exam_time=? WHERE exam_id=?",
                    (date, time, eid)
                )
                self.conn.commit()
                print("Updated")

            elif ch == "4":
                eid = input("Exam ID: ")
                self.cursor.execute("DELETE FROM exam_timetable WHERE exam_id=?", (eid,))
                self.conn.commit()
                print("Deleted")

            elif ch == "5":
                break


# ================= STUDENT =================
class Student(Database):

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        self.cursor.execute(
            "SELECT student_id FROM student WHERE username=? AND password=?",
            (username, password)
        )

        row = self.cursor.fetchone()

        if row:
            self.student_id = row[0]
            print("Login Successful")
            self.menu()
        else:
            print("Invalid Credentials")

    def menu(self):
        while True:
            print("""
1. Check Attendance
2. Check Exam Timetable
3. Logout
""")
            ch = input("Choice: ")

            if ch == "1":
                self.check_attendance()
            elif ch == "2":
                self.check_exam()
            elif ch == "3":
                break

    def check_attendance(self):
        self.cursor.execute(
            "SELECT subject_name,total_classes,attended_classes FROM attendance WHERE student_id=?",
            (self.student_id,)
        )

        for subject, total, attended in self.cursor.fetchall():
            percent = (attended * 100 / total) if total > 0 else 0
            print(f"{subject} - {percent:.2f}%")

    def check_exam(self):
        self.cursor.execute("SELECT subject_name,exam_date,exam_time FROM exam_timetable")
        exams = self.cursor.fetchall()

        print("\nSubject      Date        Time       Eligible")
        print("-"*55)

        for subject, date, time in exams:
            self.cursor.execute(
                "SELECT total_classes,attended_classes FROM attendance WHERE student_id=? AND subject_name=?",
                (self.student_id, subject)
            )

            record = self.cursor.fetchone()

            if record:
                total, attended = record
                percent = (attended * 100 / total) if total > 0 else 0
                eligible = "YES" if percent >= 75 else "NO"
            else:
                eligible = "NO"

            print(f"{subject:<12}{date}   {time:<12}{eligible}")


# ================= MAIN =================
while True:
    print("""
SELECT YOUR ROLE
1) Admin
2) Teacher
3) Student
4) Exam Department
5) Exit
""")

    choice = input("Choice: ")

    if choice == "1":
        Admin().login()

    elif choice == "2":
        Teacher().login()

    elif choice == "3":
        Student().login()

    elif choice == "4":
        ExamDepartment().login()

    elif choice == "5":
        break


