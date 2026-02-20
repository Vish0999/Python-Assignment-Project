

import pyodbc

class Database:
    def __init__(self):
        server = r"Poonam\SQLEXPRESS01"
        database = "college_data"

        self.conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={server};"
            f"DATABASE={database};"
            "Trusted_Connection=yes;"
        )
        self.cursor = self.conn.cursor()
        print("Database connected successfully")



class College(Database):
    def __init__(self):
        super().__init__()
        self.courses = []
        self.fee = {}
        self.load_courses()
        self.load_fee_structure()

    def load_courses(self):
        self.courses.clear()
        self.cursor.execute("SELECT course_name FROM courses")
        for row in self.cursor.fetchall():
            self.courses.append(row[0])

    def load_fee_structure(self):
        self.cursor.execute("SELECT * FROM fee_structure")
        row = self.cursor.fetchone()

        self.fee = {
            "base": row[1],
            "analytical": row[2],
            "hostel": row[3],
            "food": row[4],
            "semester": row[5],
            "annual": row[6]
        }

    def show_courses(self):
        print("\n---- AVAILABLE COURSES ----")
        for c in self.courses:
            print("-", c)








class FeeCalculation:
    def __init__(self, college):
        self.college = college

    def calculate_fee(self):
        name = input("Enter student name: ").lower()
        self.college.show_courses()

        course = input("Enter course name: ")
        if course not in self.college.courses:
            print("Invalid course")
            return

        stream = input("Analytical stream (Y/N): ").lower()
        hostel = input("Hostel (Y/N): ").lower()
        food_months = int(input("Food months: "))
        transport = input("Transport (semester/annual): ").lower()

        total = self.college.fee["base"]

        if stream == "y":
            total += total * self.college.fee["analytical"]

        if hostel == "y":
            total += self.college.fee["hostel"]

        total += food_months * self.college.fee["food"]

        if transport == "semester":
            total += self.college.fee["semester"]
        elif transport == "annual":
            total += self.college.fee["annual"]
        else:
            print("Invalid transport")
            return

        self.college.cursor.execute(
            """
            INSERT INTO student_fee
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (name, course, stream, hostel, food_months, transport, total)
        )

        self.college.conn.commit()

        print("\n TOTAL ANNUAL FEE:", total)





class FeeReport:
    def __init__(self, college):
        self.college = college

    def show_bill(self):
        name = input("Enter student name: ").lower()

        self.college.cursor.execute(
            "SELECT * FROM student_fee WHERE student_name=?",
            (name,)
        )
        row = self.college.cursor.fetchone()

        if not row:
            print("No record found")
            return

        print("\n------ STUDENT FEE BILL ------")
        print("Student:", row[1])
        print("Course:", row[2])
        print("Analytical Stream:", row[3])
        print("Hostel:", row[4])
        print("Food Months:", row[5])
        print("Transport:", row[6])
        print("------------------------------")
        print("TOTAL FEE:", row[7])




college = College()

while True:
    print("""
1. Show Courses
2. Calculate Fee
3. Print Fee Bill
4. Exit
""")

    ch = input("Enter choice: ")

    if ch == "1":
        college.show_courses()

    elif ch == "2":
        fee = FeeCalculation(college)
        fee.calculate_fee()

    elif ch == "3":
        bill = FeeReport(college)
        bill.show_bill()

    elif ch == "4":
        break

    else:
        print("Invalid choice")