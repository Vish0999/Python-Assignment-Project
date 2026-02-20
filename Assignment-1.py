# QUE 1)
# Find the output of the following
# Index 
# 1.	If  name = ''' Hi How are you?
# Starterd learning python.
# It's really interesting.''' Then what is the output of following code
# •	name[:] 
# •	name[-10:-5]
# •	name[3:12]
# •	name[12:3]
# •	name[5,6]
# •	name[-4:-12]
# •	name[::2]
# •	name[::-2]



name = ''' Hi How are you?
 Starterd learning python.
 It's really interesting.''' 
# it return whole string
print(name) 

# it return whole string
print(name[:]) 

 # it is string slicing it returns string from -10 index to -5 index
print(name[-10:-5])

# it return from index 3 to 12
print(name[3:12]) 

# it returns null output
print(name[12:3]) 

#incorrect syntax
print(name[5,6]) 

 # it returns index from -4 index to -12
print(name[-4:-12])

 # it returns whole string but it jump everytime 2 for example 2, 5, 8
print(name[::2])

# it return whole string but it jump everytime 2 for example -2
print(name[::-2]) 









# QUE 2)
# 2.	 L1 = [‘a’ , ‘b’, 20, 30, ‘t’, 100, 300, 400, ‘Happy’, ‘major’]
# a.	L1[:]
# b.	L1[::3]
# c.	L1[::-2]
# d.	How to extract  value “Happy” based on index and negative index
# e.	How to check type of data in list at 4th position
# f.	Extract values for 100, 300, 400 

L1 = ['a' , 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']

# it returns whole list
print(L1)

# it returns whole list
print(L1[:]) 

# it returns list by jumping 3 index
print(L1[::3]) 

# it returns list by jumping -2 index 
print(L1[::-2]) 

# it returns 'Happy' using positive index
print(L1[8]) 

 # it returns "happy" word with negative index
print(L1[-2])

# check type of data in list at 4th position
print(type(L1[4])) 

 # it returns 100,300,400 
print(L1[5:8])








# QUE 3)

# 3.	If l2 =[1,2,3,5,[‘a’, ‘b’, ‘work hard’],100 , 200, “Success”] then what is the output of following
# •	L2[4]
# •	L2[1:5]
# •	L2[7]
# •	L2[7][2]
# •	L7[7][2:]
# •	L2[ : 3]
# •	L2[3:]


l2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, "Success"]

 # it return ['a', 'b', 'work hard']
print(l2[4])

# it return [2, 3, 5, ['a', 'b', 'work hard']]
print(l2[1:5]) 

 # it returns items at position 7 index
print(l2[7])

# it extract word "success" index wise and return "c"
print(l2[7][2]) 

# it extract word "success" index wise and return "c,c,e,s,s"
print(l2[7][2:]) 

# it return list element upto index 3
print(l2[ : 3]) 

# it return list element from index 3 to last index
print(l2[3:])







# QUE 4)

# 4.	From the above l2 value ‘b’ must be changed to ‘BEE’.

l2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, "Success"]

l2[4][1] = 'BEE'
print(l2)





# QUE 5)

# 5.	From l2 “BEE” has to discard.
l2[4].remove("BEE")
print(l2)





# QUE 6)

#  6.	In l2 add a dictionary at the end {‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}


l2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, "Success"]

l2.extend( [{'insect': ['bee', 'moth'] , 'bird' : ['parrot', 'sparrow']}] )
print(l2)







# QUE 7)

# 7.	From l2 extract insect information.
print(l2[8]['insect'])





# QUE 8)

# 8.	Create a dictionary d1 = {‘a’:10, ‘b’:20, ‘c’ : 30} and add the d1 at 2nd position of l2
d1 = {'a':10, 'b':20, 'c' : 30}
l2.insert(2, d1)
print(l2)






# QUE9)

# 9.	Based on new l2 created here extract the value 10 from l2 dictionary.

print(l2[2]['a'])





# QUE 10)

# 10.	If l2 =[1,2,3,5, (90,40,50,10), ‘Python’, 400 ,[‘a’, ‘b’, ‘work hard’],100 , 200, “Success”, (200,300, “Hundreds”)] then what is the output of following
# •	L2[4][2]
# •	L2[5][:]
# •	L2[2] [:]
# •	L2[1:5]
# •	L2[5]
# •	L2[5][3:-1]
# •	L2[-1]
# •	L2[-4, -3]
# •	L2[-4: -10]
# •	L2[7][2]
# •	L7[-7][[2:]
# •	L2[ :- 3]
# •	L2[-3:]


