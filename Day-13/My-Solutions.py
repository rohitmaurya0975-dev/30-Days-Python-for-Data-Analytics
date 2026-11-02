
# ============================================
# 🐍 Day 13 - Python Functions
# 30 Days Python Challenge for Data Analytics
# ============================================


# Q01 - Create a Function

def greet():
    print("Hello Python")


greet()


# Q02 - Welcome Message

def welcome():
    print("Welcome to Data Analytics!")


welcome()
welcome()
welcome()


# Q03 - Square of a Number

def square(number):
    print(number * number)


square(5)


# Q04 - Display a Name

def display_name(name):
    print(f"Hello, {name}!")


display_name("Rohit")
display_name("Aman")
display_name("Rahul")


# Q05 - Add Two Numbers

def add(a, b):
    print(a + b)
    print(a-b)
    print(a*b)
    print(a/b)

add(877, 290)


# Q06 - Subtraction


def subtract(a, b):
    return a - b


result = subtract(298, 290)
print("Subtraction:", result)


# Q07 - Multiplication  

def multiply(a, b):
    return a * b


result = multiply(10, 57)
print("Multiplication:", result)


# Q08 - Calculate Profit  

def calculate_profit(revenue, cost):
    return revenue - cost


profit = calculate_profit(15000, 9000)
print("Profit: ₹", profit)


# Q09 - Calculate Total Sales


def calculate_sales(price, quantity):
    return price * quantity


total_sales = calculate_sales(500, 4)
print("Total Sales: ₹", total_sales)


# Q10 - Average of Three Numbers
def calculate_average(a, b, c):
    return (a + b + c) / 3


average = calculate_average(70, 80, 90)
print("Average:", average)


# Q11 - Employee Salary

def calculate_salary(basic_salary, bonus):
    return basic_salary + bonus


total_salary = calculate_salary(30000, 5000)
print("Total Salary: ₹", total_salary)


# Q12 - Discount Calculator

def calculate_discount(price, discount):
    return price - discount


final_price = calculate_discount(1000, 150)
print("Final Price: ₹", final_price)


# Q13 - Sales Performance

def sales_performance(sales):
    return sales[0] + sales[1] + sales[2]


sales = [1000, 2000, 3000]
total = sales_performance(sales)
print("Total Sales: ₹", total)


# Q14 - Difference Between print() and return

def add_using_print(a, b):
    print("Sum using print:", a + b)


def add_using_return(a, b):
    return a + b


add_using_print(10, 20)

result = add_using_return(10, 20)
print("Sum using return:", result)


# Q15 - Mini Business Calculator

def business_calculator(revenue, expenses):
    return revenue - expenses


print("Business Profit 1:", business_calculator(20000, 12000))
print("Business Profit 2:", business_calculator(35000, 20000))
print("Business Profit 3:", business_calculator(50000, 30000))


# BONUS - Order Total Calculator
def calculate_order_total(price, quantity, discount):
    total_price = price * quantity
    final_amount = total_price - discount
    return final_amount


order_total = calculate_order_total(800, 3, 200)
print("Final Amount: ₹", order_total)


# ============================================
# 🎉 Day 13 Solutions Completed!
# ============================================

