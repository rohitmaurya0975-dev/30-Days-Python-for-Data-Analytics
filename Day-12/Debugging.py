
# ==================================================
# Day 12 - Python Debugging Practice
# Topics: break, continue and pass
# 30 Days Python Challenge for Data Analytics
# ==================================================


# Q1. Find and fix the error.
# Expected: Print numbers 1 and 2, then stop.

print("Q1: Fix the break condition")

for i in range(1, 6):
    if i == 3:
        print(i)
        break
    print(i)


# Q2. Find and fix the error.
# Expected: Print 1, 2, 4, 5.

print("\nQ2: Fix the continue condition")

for i in range(1, 6):
    if i == 3:
        continue
        print(i)
    else:
        print(i)


# Q3. Find and fix the error.
# Expected: Print all numbers from 1 to 5.
# Use pass when i is 3.

print("\nQ3: Understand pass")

for i in range(1, 6):
    if i == 3:
        pass
    print(i)


# Q4. Find and fix the error.
# Expected: Print only non-zero sales.

print("\nQ4: Skip Zero Sales")

sales = [1000, 0, 2000, 0, 3000]

for sale in sales:
    if sale == 0:
        continue
    print(sale)


# Q5. Find and fix the error.
# Expected: Stop when stock becomes zero.

print("\nQ5: Inventory Check")

stock = [10, 8, 5, 0, 7]

for quantity in stock:
    if quantity == 0:
        print("Out of Stock!")
        break
    print("Available Stock:", quantity)


# Q6. Find and fix the error.
# Expected: Print only odd numbers from 1 to 10.

print("\nQ6: Print Odd Numbers")

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


# Q7. Find and fix the error.
# Expected: Find the first multiple of 7.

print("\nQ7: Find Multiple of 7")

for number in range(1, 51):
    if number % 7 == 0:
        print("Found:", number)
        break


# Q8. Find and fix the error.
# Expected: Calculate total of non-zero sales.

print("\nQ8: Calculate Sales Total")

sales = [1000, 0, 2000, 3000, 0]

total = 0

for sale in sales:
    if sale == 0:
        continue
    total += sale

print("Total Sales:", total)


# Q9. Find and fix the error.
# Expected: Stop searching when 30 is found.

print("\nQ9: Search for 30")

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        print("Number found:", number)
        break
    print("Checking:", number)


# Q10. Find and fix the error.
# Expected: Skip sales below 1000 and print the rest.

print("\nQ10: Filter Sales")

sales = [500, 1500, 800, 2500, 1200]

for sale in sales:
    if sale < 1000:
        continue
    print("Valid Sale:", sale)


# ==================================================
# Debugging Reminder
# ==================================================
# break    -> Exits the loop.
# continue -> Skips the current iteration.
# pass     -> Does nothing.
#
# Tip: Run each question separately while debugging.