l2 =[1,2,3,5, (90,40,50,10), 'Python', 400 ,['a', 'b', 'work hard'],100 , 200, "Success", (200,300, "Hundreds")]

# it returns output 50 from 4th position touple
print(l2[4][2]) 

# it returns list items from index 5 
print(l2[5][:])

# syntax errro
print(l2[2] [:]) 

# it returns list items from index 1 to 5
print(l2[1:5]) 

# it return value which at index 5
print(l2[5]) 


# it return values from 5th index to -1 index ho
print(l2[5][3:-1]) 

# it return -1 index value i.e "Hundreds"
print(l2[-1]) 

# syntax error
print(l2[-4, -3]) 

# empty list
print(l2[-4: -10])  

# it return output which at 7 index "work hard"
print(l2[7][2]) 


# it return "thon"
print(l2[-7][2:]) 

# it return values from 0 index to -3 index
print(l2[ :- 3]) 


# it return values from index -3 to last [200, 'Success', (200, 300, 'Hundreds')]
print(l2[-3:]) 







# QUE 11)
# 11.	Ask user to enter the marks and define if the user got distinction, first class, second class, pass, Fails
# If marks are more than 80 output must be “You got distinction”
# For marks more than 60 output must be “You got First class”
# Marks more than 40 will display “You got second class”
# Marks more than or equal to 35 “PASS” Otherwise Fail


marks = input("enter the marks : ")
m1 = float(marks)

if m1 <= 100 and m1 > 0 :
    if m1 >= 80 :
        print("You got distinction")
    elif m1 >= 60 :
        print("You got First class")
    elif m1 >= 40 :
        print("Second class")
    elif m1 >= 35 :
        print("pass")
    else:
        print("fail") 
else:
    print("marks should be between 0 to 100") 





# QUE 12)

# 12.	Ask user to enter information about salary of the employee per year and rating received as A, B, C, D
# If salary upto 5 lpa then increament based on ratings are  A = 16% , B=12%, C= 10%, D=6%
# If salary upto 10 lpa then increament based on ratings are  A = 14% , B=10%, C= 8%, D=6%
# If salary upto 15 lpa then increament based on ratings are  A = 8% , B=6%, C= 4%, D = no increment
# If salary upto 23 lpa then increament based on ratings are  A = 7% , B=5%, C= 4%, D=no




salary = float(input("Enter yearly salary in LPA: "))
rating = input("Enter rating (A/B/C/D): ").upper()

increment_percent = 0

# Salary up to 5 LPA
if salary <= 5:
    if rating == "A":
        increment_percent = 16
    elif rating == "B":
        increment_percent = 12
    elif rating == "C":
        increment_percent = 10
    elif rating == "D":
        increment_percent = 6

# Salary up to 10 LPA
elif salary <= 10:
    if rating == "A":
        increment_percent = 14
    elif rating == "B":
        increment_percent = 10
    elif rating == "C":
        increment_percent = 8
    elif rating == "D":
        increment_percent = 6

# Salary up to 15 LPA
elif salary <= 15:
    if rating == "A":
        increment_percent = 8
    elif rating == "B":
        increment_percent = 6
    elif rating == "C":
        increment_percent = 4
    elif rating == "D":
        increment_percent = 0

# Salary up to 23 LPA
elif salary <= 23:
    if rating == "A":
        increment_percent = 7
    elif rating == "B":
        increment_percent = 5
    elif rating == "C":
        increment_percent = 4
    elif rating == "D":
        increment_percent = 0

else:
    print("Salary out of range")

increment_amount = (salary * increment_percent) / 100
new_salary = salary + increment_amount

print("Increment Percentage:", increment_percent, "%")
print("Increment Amount:", increment_amount, "LPA")
print("New Salary:", new_salary, "LPA")






# QUE 13) 

# 13.	Ask user to opt for courses for master degree based on the following
# L1 = [“HR”, “Finance”, “Marketing”, “DS”]
# Based on above subject there are two different streams. For example- HR is having HR core and HR analytics and Marketing is having core and Marketing analytics. Analytics is the optional subject and having added extra fees. DS is not having analytics.
# If fees for L1 is 2 lakhs for each course core subject having the same fees but analytics subject having 10% extra on 2 lakhs.
# If student opts for hostel then 2 lakhs per year is added. For food monthly 2000 .
# Transportation charges 13000 per semester. Calculate the total annual cost based on selected service.  
# User will enter values as subject, analytics(Y/N), Hostel (Y/N), food(How many months?), Transportation(semester/annual)



