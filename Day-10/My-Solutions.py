# ==========================================
# DAY 10 - PYTHON FOR LOOP SOLUTIONS
# 30 Days Python Challenge for Data Analytics
# ==========================================

print("===== DAY 10: MY SOLUTIONS =====")


# Q1. Print numbers from 1 to 10

print("\nQ1: Numbers from 1 to 10")

for i in range(1, 11):
    print(i)


# Q2. Print numbers from 10 to 1

print("\nQ2: Reverse Numbers")

for i in range(10, 0, -1):
    print(i)


# Q3. Print even numbers from 1 to 20

print("\nQ3: Even Numbers")

for i in range(2, 21, 2):
    print(i)


# Q4. Print odd numbers from 1 to 20

print("\nQ4: Odd Numbers")

for i in range(1, 21, 2):
    print(i)


# Q5. Multiplication table of a user-entered number

print("\nQ5: Multiplication Table")

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Q6. Calculate the sum of numbers from 1 to 100

print("\nQ6: Sum from 1 to 100")
total = 0

for i in range(1, 101):
    total = total + i

print("Total:", total)


# Q7. Print all elements of a list

print("\nQ7: Print List Elements")

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# Q8. Calculate the sum of list elements

print("\nQ8: Sum of List Elements")

numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total = total + number

print("Sum:", total)

# Q9. Count even numbers in a list

print("\nQ9: Count Even Numbers")

numbers = [12, 7, 8, 15, 20, 31, 44, 9]
even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count = even_count + 1

print("Even Numbers Count:", even_count)


# Q10. Calculate factorial of a number

print("\nQ10: Factorial")

num = int(input("Enter a non-negative number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1

    for i in range(1, num + 1):
        factorial = factorial * i

    print("Factorial:", factorial)


# Q11. Calculate total sales

print("\nQ11: Total Sales")

sales = [1000, 2500, 1800, 4000, 5000]
total_sales = 0

for amount in sales:
    total_sales = total_sales + amount

print("Total Sales:", total_sales)


# Q12. Print sales greater than or equal to 3000

print("\nQ12: High Sales")

sales = [1000, 2500, 1800, 4000, 5000]

for amount in sales:
    if amount >= 3000:
        print(amount)


# Q13. Count high-sales days

print("\nQ13: Count High Sales Days")

sales = [1000, 3500, 1800, 4500, 5000, 1200]
high_sales_count = 0

for amount in sales:
    if amount >= 3000:
        high_sales_count = high_sales_count + 1

print("High Sales Days:", high_sales_count)


# Q14. Calculate total inventory value

print("\nQ14: Inventory Value")

prices = [500, 1200, 800, 2000, 1500]
total_value = 0

for price in prices:
    total_value = total_value + price

print("Total Inventory Value:", total_value)


# Q15. Classify sales as High, Medium, or Low

print("\nQ15: Sales Classification")

sales = [12000, 25000, 8000, 45000, 18000]

for amount in sales:
    if amount >= 30000:
        category = "High"
    elif amount >= 15000:
        category = "Medium"
    else:
        category = "Low"

    print("Sales:", amount, "| Category:", category)


# Q16. Calculate average sales

print("\nQ16: Average Sales")

sales = [1000, 2000, 3000, 4000, 5000]
total_sales = 0

for amount in sales:
    total_sales = total_sales + amount

average_sales = total_sales / len(sales)

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)


print("\n===== ALL 16 QUESTIONS COMPLETED =====")