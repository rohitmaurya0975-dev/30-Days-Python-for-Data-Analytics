
# ============================================
# 🐍 DAY 13 - PYTHON FUNCTIONS
# DEBUGGING PRACTICE
# ============================================


# Q01 - Missing Function Call

def greet():
    print("Hello Python")

# Correct:
greet()


# Q02 - Missing Parentheses

def welcome():
    print("Welcome to Data Analytics!")

# Wrong: welcome
# Correct:
welcome()


# Q03 - Incorrect Indentation

def student():
    print("Student Name: Rohit")
    print("Course: Data Analytics")

student()


# Q04 - Missing Parameter

def add(a, b):
    return a + b

# Wrong: add(10)
# Correct:
print("Addition:", add(10, 20))


# Q05 - Incorrect Return Statement

def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Multiplication:", result)


# Q06 - Print vs Return

def calculate_sum(a, b):
    return a + b

result = calculate_sum(10, 20)
print("Sum:", result)


# Q07 - Wrong Variable Name

def calculate_profit(revenue, cost):
    return revenue - cost

profit = calculate_profit(15000, 9000)
print("Profit: ₹", profit)


# Q08 - Function Without Return

def calculate_square(number):
    return number * number

square = calculate_square(6)
print("Square:", square)


# Q09 - Division by Zero Protection

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("Division:", divide(20, 5))
print("Division:", divide(20, 0))


# Q10 - Incorrect Calculation

def calculate_average(a, b, c):
    return (a + b + c) / 3

average = calculate_average(60, 70, 80)
print("Average:", average)


# ============================================
# 🎯 DEBUGGING LESSONS
# ============================================

# 1. Always call a function using parentheses.
# 2. Pass the correct number of arguments.
# 3. Maintain proper indentation.
# 4. Use return when you need a result.
# 5. Check variable names carefully.
# 6. Handle division by zero.

# ============================================
# 🎉 DAY 13 DEBUGGING COMPLETED!
# ============================================