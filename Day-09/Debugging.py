# ==================================================
# DAY 09 - PYTHON DEBUGGING CHALLENGE
# 30 Days Python Challenge for Data Analytics
# File: Debugging.py
# ==================================================


# Q01. Find and fix the error.
# Expected Output: Positive Number

number = 10

if number > 0:
    print("Positive Number")


# Q02. Find and fix the error.
# Expected Output: Negative Number

number = -5

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")


# Q03. Find and fix the error.
# Expected Output: Even Number

number = 8

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Q04. Find and fix the error.
# Expected Output: Pass

marks = 75

if marks >= 33:
 print("Pass")
else:
    print("Fail")


# Q05. Find and fix the error.
# Expected Output: Grade A

marks = 95

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# Q06. Find and fix the error.
# Expected Output: Second number is greater

a = 20
b = 40

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Both are Equal")


# Q07. Find and fix the error.
# Expected Output: Login Successful

username = "rohit"
password = "python123"

if username == "rohit" and password =="python123":
    print("Login Successful")
else:
    print("Invalid Credentials")


# Q08. Find and fix the error.
# Expected Output: Low Stock

stock = 5

if stock == 0:
    print("Out of Stock")
elif stock <= 10:
    print("Low Stock")
elif stock <= 50:
    print("Stock Available")
else:
    print("High Stock")


# Q09. Find and fix the error.
# Expected Output: Bonus: 5000

performance_score = 85
salary = 40000

if performance_score >= 80:
    if salary >= 50000:
        print("Bonus: 10000")
    else:
        print("Bonus: 5000")
else:
    print("No Bonus")


# Q10. Find and fix the error.
# Expected Output: Electricity Bill: Rs. 1700

units = 250

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print("Electricity Bill: Rs.", bill)


# ==================================================
# END OF DAY 09 - DEBUGGING CHALLENGE
# ==================================================