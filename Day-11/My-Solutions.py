
# =====================================================
# Day 11: Python While Loops - My Solutions
# 30 Days Python for Data Analytics Challenge
# =====================================================


# Q1. Print numbers from 1 to 10
print("\nQ1. Numbers from 1 to 10")

i = 1

while i <= 10:
    print(i)
    i += 1


# Q2. Reverse counting from 10 to 1
print("\nQ2. Reverse Counting")

i = 10

while i >= 1:
    print(i)
    i -= 1


# Q3. Print even numbers from 2 to 20
print("\nQ3. Even Numbers")

i = 2

while i <= 20:
    print(i)
    i += 2


# Q4. Print odd numbers from 1 to 19
print("\nQ4. Odd Numbers")

i = 1

while i <= 19:
    print(i)
    i += 2


# Q5. Print Python five times
print("\nQ5. Print Python Five Times")

i = 1

while i <= 5:
    print("Python")
    i += 1


# Q6. Sum of numbers from 1 to 100
print("\nQ6. Sum from 1 to 100")

i = 1
total = 0

while i <= 100:
    total += i
    i += 1

print("Total:", total)


# Q7. Sum of even numbers from 1 to 20
print("\nQ7. Sum of Even Numbers")

i = 2
total = 0

while i <= 20:
    total += i
    i += 2

print("Total:", total)


# Q8. Multiplication table
print("\nQ8. Multiplication Table")

number = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1


# Q9. Factorial of a number
print("\nQ9. Factorial")

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    i = 1
    factorial = 1

    while i <= number:
        factorial *= i
        i += 1

    print("Factorial:", factorial)


# Q10. Sum of digits
print("\nQ10. Sum of Digits")

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
else:
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number //= 10

    print("Sum of digits:", total)


# Q11. Create an empty list and input five items

print("\nQ11. Create a List")

my_list = []
count = 0

while count < 5:
    item = input("Enter an item: ")
    my_list.append(item)
    count += 1

print("Final List:", my_list)


# Q12. Input five numbers and calculate their total
print("\nQ12. Total of Five Numbers")

numbers = []
count = 0
total = 0

while count < 5:
    number = int(input("Enter a number: "))
    numbers.append(number)
    total += number
    count += 1

print("Numbers:", numbers)
print("Total:", total)


# Q13. Count positive numbers

print("\nQ13. Count Positive Numbers")

numbers = [10, -5, 20, -2, 0, 15, -8]

i = 0
count = 0

while i < len(numbers):
    if numbers[i] > 0:
        count += 1

    i += 1

print("Positive Numbers:", count)


# Q14. Calculate total sales

print("\nQ14. Total Sales")

sales = [1500, 2500, 3000, 2000, 4000]

i = 0
total = 0

while i < len(sales):
    total += sales[i]
    i += 1

print("Total Sales:", total)


# Q15. Count high-sales days

print("\nQ15. Count High Sales")

sales = [1000, 3500, 1800, 4500, 5000, 1200]

i = 0
count = 0

while i < len(sales):
    if sales[i] >= 3000:
        count += 1

    i += 1

print("High-Sales Days:", count)


# Q16. Password validation\

print("\nQ16. Password Validation")

correct_password = "python123"
password = ""

while password != correct_password:
    password = input("Enter password: ")

    if password != correct_password:
        print("Incorrect password. Try again!")

print("Login successful!")


# Q17. Number guessing

print("\nQ17. Number Guessing Game")

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))

    if guess != secret_number:
        print("Wrong guess. Try again!")

print("Correct! You guessed the number.")


# Q18. Count out-of-stock products

print("\nQ18. Out-of-Stock Products")

stock = [10, 0, 25, 3, 0, 15, 2]

i = 0
count = 0

while i < len(stock):
    if stock[i] == 0:
        count += 1

    i += 1

print("Out-of-Stock Products:", count)


# Q19. Count low-stock products
print("\nQ19. Low-Stock Products")

stock = [10, 0, 25, 3, 0, 15, 2]

i = 0
count = 0

while i < len(stock):
    if stock[i] < 5:
        count += 1

    i += 1

print("Low-Stock Products:", count)


# Q20. Sales Performance Analyzer

print("\nQ20. Sales Performance Analyzer")

sales = [1200, 3500, 1800, 4500, 2500, 5000, 4000]

i = 0
total = 0
high_sales_count = 0

while i < len(sales):
    total += sales[i]

    if sales[i] >= 3000:
        high_sales_count += 1

    i += 1

average = total / len(sales)

print("Total Sales:", total)
print("Average Sales:", round(average, 2))
print("High-Sales Days:", high_sales_count)


# =====================================================
# BONUS 1. First 10 Fibonacci numbers
# =====================================================

print("\nBonus 1. Fibonacci Series")

a = 0
b = 1
count = 0

while count < 10:
    print(a)

    next_number = a + b
    a = b
    b = next_number

    count += 1


# =====================================================
# BONUS 2. Reverse a number
# =====================================================

print("\nBonus 2. Reverse a Number")

number = int(input("Enter a positive integer: "))

if number < 0:
    print("Please enter a positive integer.")
else:
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10

    print("Reversed Number:", reverse)


# =====================================================
# BONUS 3. Menu-driven list program
# =====================================================

print("\nBonus 3. Menu-Driven List")

items = []

while True:
    print("\n===== MENU =====")
    print("1. Add Item")
    print("2. View List")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter an item to add: ")
        items.append(item)
        print("Item added successfully!")

    elif choice == "2":
        print("Your List:", items)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")


# =====================================================
# END OF DAY 11 SOLUTIONS
# =====================================================
