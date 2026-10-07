# ==========================================
# Day 03 - Python Challenge
# ==========================================

# Challenge 01
# Calculate the average of three numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average:", average)


# Challenge 02
# Calculate total sales.

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total_sales = price * quantity

print("Total Sales:", total_sales)


# Challenge 03
# Calculate total marks and percentage.

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
sql = float(input("Enter SQL marks: "))

total_marks = maths + python + sql
percentage = total_marks / 3

print("Total Marks:", total_marks)
print("Percentage:", percentage)


# Challenge 04
# Calculate age after 5 years.

age = int(input("Enter your age: "))

future_age = age + 5

print("Age after 5 years:", future_age)








"""a =("Rohan","Rahul","Sumit","Ramesh","Suresh")

for i in a :
   print(i)"""


a =["Rohan","Rahul","Sumit","Ramesh","Suresh"]
a[1] = "sunil"
a[3] = "nilesh"


