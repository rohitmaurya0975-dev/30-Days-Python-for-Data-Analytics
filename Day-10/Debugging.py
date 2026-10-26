# ==========================================
# DAY 10 - PYTHON FOR LOOP DEBUGGING
# 30 Days Python Challenge for Data Analytics
# ==========================================

print("===== DAY 10: DEBUGGING PRACTICE =====")


# Q1. Find and fix the range error.
# Expected output: 1 to 10

print("\nQ1: Print numbers from 1 to 10")

for i in range(1, 10):
    print(i)


# Q2. Find and fix the indentation error.
# Expected output: 2, 4, 6, 8, 10

print("\nQ2: Print even numbers")

for i in range(2, 11, 2):
 print(i)


# Q3. Find and fix the total calculation error.
# Expected output: 150

print("\nQ3: Calculate total")

numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total = number

print("Total:", total)


# Q4. Find and fix the counting error.
# Expected output: 4

print("\nQ4: Count numbers greater than 10")

numbers = [5, 15, 20, 8, 25, 30]
count = 0

for number in numbers:
    if number > 10:
        count = count + 2

print("Count:", count)


# Q5. Find and fix the condition error.
# Expected output: 20, 40

print("\nQ5: Print numbers greater than 15")

numbers = [10, 20, 15, 40, 5]

for number in numbers:
    if number > 15:
        print(number)


# Q6. Find and fix the multiplication table error.
# Expected output: Table of 5 from 1 to 10

print("\nQ6: Multiplication table of 5")

for i in range(1, 11):
    print("5 x", i, "=", 5 + i)


# Q7. Find and fix the largest-number error.
# Expected output: 90

print("\nQ7: Find the largest number")

numbers = [20, 45, 90, 35, 70]
largest = 0

for number in numbers:
    if number < largest:
        largest = number

print("Largest:", largest)


# Q8. Find and fix the average calculation error.
# Expected output: 20.0

print("\nQ8: Calculate average")

numbers = [10, 20, 30]
total = 0

for number in numbers:
    total = total + number

average = total / 2

print("Average:", average)


# Q9. Find and fix the loop variable error.
# Expected output: 1, 2, 3, 4, 5

print("\nQ9: Print numbers from 1 to 5")

for i in range(1, 6):
    print(number)


# Q10. Find and fix the sales total error.
# Expected output: 15000

print("\nQ10: Calculate total sales")

sales = [2000, 3000, 4000, 6000]
total_sales = 0

for amount in sales:
    total_sales = total_sales + sales

print("Total Sales:", total_sales)


print("\n===== DEBUGGING PRACTICE COMPLETED =====")