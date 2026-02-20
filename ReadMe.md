## **Python Assignment + Project**

#### This repository contains python assignment questions file ( Assignment-1.py and Assignment-2.py ) and python project file ( Print-Bill-Project.py ) and python self made project ( College ERP System).

### **Assignment-1.py**
This file contain 55 python questions related to list, dict, set, functions, lamda, database, file handling.

### **Assignment-2.py**
This file contain 50 questions related to List comprhension, lamda.



## **Project Details :**
## **1) Print-Bill-Project :**
## **Project Introduction :**

This project is a HMS (customer Bill Printing + add new menu with price ) developed using Python and SQL Server. It allows hotel staff to manage menu items, take customer orders, and generate bills efficiently. The system uses Object-Oriented Programming (OOP) concepts (Class, Inheritance) and connects to a database using pyodbc for data storage.

This project helps automate hotel billing operations and reduces manual errors.



## **Project Functionality :**

This Project allows users to manage hotel menus, take customer orders,Print Bills and store order details in a database.
The system automatically calculates bills and enables printing customer-wise bills from stored data.
It uses object-oriented programming with database connectivity for real-time data handling.

### functionality of Hotel staff and customer

1. Show Menu
    This function is used to show all menu/items available in database with price 
2. Add New Menu
3. Take Order
4. print Bill
5. Exit


### Various classes used in project :
1) Class Database :
This class use for database connection. It is super class.

2) Class Hotel: 
Class hotel is used to perform all hotel related functionalityv like load_menu(), show_menu(), add_menu_items(), customer_Bill(), download_bill(). 
This Class inherit class Database.

3) Class Order :
This class is used for customer order. it is use to perform functionality like take_order(), save_order(), print_bill(),


## Input-Output Screens

1) Database Schema :
<img src="Project-Images\image.png" width="700" height="400">

## **3) College ERP System :( Self Made )**
This College ERP System helps manage basic college activities like teachers, students, attendance, and exams. It allows different users to log in and perform their specific tasks. The system stores data in a database and makes college work easier and more organized. 

## **Project Workflow :**
<img src="Project-Images\image-1.png" width="700" height="400">

## **Project Functionality :**
This Project allows users to manage hotel menus, take customer orders,Print Bills and store order details in a database.

### **1. Admin Module :**

* Admin can securely log in using username and password.

* Admin can add, update, delete, and view teachers.

* Admin can add, update, delete, and view exam department members.

* Admin manages user credentials for teachers and exam department.

* Admin can view all teachers and exam department members in the system.

* Admin can log out securely.


### **2. Teacher Module :**

Teacher can log in using assigned credentials.

Teacher can add new students to the system.

Teacher can delete students when required.

Teacher can take attendance for students subject-wise.

Attendance data updates total classes and attended classes automatically.

Teacher can view all students.

Teacher can log out securely.


### **3. Student Module :**

Student can log in using their credentials.

Student can check subject-wise attendance percentage.

System automatically calculates attendance percentage.

Student can view exam timetable.

Exam eligibility is displayed based on 75% attendance rule.

Student can log out securely.





### **4. Exam Department Module :**

Exam department user can log in securely.

Exam department can add exam timetable details (subject, date, time).

Exam department can view all exam schedules.

Exam department can update exam date and time.

Exam department can delete exam timetable records.

Exam department can log out securely.



### **5. Database & Security Features :**

Uses MS SQL Server for centralized data storage.

All database operations are performed using parameterized queries to prevent SQL injection.

Data is stored in structured tables like admin, teacher, student, attendance, and exam_timetable.

Role-based access ensures users can only perform allowed operations.

## **Class Details :**

The College ERP System follows an object-oriented approach where each role is implemented as a separate class. All classes inherit database connectivity from a common Database class.

### **1. Database Class**

This class connects the application to the database.

It creates a database connection and cursor.

All other classes use this class to access the database


### **2. Admin Class**

Used by the admin to manage the system.

Admin can log in to the system.

Admin can add, update, delete, and view teachers.

Admin can add, update, delete, and view exam department members.

Admin can log out after completing work.


### **3. Teacher Class**

Used by teachers to manage students and attendance.

Teacher can log in using username and password.

Teacher can add and delete students.

Teacher can take student attendance subject-wise.

Teacher can view all students.

Teacher can log out.

### **4. Student Class**


Used by students to check their academic details.

Student can log in using credentials.

Student can check subject-wise attendance percentage.

Student can view exam timetable.

System shows exam eligibility based on attendance.

Student can log out.



### **5. ExamDepartment Class**

Used by exam department staff to manage exams.

Exam department can log in securely.

Exam department can add, update, delete exam timetable.

Exam department can view exam timetable.

Exam department can log out.

### **6. Main Program**

Displays role selection menu.

Calls the correct class based on user choice.

Runs the system until the user exits.







## **Database Introduction**

The College ERP System uses a database named ERP to store and manage all college-related data. This database helps in maintaining records of admins, teachers, students, attendance, exams, and exam department members. It provides centralized storage, data security, and smooth interaction between different modules of the system.

## **Database Tables Description**
### **1. Admin Table**

Stores admin login details.

Used to authenticate the administrator.

Contains admin ID, username, and password.

### **2. Teacher Table**

Stores teacher information.

Includes teacher name, subject name, username, and password.

Used for teacher login and subject assignment.

### **3. Student Table**

Stores student details.

Includes student name, username, and password.

Used for student authentication and identification.

### **4. Attendance Table**

Stores student attendance records subject-wise.

Contains total classes and attended classes.

Used to calculate attendance percentage and exam eligibility.

### **5. Exam Timetable Table**

Stores exam schedule details.

Includes subject name, exam date, and exam time.

Used by students to view exam schedules.

### **6. Exam Department Table**

Stores exam department staff details.

Includes name, username, and password.

Used for managing exam timetables.







