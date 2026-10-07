# ==========================================
# 30 Days Python Challenge
# Day 03 - Input & Type Conversion
# ==========================================

# Q01
name = input("Enter your name: ")
print(name)


# Q02
age = int(input("Enter your age: "))
print(age)


# Q03
age = int(input("Enter your age: "))
next_year_age = age + 1

print("Next year age:", next_year_age)


# Q04
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2

print("Sum:", total)


# Q05
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 * num2

print("Multiplication:", result)


# Q06
price = float(input("Enter product price: "))

print("Product Price:", price)


# Q07
percentage = float(input("Enter percentage: "))

print("Percentage:", percentage)
print("Data Type:", type(percentage))


# Q08
name = input("Enter your name: ")
city = input("Enter your city: ")

print("My name is", name, "and I live in", city)


# Q09
salary = float(input("Enter salary: "))
bonus = float(input("Enter bonus: "))

total_salary = salary + bonus

print("Total Salary:", total_salary)


# Q10

product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount: "))

total_price = product_price * quantity
final_amount = total_price - discount

print("Total Price:", total_price)
print("Final Amount:", final_amount)