def calculate_fee():
    try:
        print("Select course from  list : ")
        L1 = ["HR", "Finance", "Marketing"]

        for course in L1:
            print(course)

        courses = input("Enter course name : ")

        if courses not in L1:
            raise ValueError("Invalid course name ")

        stream = input("You want analytical stream or not analytics (Y/N) : ")
        hostel = input("You want hostel facility (Y/N) : ")

        food_months = int(input("Enter number of months for food : "))
        transportation = input("Enter transportation type (semester/annual) : ")

        base_fee = 200000
        total_fee = base_fee

        if stream.lower() == "y":
            total_fee += base_fee * 0.10

        
        if hostel.lower() == "y":
            total_fee += 200000

     
        total_fee += food_months * 2000

        
        if transportation.lower() == "semester":
            total_fee += 13000 * 2
        elif transportation.lower() == "annual":
            total_fee += 13000 * 4
        else:
            raise ValueError("Invalid transportation option")

        print("Total annual cost is :", total_fee)

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("Something went wrong :", e)


calculate_fee()











# QUE 14) 
# Digitalize the book allotment process for school. Charges are mentioned here in the given table:

import pandas as pd


def stationery_shop():
    try:
        books_charges = {
            "Hindi": {"1st-4th": 60, "5th-8th": 100, "9th-10th": 150},
            "Marathi": {"1st-4th": 60, "5th-8th": 100, "9th-10th": 150},
            "English": {"1st-4th": 80, "5th-8th": 100, "9th-10th": 150},
            "Science": {"1st-4th": 90, "5th-8th": 120, "9th-10th": 200},
            "Maths": {"1st-4th": 100, "5th-8th": 140, "9th-10th": 250}
        }

        notebooks_charges = {
            "square": {"100 pages": 40, "200 pages": 70},
            "4line": {"100 pages": 30, "200 pages": 50},
            "2line": {"100 pages": 30, "200 pages": 50},
            "single lines": {"100 pages": 60, "200 pages": 100},
            "a4 notebook": {"100 pages": 100, "200 pages": 180}
        }

        print("\nBooks Price List")
        print(pd.DataFrame(books_charges))

        print("\nNotebooks Price List")
        print(pd.DataFrame(notebooks_charges))

        total_price = 0

        order_data = {
            "item": [],
            "Subject/Notebook": [],
            "standards/Pages": [],
            "qty": [],
            "price": []
        }

        while True:
            order = input("\nEnter your order (book/notebook): ").lower()
            if order not in {"book", "notebook"}:
                raise ValueError("Invalid order type")

            order_data["item"].append(order)

            # BOOK 
            if order == "book":
                subject = input("Enter subject: ").title()
                stds = int(input("Enter standard (1-10): "))
                qty = int(input("Enter quantity: "))

                if subject not in books_charges:
                    raise ValueError("Invalid subject")

                if 1 <= stds <= 4:
                    std = "1st-4th"
                elif 5 <= stds <= 8:
                    std = "5th-8th"
                elif 9 <= stds <= 10:
                    std = "9th-10th"
                else:
                    raise ValueError("Invalid standard")

                price = books_charges[subject][std] * qty

                order_data["Subject/Notebook"].append(subject)
                order_data["standards/Pages"].append(std)
                order_data["qty"].append(qty)
                order_data["price"].append(price)

                total_price += price
                print(f"{subject} book price: {price} Rs")

            # NOTEBOOK 
            else:
                notebook = input("Enter notebook type: ").lower()
                pages = input("Enter pages (100/200): ")
                qty = int(input("Enter quantity: "))

                pages_key = pages + " pages"

                if notebook not in notebooks_charges:
                    raise ValueError("Invalid notebook type")

                if pages_key not in notebooks_charges[notebook]:
                    raise ValueError("Invalid page selection")

                price = notebooks_charges[notebook][pages_key] * qty

                order_data["Subject/Notebook"].append(notebook)
                order_data["standards/Pages"].append(pages_key)
                order_data["qty"].append(qty)
                order_data["price"].append(price)

                total_price += price
                print(f"{notebook} notebook price: {price} Rs")

            choice = input("\nAdd more items? (Y/N): ").lower()
            if choice != "y":
                break

        print("\n---------------- BILL ----------------")
        print(pd.DataFrame(order_data))
        print("Total price:", total_price, "Rs")

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("Unexpected Error:", e)


