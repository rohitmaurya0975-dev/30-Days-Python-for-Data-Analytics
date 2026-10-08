# ==========================================
# Day 04 - Python Operators Challenge
# 30 Days Python Challenge for Data Analytics
# ==========================================


# Challenge 1: Employee Salary Calculator
# ----------------------------------------
# Take basic salary and bonus as input.
# Calculate the total salary.

salary = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus: "))

total_salary = salary + bonus

print("Total Salary:", total_salary)


# Challenge 2: Product Billing
# ----------------------------
# Take product price and quantity.
# Calculate the total bill.

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total_bill = price * quantity

print("Total Bill:", total_bill)


# Challenge 3: Discount Calculator
# --------------------------------
# Take total bill and discount percentage.
# Calculate discount amount and final amount.

bill = float(input("Enter total bill: "))
discount_percent = float(input("Enter discount percentage: "))

discount_amount = bill * discount_percent / 100
final_amount = bill - discount_amount

print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)


# Challenge 4: Average Marks
# --------------------------
# Take marks of 3 subjects.
# Calculate total marks and average.

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
sql = float(input("Enter SQL marks: "))

total_marks = maths + python + sql
average_marks = total_marks / 3

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)


# Challenge 5: Data Analyst Mini Challenge
# ----------------------------------------
# Take total sales and total expenses.
# Calculate profit and profit percentage.

sales = float(input("Enter total sales: "))
expenses = float(input("Enter total expenses: "))

profit = sales - expenses
profit_percentage = (profit / sales) * 100
print("Profit:", profit)
print("Profit Percentage:", profit_percentage)


# Challenge 6: Comparison Operators
# ----------------------------------
# Take two salaries and compare them.

salary1 = float(input("Enter Employee 1 salary: "))
salary2 = float(input("Enter Employee 2 salary: "))

print("Salary 1 > Salary 2:", salary1 > salary2)
print("Salary 1 < Salary 2:", salary1 < salary2)
print("Salary 1 == Salary 2:", salary1 == salary2)


# Challenge 7: Even or Odd
# ------------------------
# Take a number and check whether it is even or odd.
# Hint: Use the modulus (%) operator.

number = int(input("Enter a number: "))

print("Remainder:", number % 2)

if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


# ==========================================
# End of Day 04 Challenge
# ==========================================