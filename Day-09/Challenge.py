# ==================================================
# DAY 09 - PYTHON CHALLENGE
# 30 Days Python Challenge for Data Analytics
# File: Challenge.py
# ==================================================

# Instructions:
# 1. Har challenge ko khud solve karne ki koshish karo.
# 2. if, elif, else aur comparison operators use karo.
# 3. Jahan zaroori ho, nested if use karo.
# 4. Abhi solutions copy karne ke bajay khud practice karo.


# ==================================================
# CHALLENGE 01 - Age Category
# ==================================================
# User se age input lo.
#
# Conditions:
# Age below 13       -> Child
# Age 13 to 19       -> Teenager
# Age 20 to 59       -> Adult
# Age 60 or above    -> Senior Citizen
#
# Negative age ke liye "Invalid Age" print karo.

age =int(input("enter your age "))
if age <13 :
   print("I AM A CHILDREN")
elif age <19  :
   print("Teenager")   
elif age <59:
   print("Adult")
else:
   print("Senier Citizen")
 
# Write your code below:


# ==================================================
# CHALLENGE 02 - Number Checker
# ==================================================
# User se ek number input lo.
#
# Check karo:
# Number positive, negative ya zero hai.
# Agar number positive hai, toh even ya odd bhi check karo.


# Write your code below:

number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")

    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

elif number < 0:
    print("Negative Number")
else:
    print("Zero")


# ==================================================
# CHALLENGE 03 - Result Calculator
# ==================================================
# User se marks input lo.
#
# Conditions:
# Marks 90 or above  -> Excellent
# Marks 75 or above  -> Very Good
# Marks 60 or above  -> Good
# Marks 33 or above  -> Pass
# Marks below 33     -> Fail
#
# Marks 0 se kam ya 100 se zyada hon toh
# "Invalid Marks" print karo.


# Write your code below:

marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Very Good")
elif marks >= 60:
    print("Good")
elif marks >= 33:
    print("Pass")
else:
    print("Fail")

# ==================================================
# CHALLENGE 04 - Shopping Discount
# ==================================================
# User se purchase amount input lo.
#
# Conditions:
# Amount >= 10000 -> 25% discount
# Amount >= 5000  -> 15% discount
# Amount >= 2000  -> 10% discount
# Amount >= 1000  -> 5% discount
# Amount < 1000   -> No discount
#
# Negative amount ke liye "Invalid Amount" print karo.
#
# Print:
# Original Amount
# Discount
# Final Amount


# Write your code below:

amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid Amount")
else:
    if amount >= 10000:
        discount_rate = 0.25
    elif amount >= 5000:
        discount_rate = 0.15
    elif amount >= 2000:
        discount_rate = 0.10
    elif amount >= 1000:
        discount_rate = 0.05
    else:
        discount_rate = 0

    discount = amount * discount_rate
    final_amount = amount - discount

    print("Original Amount:", amount)
    print("Discount:", discount)
    print("Final Amount:", final_amount)

# ==================================================
# CHALLENGE 05 - Login System
# ==================================================
# Correct username: rohit
# Correct password: python123
#
# User se username aur password input lo.
#
# Dono correct hon:
# "Login Successful"
#
# Username ya password galat ho:
# "Invalid Credentials"


# Write your code below:


username = input("Enter username: ")
password = input("Enter password: ")

if username == "rohit" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")

# ==================================================
# CHALLENGE 06 - Largest of Three Numbers
# ==================================================
# User se three numbers input lo.
#
# if, elif aur else ka use karke
# sabse bada number print karo.
#
# Agar numbers equal hon, tab bhi
# correct largest value print honi chahiye.


# Write your code below:

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest Number:", a)
elif b >= a and b >= c:
    print("Largest Number:", b)
else:
    print("Largest Number:", c)


# ==================================================
# CHALLENGE 07 - Profit or Loss Analyzer
# ==================================================
# User se revenue aur cost input lo.
#
# Revenue > Cost -> Profit
# Revenue < Cost -> Loss
# Revenue == Cost -> No Profit No Loss
#
# Profit ya loss ki amount bhi print karo.
# Negative revenue ya cost ko invalid input mano.


# Write your code below:

revenue = float(input("Enter revenue: "))
cost = float(input("Enter cost: "))

if revenue < 0 or cost < 0:
    print("Invalid Input")
elif revenue > cost:
    print("Profit:", revenue - cost)
elif revenue < cost:
    print("Loss:", cost - revenue)
else:
    print("No Profit No Loss")

# ==================================================
# CHALLENGE 08 - Inventory Alert
# ==================================================
# User se stock quantity input lo.
#
# Stock == 0       -> Out of Stock
# Stock <= 10      -> Low Stock
# Stock <= 50      -> Stock Available
# Stock > 50       -> High Stock
#
# Negative stock ke liye "Invalid Stock" print karo.


# Write your code below:


# ==================================================
# CHALLENGE 09 - Employee Bonus
# =================
stock = int(input("Enter stock quantity: "))

if stock < 0:
    print("Invalid Stock")
elif stock == 0:
    print("Out of Stock")
elif stock <= 10:
    print("Low Stock")
elif stock <= 50:
    print("Stock Available")
else:
    print("High Stock")

# User se performance score aur salary input lo.
#
# Score >= 80:
#     Salary >= 50000 -> Bonus 10000
#     Salary < 50000  -> Bonus 5000
#
# Score below 80 -> No Bonus
#
# Score 0-100 ke beech hona chahiye.
# Negative salary ya score 100 se zyada ho,
# toh invalid input print karo.


# Write your code below:

score = float(input("Enter performance score (0-100): "))
salary = float(input("Enter employee salary: "))

if score < 0 or score > 100 or salary < 0:
    print("Invalid Input")

elif score >= 80:
    if salary >= 50000:
        print("Bonus: 10000")
    else:
        print("Bonus: 5000")

else:
    print("No Bonus")

# ==================================================
# CHALLENGE 10 - Electricity Bill
# ==================================================
# User se electricity units input lo.
#
# First 100 units  -> Rs. 5 per unit
# Next 100 units   -> Rs. 7 per unit
# Above 200 units  -> Rs. 10 per unit
#
# Example:
# Units = 250
# Bill = 100*5 + 100*7 + 50*10
# Bill = Rs. 1700
#
# Negative units ke liye "Invalid Units" print karo.


# Write your code below:


units = float(input("Enter electricity units: "))

if units < 0:
    print("Invalid Units")

elif units <= 100:
    bill = units * 5
    print("Electricity Bill: Rs.", bill)

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    print("Electricity Bill: Rs.", bill)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    print("Electricity Bill: Rs.", bill)

# ==================================================
# BONUS CHALLENGE - Sales Performance Analyzer
# ==================================================
# User se product name, sales aur target input lo.
#
# Sales >= Target:
#     "Target Achieved"
#     Sales >= Target * 1.5:
#         "Outstanding Performance"
#
# Sales < Target:
#     "Target Not Achieved"
#
# Sales aur target negative nahi hone chahiye.
#
# Product name aur final performance status print karo.


# Write your code below:


product_name = input("Enter product name: ")
sales = float(input("Enter sales amount: "))
target = float(input("Enter sales target: "))

if sales < 0 or target < 0:
    print("Invalid Sales or Target")

else:
    if sales >= target:
        if sales >= target * 1.5:
            status = "Outstanding Performance"
        else:
            status = "Target Achieved"
    else:
        status = "Target Not Achieved"

    print("Product:", product_name)
    print("Sales:", sales)
    print("Target:", target)
    print("Performance:", status)
# ==================================================
# END OF DAY 09 CHALLENGE
# ==================================================