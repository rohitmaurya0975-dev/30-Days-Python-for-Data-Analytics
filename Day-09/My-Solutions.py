# ============================================
# DAY 09 - PYTHON CONDITIONAL STATEMENTS
# 30 Days Python Challenge for Data Analytics
# File: My-Solutions.py
# ============================================


# Q01. Positive Number

number = 10

if number > 0:
    print("Positive Number")


# Q02. Even or Odd

number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Q03. Pass or Fail

marks = 75

if marks >= 33:
    print("Pass")
else:
    print("Fail")


# Q04. Voting Eligibility

age = 20

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")


# Q05. Compare Two Numbers

a = 25
b = 40

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Both are Equal")


# Q06. Grade Calculator

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 33:
    print("Grade D")
else:
    print("Fail")


# Q07. Largest of Three Numbers

a = 25
b = 60
c = 40

if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)


# Q08. Discount Calculator

amount = 4000

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

final_amount = amount - discount

print("Purchase Amount:", amount)
print("Discount:", discount)
print("Final Amount:", final_amount)


# Q09. Positive, Negative, or Zero

number = -5

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")


# Q10. Login Check

username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")


# Q11. Nested if - Positive, Even or Odd

number = 8

if number > 0:
    if number % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Number is not Positive")


# Q12. Employee Bonus

performance_score = 85
salary = 45000

if performance_score >= 80:
    if salary >= 50000:
        print("Bonus: 10000")
    else:
        print("Bonus: 5000")
else:
    print("No Bonus")


# Q13. Sales Performance

sales = 75000

if sales >= 100000:
    print("Excellent")
elif sales >= 50000:
    print("Good")
elif sales >= 20000:
    print("Average")
else:
    print("Low")


# Q14. Profit or Loss

revenue = 80000
cost = 60000

if revenue > cost:
    print("Profit:", revenue - cost)
elif revenue < cost:
    print("Loss:", cost - revenue)
else:
    print("No Profit No Loss")


# Q15. Inventory Alert

stock = 8

if stock == 0:
    print("Out of Stock")
elif stock <= 10:
    print("Low Stock")
elif stock <= 50:
    print("Stock Available")
else:
    print("High Stock")


# Q16. Electricity Bill Calculator

units = 250

if units < 0:
    print("Invalid Units")
elif units <= 100:
    bill = units * 5
    print("Electricity Bill:", bill)
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    print("Electricity Bill:", bill)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    print("Electricity Bill:", bill)

