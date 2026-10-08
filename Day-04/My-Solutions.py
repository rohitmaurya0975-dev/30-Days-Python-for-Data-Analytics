# 🐍 30 Days Python Challenge — DAY 04

# My Solutions

# Topic: Operators

# ============================================================

# 🔹 ARITHMETIC OPERATORS

# ============================================================

# Q1. Add 25 and 15.

answer_1 = 25 + 15
print("Q1:", answer_1)

# Q2. Subtract 30 from 100.

answer_2 = 100 - 30
print("Q2:", answer_2)

# Q3. Multiply 12 by 5.

answer_3 = 12 * 5
print("Q3:", answer_3)

# Q4. Divide 100 by 4.

answer_4 = 100 / 4
print("Q4:", answer_4)

# Q5. Find the remainder when 25 is divided by 4.

answer_5 = 25 % 4
print("Q5:", answer_5)

# Q6. Find the floor division of 25 by 4.

answer_6 = 25 // 4
print("Q6:", answer_6)

# Q7. Calculate 2 raised to the power of 5.

answer_7 = 2 ** 5
print("Q7:", answer_7)

# ============================================================

# 🔹 COMPARISON OPERATORS

# ============================================================

# Q8. Check whether 50 is equal to 50.

answer_8 = 50 == 50
print("Q8:", answer_8)

# Q9. Check whether 75 is greater than 50.

answer_9 = 75 > 50
print("Q9:", answer_9)

# Q10. Check whether 25 is less than 20.

answer_10 = 25 < 20
print("Q10:", answer_10)

# Q11. Check whether 100 is not equal to 90.

answer_11 = 100 != 90
print("Q11:", answer_11)

# Q12. Check whether 50 is greater than or equal to 50.

answer_12 = 50 >= 50
print("Q12:", answer_12)

# Q13. Check whether 40 is less than or equal to 30.

answer_13 = 40 <= 30
print("Q13:", answer_13)

# ============================================================

# 🔹 ASSIGNMENT OPERATORS

# ============================================================

# Q14. Increase sales by 10000 using +=.

sales = 50000
sales += 10000
print("Q14:", sales)

# Q15. Decrease expenses by 5000 using -=.

expenses = 30000
expenses -= 5000
print("Q15:", expenses)

# Q16. Double price using *=.

price = 100
price *= 2
print("Q16:", price)

# Q17. Divide amount by 2 using /=.

amount = 10000
amount /= 2
print("Q17:", amount)

# ============================================================

# 🔹 LOGICAL OPERATORS

# ============================================================

# Q18. Check age >= 18 AND city == "Delhi".

age = 20
city = "Delhi"

answer_18 = age >= 18 and city == "Delhi"
print("Q18:", answer_18)

# Q19. Check sales > 50000 OR profit > 10000.

sales = 60000
profit = 5000

answer_19 = sales > 50000 or profit > 10000
print("Q19:", answer_19)

# Q20. Create is_student = True and use not.

is_student = True

answer_20 = not is_student
print("Q20:", answer_20)

# ============================================================

# 🔹 input() + OPERATORS

# ============================================================

# Q21. Take two numbers and add them.

num1 = int(input("Q21 - Enter first number: "))
num2 = int(input("Q21 - Enter second number: "))

print("Q21 Answer:", num1 + num2)

# Q22. Take two numbers and calculate their product.

num1 = int(input("Q22 - Enter first number: "))
num2 = int(input("Q22 - Enter second number: "))

print("Q22 Answer:", num1 * num2)

# Q23. Take sales and expenses and calculate profit.

sales = float(input("Q23 - Enter sales: "))
expenses = float(input("Q23 - Enter expenses: "))

profit = sales - expenses

print("Q23 Answer - Profit:", profit)

# Q24. Take marks and total marks and calculate percentage.

marks = float(input("Q24 - Enter marks: "))
total_marks = float(input("Q24 - Enter total marks: "))

percentage = (marks / total_marks) * 100

print("Q24 Answer - Percentage:", percentage)

# Q25. Take sales and target and check whether target was achieved.

sales = float(input("Q25 - Enter sales: "))
target = float(input("Q25 - Enter target: "))

target_achieved = sales >= target

print("Q25 Answer - Target Achieved:", target_achieved)

# ============================================================

# 📊 DATA ANALYTICS PRACTICE

# ============================================================

# Q26. Product price × quantity = total sales.

price = float(input("Q26 - Enter product price: "))
quantity = int(input("Q26 - Enter quantity: "))

total_sales = price * quantity

print("Q26 Answer - Total Sales:", total_sales)

# Q27. Monthly sales - expenses = profit.

sales = float(input("Q27 - Enter monthly sales: "))
expenses = float(input("Q27 - Enter monthly expenses: "))

profit = sales - expenses

print("Q27 Answer - Profit:", profit)

# Q28. Actual sales - target sales = difference.

actual_sales = float(input("Q28 - Enter actual sales: "))
target_sales = float(input("Q28 - Enter target sales: "))

difference = actual_sales - target_sales

print("Q28 Answer - Difference:", difference)

# Q29. Average of three subject marks.

marks1 = float(input("Q29 - Enter first subject marks: "))
marks2 = float(input("Q29 - Enter second subject marks: "))
marks3 = float(input("Q29 - Enter third subject marks: "))

average = (marks1 + marks2 + marks3) / 3

print("Q29 Answer - Average:", average)

# Q30. Check sales >= 100000 AND profit >= 20000.

sales = float(input("Q30 - Enter sales: "))
profit = float(input("Q30 - Enter profit: "))

good_performance = sales >= 100000 and profit >= 20000

print("Q30 Answer - Good Performance:", good_performance)

# ============================================================

# ⭐ DAY 04 CHALLENGE

# ============================================================

employee_name = input("Enter employee name: ")
salary = float(input("Enter monthly salary: "))
experience = int(input("Enter experience in years: "))

bonus_eligible = salary >= 30000 and experience >= 2

print("\n===== Bonus Eligibility =====")
print("Employee Name:", employee_name)
print("Salary:", salary)
print("Experience:", experience, "years")
print("Bonus Eligibility:", bonus_eligible)