stationery_shop()





# QUE 15)





# QUE 16)






# QUE 17)

# Type Casting 
# Create a=100 
# •	Convert a to string 
# •	Convert a to list    
# •	Convert a to tuple  
# •	Convert a to dict 
# •	Convert a to set 
# •	Convert to float 
# Observe the errors and note it down for all conversions. 



a = 100
# •	Convert a to string 
print(str(a))
# •	Convert a to list  
print(list(a)) # TypeError: 'int' object is not iterable. We cannot convert an integer to a list directly because a list is a collection of items, and an integer is a single value. To convert an integer to a list, we need to put it inside a list, like this: [a]
# •	Convert a to tuple
print(tuple(a)) # TypeError: 'int' object is not iterable. Similar to the list conversion, we cannot convert an integer to a tuple directly because a tuple is also a collection of items. To convert an integer to a tuple, we need to put it inside a tuple, like this: (a,)
# •	Convert a to dict 
print(dict(a)) # TypeError: 'int' object is not iterable. We cannot convert an integer to a dictionary directly because a dictionary is a collection of key-value pairs, and an integer is a single value. To convert an integer to a dictionary, we need to create a key-value pair, like this: {key: a}
# •	Convert a to set 
print(set(a)) # TypeError: 'int' object is not iterable. We cannot convert an integer to a set directly because a set is a collection of unique items, and an integer is a single value. To convert an integer to a set, we need to put it inside a set, like this: {a}
# •	Convert to float 
print(float(a)) # it converts integer to float and return 100.0








# QUE 18)

# .	Create city = “Pune” 
# •	Convert to int     
# •	Convert float 
# •	Convert list  
# •	Convert tuple 
# •	Convert dict 
# •	Convert set 
# •	Obsert errors and note it down for all conversions 


city = "Pune"
# •	Convert to int
print(int(city)) # ValueError: invalid literal for int() with base 10: '
# convert to float
print(float(city)) # ValueError: could not convert string to float: 'Pune'
# •	Convert list
print(list(city)) # it converts string to list and return ['P', 'u', 'n', 'e']
# •	Convert tuple
print(tuple(city)) # it converts string to tuple and return ('P', 'u', 'n', 'e')
# •	Convert dict
print(dict(city)) # TypeError: cannot convert dictionary update sequence element #0 to a sequence
# •	Convert set
print(set(city)) # it converts string to set and return {'P', 'u', 'n', 'e'}









# QUE 19
# 	Create a list as marks = [20,18,15,17,18] 
# •	Convert to int 
# •	Convert float 
# •	Convert list 
# •	Convert tuple 
# •	Convert dict 
# •	Convert set 
# •	observe : errors and note it down for all conversions 


marks = [20,18,15,17,18]
# •	Convert to int
print(int(marks)) # TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
# •	Convert to float    
print(float(marks)) # TypeError: float() argument must be a string or a number, not 'list'
# •	Convert to list
print(list(marks)) # it returns the same list [20, 18, 15, 17, 18]
# •	Convert to tuple
print(tuple(marks)) # it converts list to tuple and return (20, 18, 15, 17, 18)
# •	Convert to dict
print(dict(marks)) # TypeError: cannot convert dictionary update sequence element #0 to a sequence
# •	Convert to set
print(set(marks)) # it converts list to set and return {18, 20, 17, 15}








# QUE 20

# List operations 
# .	Create the empty list snames 
# •	 Add value 20 in the list using append 
# •	 Add value 30 in the list using extend 
# •	Add values in the list using append 
# •	Add value “WORK" in the list using extend 
# •	 Create a new list combo having the values [1, ‘a’, ‘b’ ,2 , 3] 
# •	Add sname to combo using addition operator 
# •	Add combo to snames using append 
# •	Add combo to snames using extend. 


snames = []
# •	 Add value 20 in the list using append
snames.append(20)
print(snames)
# •	 Add value 30 in the list using extend
snames.extend([30])
print(snames)
# •	Add values in the list using append
snames.append([40,50])
print(snames)
# •	Add value “WORK" in the list using extend
snames.extend(["WORK"])
print(snames)
# •	 Create a new list combo having the values [1, ‘a’, ‘b’ ,2 , 3]
combo = [1, 'a', 'b' ,2 , 3]
# •	Add sname to combo using addition operator
combo = combo + snames 
print(combo)
# •	Add combo to snames using append
snames.append(combo)
print(snames)
#   •	Add combo to snames using extend.
snames.extend(combo)
print(snames)






