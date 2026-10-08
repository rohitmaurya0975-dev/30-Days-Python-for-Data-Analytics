# ==========================================
# Day 04 - Debugging Practice
# Python Operators
# ==========================================


# Q1. Find and fix the mistake
# Problem: Addition is not giving the correct result.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Wrong:
# result = num1 + num2

# Correct:
result = int(num1) + int(num2)

print("Sum:", result)


# ------------------------------------------
# Q2. Find and fix the mistake
# Problem: Total bill is incorrect.

price = 500
quantity = 3

# Wrong:
# total = price + quantity

# Correct:
total = price * quantity

print("Total Bill:", total)


# ------------------------------------------
# Q3. Find and fix the mistake
# Problem: Discount amount is incorrect.

bill = 2000
discount = 10

# Wrong:
# discount_amount = bill - discount

# Correct:
discount_amount = bill * discount / 100

print("Discount Amount:", discount_amount)


# ------------------------------------------
# Q4. Find and fix the mistake
# Problem: Final amount is incorrect.

bill = 3000
discount_amount = 300

# Wrong:
# final_amount = bill + discount_amount

# Correct:
final_amount = bill - discount_amount

print("Final Amount:", final_amount)


# ------------------------------------------
# Q5. Find and fix the mistake
# Problem: Average marks are incorrect.

maths = 80
python = 90
sql = 70

# Wrong:
# average = maths + python + sql / 3

# Correct:
average = (maths + python + sql) / 3

print("Average Marks:", average)


# ------------------------------------------
# Q6. Find and fix the mistake
# Problem: Even/Odd result is incorrect.

number = 15

# Wrong:
# if number / 2 == 0:

# Correct:
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ------------------------------------------
# Q7. Find and fix the mistake
# Problem: Comparison is not working correctly.

salary1 = 50000
salary2 = 45000

# Wrong:
# print(salary1 = salary2)

# Correct:
print(salary1 == salary2)


# ------------------------------------------
# Q8. Find and fix the mistake
# Problem: Profit calculation is incorrect.

sales = 50000
expenses = 35000

# Wrong:
# profit = sales + expenses

# Correct:
profit = sales - expenses

print("Profit:", profit)


# ------------------------------------------
# Q9. Find and fix the mistake
# Problem: Profit percentage is incorrect.

sales = 60000
profit = 12000

# Wrong:
# profit_percentage = profit / sales

# Correct:
profit_percentage = (profit / sales) * 100

print("Profit Percentage:", profit_percentage)


# ------------------------------------------
# Q10. Find and fix the mistake
# Problem: The program should calculate
# the total price correctly.

price = 250
quantity = 4

# Wrong:
# total_price = price / quantity

# Correct:
total_price = price * quantity

print("Total Price:", total_price)


# ==========================================
# End of Day 04 Debugging
# ==========================================