# QUE 21
# 	Create one list l1 having two elements and l3 having 7 elements. Now at 4th position add l1 

l1 = [2,3]
print(l1)
l2 = [1,2,3,4,5,6,7]
print(l2)
l2.insert(4,l1)

print(l2)








# QUE 21

# .	Collection is the list having values [1,2,3,[‘a’, ‘b’, ‘c’], 100, ‘Nisha’, 20.50, 90.10 ] if the data is in integer or float then multiply with 5.  
# •	From the collection delete the record for “Nisha” 
# •	Find the location of 20.50 



collection = [1, 2, 3, ['a', 'b', 'c'], 100, 'Nisha', 20.50, 90.10]

for i in range(len(collection)):
    if isinstance(collection[i], (int, float)):
        collection[i] = collection[i] * 5

if "Nisha" in collection:
    collection.remove("Nisha")

value_to_find = 20.50 * 5
index = collection.index(value_to_find)

print("Updated Collection:", collection)
print("Location of 20.50:", index)









# QUE 22)
# 	Create a comprehensive list for square upto 10 

l1 = [ n**2 for n in range(1,10)]
print(l1)






# QUE 23)
# Create the comprehensive list to find number divisible by 13 till 200

l1 = [n for n in range(0,200) if n%13 == 0]
print(l1)






# QUE 24)
# Create the list which is divisible by 4 from 300 to 400  

l1 = [n for n in range(300,400) if n%4 == 0]
print(l1)







# QUE 25)
# Create a comprehensive list to generate list up to x, y as a number. For example if x = 3 list will be x_list = [0,1,2] and y=2 then y_list =[0,1]
# Then generate a new list based on all combination of x and y.
# For example: if x = 1 and y =2  then x_list = [0] and y_list = [0,1]
# And output will be [[0,0],[0,1]]
# If x=2 and y = 2 then output will be [[0,0],[0,1][1,0],[1,1]]


x = 2
y = 2
x_list = [i for i in range(x)]
y_list = [j for j in range(y)]
print(x_list)  # [0, 1]
print(y_list)  # [0, 1]

result = [[i, j] for i in x_list for j in y_list]
print(result)







# QUE 26)
# Create the set s1 and s2 and perform set operations like union, intersection, difference, set difference.

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print("Set s1:", s1)
print("Set s2:", s2)
print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference (s1 - s2):", s1 - s2)
print("Set Difference (s2 - s1):", s2 - s1)




# QUE 27
# Create l2 as a list and perform set operation on s1 with l1 

s1 = {1, 2, 3, 4, 5}
l2 = [4, 5, 6, 7, 8]

s2 = set(l2)

print("Set s1:", s1)
print("List l2:", l2)
print("Union:", union_set = s1 | s2)
print("Intersection:", s1 & s2)
print("Difference (s1 - l2):",  s1 - s2)
print("Difference (l2 - s1):", s2 - s1)





# QUE 28
# Ask user to enter the name and DOB and generate the password based on first name 4 characters and  @ddmm. For example name = SURESH and DOB = 05-05-1978 then password will be SURE@0505 

name = input("Enter your name: ")
dob = input("Enter your DOB (dd-mm-yyyy): ")
first_part = name[:4]
day, month, year = dob.split("-")
dob_part = day + month
password = first_part.upper() + "@" + dob_part
print("Generated Password:", password)






# QUE 29
# Ask user to enter the name and DOB and generate the password based on first name 4 characters and  last 4 digits of DOB or year @yyyy. For example name = SURESH and DOB = 05-05-1978 then password will be SURE@1978 

name = input("Enter your name: ")
dob = input("Enter your DOB (dd-mm-yyyy): ")
name_part = name[:4]
day, month, year = dob.split("-")
password = name_part.upper() + "@" + year
print("Generated Password:", password)








# QUE 30
# Create the format mentioned here.
# *
# * *
# * * *
# * * * *

for i in range(5):
    print("*"*i)





# QUE 31
# .	Create the format as mentioned below:
# ****
# ***
# **
# *

for i in range(5,-1,-1):
    print("*"*i)





# QUE 32

# Str_val = “ABCD” then create the format as mentioned below:
# A
# A B
# A B C
# A B C D

Str_val = "ABCD"
l1 = ""
for i in range(len(Str_val)):
    l1 = l1 + Str_val[i]
    print(l1)




# QUE 33)
# Create the format mentioned below:
# A
# BB
# CCC
# DDDD

Str_val = "ABCD"
for i in range(len(Str_val)):
    print(Str_val[i] * (i+1))






# QUE 34)
# 	Create the format mentioned below:
# 1
# 22
# 333
# 4444

for i in range(1, 5):
    print(str(i) * i)




#  QUE 35
# Val = “ABCD”  based on the Val, create the format mentioned below
# D
# DC
# DCB
# DCBA

val = "ABCD"
l1 = ""
for i in range(len(val)-1,-1,-1):
    l1 = l1 + val[i]
    print(l1)





# QUE 36)
# Ask user to enter the string. If string is UPGRAD then output must be
# D
# DA
# DAR
# DARG
# DARGP
# DARGPU


val = input("enter string")
l1 = ""
if val.upper() == "UPGRAD":
    for i in range(len(val)-1,-1,-1):
        l1 = l1 + val[i]
        print(l1)
else:
    print("no pattern")






# QUE 37)
# Create a list of odd numbers from 1 to 10
# 1.	Using for loop
# 2.	Using comprehensive list

odd_numbers = []
for i in range(1, 11):
    if i % 2 != 0:
        odd_numbers.append(i)
print("Odd numbers (for loop):", odd_numbers)

odd_numbers2 = [i for i in range(1, 11) if i % 2 != 0]
print("Odd numbers (list comprehension):", odd_numbers2)






# QUE 38)
# Create even number list using for loop from 200 to 250

even_numbers = []

for i in range(200, 251):
    if i % 2 == 0:
        even_numbers.append(i)
print( even_numbers)





# QUE 39)
# List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
# Multiply each and every element by 2 and display the answer


List2 = [2, 70, 'work', 'para', 2.5, [1, 2, 3], (1, 2), {1, 2}, {1: 'a', 2: 'b'}, 3, 10, 302.5]
result = []

for item in List2:
    if type(item) in {int, float, str, list, tuple}:
        result.append(item * 2)
    else:
        result.append(item)

print("Original List:")
print(List2)

print("Result after multiplying by 2:")
print(result)







# QUE 40)
# List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
# Multiply each and every element from list2 by 2 and store the answer in list3

list2 = [2, 70, 'work', 'para', 2.5, [1, 2, 3], (1, 2), {1, 2}, {1: 'a', 2: 'b'}, 3, 10, 302.5]

list3 = []

for item in list2:
    if isinstance(item, (int, float, str, list, tuple)):
        list3.append(item * 2)
    else:
        list3.append(item)

print("List2:", list2)
print("List3:", list3)






# QUE 41)
# Create a function to accept marks from user utilize exception concept to validate proper marks.

def accept_marks():
    try:
        marks = int(input("Enter marks (0 to 100): "))

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        print("Valid marks entered:", marks)

    except ValueError as ve:
        print("Invalid input :", ve)

    except Exception as e:
        print("Error:", e)


accept_marks()






# QUE 42)
# Create a function to validate user first name/last name. User first name/last name should contain only characters. No special characters, numbers, space in name 

def check_name(firstName, lastName):
    try:
        if not firstName.isalpha() or not lastName.isalpha():
            raise ValueError("Name must contain only alphabets")

        return f"Valid name Mr {firstName} {lastName}"

    except ValueError as e:
        return f"Invalid name: {e}"

firstName = input("enter your FName : ")
LName = input("enter your FName : ")

a = check_name(firstName, LName)
print(a)







# QUE 43)
# Create a function to accept mobile number. Mobile number should contain 10 digits. No Special character, alphabets and space. 
def check_mb(mobile):
    if len(mobile) != 10 or not mobile.isdigit():
        raise ValueError("invalid values !!!! sir !!")
    try:
        return "hey buddy your mobile number {m} is correct !!!!!".format(m = mobile)
    except:
        return "invalide number !!!!!!"
    
mb = input("enter your number : ")
print(len(mb))
result = check_mb(mb)
print(result)






# QUE 44)
#Create a function to generate auto-password based on specific person details. Ask user to enter name, DOB. And password must be First name 4 characters and year of birth.

def auto_pass(name, dob):
    if not name.isalpha():
            raise ValueError("please check name !!  name should be alphabetical  ")
    try: 
            pass1 = name[:4]
            dob_pass = dob[::-1] 
            pass2 = dob_pass[0:4]
            dob_pass = pass2[::-1]
            password = pass1 + dob_pass
            return "your password is : {pas}".format(pas = password )
    except ValueError:
        print("errro") 

n = input("enter your name: ")
dob = input("enter your DOB in format DD/MM/YYYY: ")

result = auto_pass(n, dob)
print(result)







# QUE 45)
# Create a empty dictionary and ask user to enter values as name, DOB, mobile number add all the details in dictionary with customer number as 1 for first time. If user try to enter another value, then number should increase as 2 with new details and previous values should not change.
# For example:
# {}
# {1:{name : "Sachin", "DOB": "21-06-1965" , "mobile": "1234123423"}}
# {1:{name : "Sachine", "DOB": "21-06-1965" , "mobile": "1234123423"},
# 2: {name : "Sumedh", "DOB": "02-02-2002" , "mobile": "1234123433"}}

d1 = {}
number  = 1
while True:
    choice = input("do you want to add your details : Yes/No")
    if choice.lower() in {"y","yes"}:
        try:
            name = input("enter your name : ")
            if not name.isalpha():
                raise ValueError("Name must contain only alphabets")
            dob = input("enter your DOB in format dd-mm-yyyy :")
            mobile = input("enter your mobile number : ")
            if len(mobile) != 10 and not mobile.isdigit():
                raise ValueError("Mobile number must be exactly 10 digits")
            d1[number] = {
                    "name" : name,
                    "DOB" : dob,
                    "Mobile": mobile 
                }
            number += 1

        except ValueError as e:
            print("renter details")
            print("error", e)

        
    else :
        break

print(d1)









# QUE 46)
# Based on the above example create the dictionary and save the same in a cust_info.txt or cust_info.log

d1 = {}
number = 1

while True:
    choice = input("Do you want to add your details (Yes/No): ")

    if choice.lower() in {"y", "yes"}:
        try:
            name = input("Enter your name: ")
            if not name.isalpha():
                raise ValueError("Name must contain only alphabets")

            dob = input("Enter your DOB (dd-mm-yyyy): ")

            mobile = input("Enter your mobile number: ")
            if len(mobile) != 10 or not mobile.isdigit():
                raise ValueError("Mobile number must be exactly 10 digits")

            d1[number] = {
                "name": name,
                "DOB": dob,
                "mobile": mobile
            }

            number += 1

        except ValueError as e:
            print("Re-enter details")
            print("Error:", e)

    else:
        break

try:
    with open("cust_info.txt", "w") as file:
        for cust_no, details in d1.items():
            file.write(f"Customer No: {cust_no}\n")
            for key, value in details.items():
                file.write(f"{key} : {value}\n")
            file.write("\n")

    print("Customer details saved successfully in cust_info.txt")

except Exception as e:
    print("File error:", e)

print(d1)









#  QUE 47)
# 43.	Based on the above example read the file cust_info.txt . check if dictionary any information is available in the file. If there is information then read the dictionary store into one variable and then append new information of customer if added.

d1 = {}

try:
    with open("cust_info.txt", "r") as file:
        lines = file.readlines()

    cust_no = None
    for line in lines:
        line = line.strip()

        if line.startswith("Customer No"):
            cust_no = int(line.split(":")[1])
            d1[cust_no] = {}

        elif ":" in line and cust_no is not None:
            key, value = line.split(":", 1)
            d1[cust_no][key.strip()] = value.strip()

except FileNotFoundError:
    print("File not found. New file will be created.")
except Exception as e:
    print("Error while reading file:", e)


number = max(d1.keys()) + 1 if d1 else 1


while True:
    choice = input("Do you want to add new customer details (Yes/No): ")

    if choice.lower() in {"y", "yes"}:
        try:
            name = input("Enter name: ")
            if not name.isalpha():
                raise ValueError("Name must contain alphabets only")

            dob = input("Enter DOB (dd-mm-yyyy): ")

            mobile = input("Enter mobile number: ")
            if len(mobile) != 10 or not mobile.isdigit():
                raise ValueError("Mobile number must be 10 digits")

            d1[number] = {
                "name": name,
                "DOB": dob,
                "mobile": mobile
            }

            number += 1

        except ValueError as e:
            print("Invalid input:", e)

    else:
        break

try:
    with open("cust_info.txt", "w") as file:
        for cust_no, details in d1.items():
            file.write(f"Customer No: {cust_no}\n")
            for key, value in details.items():
                file.write(f"{key} : {value}\n")
            file.write("\n")

    print("Customer information updated successfully")

except Exception as e:
    print("Error while writing file:", e)

print("\nFinal Dictionary:")
print(d1)








# QUE 48
# Dict1= {“Key”: {“subkey”:20} ,  “k2”:{“sub2” : 5}, “k3” : {“sub4” :16},  “k4” : {“sub4” : 6}}
# Sort elements based on values
# Output must be {,  “k2”:{“sub2” : 5}, “k4” : {“sub4” : 6},  “k3” : {“sub4” : 16}, “Key”:{“subkey”:20}}

Dict1 = {
    "Key": {"subkey": 20},
    "k2": {"sub2": 5},
    "k3": {"sub4": 16},
    "k4": {"sub4": 6}
}

sorted_dict = dict(
    sorted(
        Dict1.items(),
        key=lambda item: list(item[1].values())[0]
    )
)

print(sorted_dict)








# QUE 49
# Create a function to calculate age till now.

from datetime import date

def calculate_age():
    try:
        dob = input("Enter your DOB (dd-mm-yyyy): ")

        day, month, year = map(int, dob.split("-"))
        birth_date = date(year, month, day)
        today = date.today()

        if birth_date > today:
            raise ValueError("DOB cannot be in future")

        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        print("Your age is:", age, "years")

    except ValueError as ve:
        print("Invalid input :", ve)

    except Exception as e:
        print("Error :", e)

calculate_age()








# # QUE 50)
# Create a function to check age eligibility for given customer based on DOB. Function will take two input DOB and ELIGIBILITY age.

from datetime import date

def check_voting_eligibility(dob):
    day, month, year = map(int, dob.split("-"))
    birth_date = date(year, month, day)
    today = date.today()

    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    if age >= 18:
        return "Eligible for voting"
    else:
        return "Not eligible for voting"

print(check_voting_eligibility("15-08-2008"))







# QUE 51)
# Create a function to check if string is palindrome or not ? For example, if input is NITIN then reverse of the string is same then it is palindrome. If input is ANIL then reverse is LINA which is not same then it is not palindrome.  

def check_palindrome(word):
    reverse_word = word[::-1]

    if word == reverse_word:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(check_palindrome("NITIN"))
print(check_palindrome("ANIL"))







#  QUE 52

# Create a function to generate a Fibonacci Series. 0 1 1 2 3 5 8 13 21 34 …..  upto 100 
def fib_series():
    a, b = 0, 1
    print(a, b, end=" ")

    while True:
        c = a + b
        if c > 100:
            break
        print(c, end=" ")
        a, b = b, c

fib_series()







#  QUE 53
# Write a code to generate factorial of the number  For example: factorial of 5 = 5! = 5*4*3*2*1

def fact(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

fact(5)







# QUE 54
# Write a program to find largest number in the list.
num = [333,66,77,22,99]
print(max(num))







# QUE 55 )
# Write a program to check frequency of each element in the list.
num = [333,66,77,22,99]
for i in num:
    print(i, ":", num.count(i))




# QUE 56)
# There are two string l1 =[ 1,2,3,4,5] and l2 =[3,2,8,7,9] then write a program to find common elements in the list.

l1 =[ 1,2,3,4,5]
l2 =[3,2,8,7,9] 
print(list(set(l1) & set(l2)))







# QUE 57)


#divide files into different folders base on their size

import os
import shutil

os.mkdir("helloooPython")
folder_path = r"D:\Bizmetric Training\Python_Training\helloooPython"

small_dir = r"D:\Bizmetric Training\Python_Training\Small-Size"
mid_dir   = r"D:\Bizmetric Training\Python_Training\Mid-Size"
large_dir = r"D:\Bizmetric Training\Python_Training\Large-Size"

os.makedirs(small_dir, exist_ok=True)
os.makedirs(mid_dir, exist_ok=True)
os.makedirs(large_dir, exist_ok=True)

count = 0
for root, dirs, files in os.walk(folder_path):
     for file in files:
          file_path  = os.path.join(root,file) 
          size_bytes = os.path.getsize(file_path)
          size_kb = size_bytes // 1024
          print("size of file :",file_path, " : ", size_kb)

          if size_kb < 20:
            shutil.copy2(file_path, small_dir)

          elif 20 <= size_kb <= 100:
             shutil.copy2(file_path, mid_dir)

          else:
              shutil.copy2(file_path, large_dir)
                
          count += 1

print("Total files:", count)


