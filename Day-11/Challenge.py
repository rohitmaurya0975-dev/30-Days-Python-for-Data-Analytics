
# =====================================================
# Day 11: While Loop Challenge Solutions
# 30 Days Python for Data Analytics
# =====================================================


# Challenge 1: Print numbers from 1 to 20

print("\nChallenge 1: Counting")

i = 1

while i <= 20:
    print(i)
    i += 1


# Challenge 2: Reverse counting from 20 to 1
print("\nChallenge 2: Reverse Counting")

i = 20

while i >= 1:
    print(i)
    i -= 1


# Challenge 3: Empty list and input five 


print("\nChallenge 3: Empty List")

items = []
i = 0

while i < 5:
    item = input("Enter an item: ")
    items.append(item)
    i += 1

print("Final List:", items)


# Challenge 4: Sum of numbers from 1 to 50

print("\nChallenge 4: Sum of Numbers")

i = 1
total = 0

while i <= 50:
    total += i
    i += 1

print("Total:", total)


# Challenge 5: Multiplication table

print("\nChallenge 5: Multiplication Table")

number = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1


# Challenge 6: Even numbers from 1 to 50

print("\nChallenge 6: Even Numbers")

i = 2

while i <= 50:
    print(i)
    i += 2


# Challenge 7: Input five numbers and calculate total

print("\nChallenge 7: Total of Five Numbers")

numbers = []
i = 0
total = 0

while i < 5:
    number = int(input("Enter a number: "))
    numbers.append(number)
    total += number
    i += 1

print("Numbers:", numbers)
print("Total:", total)


# Challenge 8: Find the largest number

print("\nChallenge 8: Largest Number")

numbers = [12, 45, 23, 67, 34, 89, 10]

i = 1
largest = numbers[0]

while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]

    i += 1

print("Largest Number:", largest)


# Challenge 9: Count high-sales days

print("\nChallenge 9: High Sales")

sales = [1200, 3500, 1800, 4500, 5000, 1200, 4000]

i = 0
count = 0

while i < len(sales):
    if sales[i] >= 3000:
        count += 1

    i += 1

print("High-Sales Days:", count)


# Challenge 10: Count out-of-stock products

print("\nChallenge 10: Inventory Alert")

stock = [10, 0, 25, 3, 0, 15, 2]

i = 0
count = 0

while i < len(stock):
    if stock[i] == 0:
        count += 1

    i += 1

print("Out-of-Stock Products:", count)


# Challenge 11: Password validation

print("\nChallenge 11: Password Validation")

correct_password = "python123"
password = ""

while password != correct_password:
    password = input("Enter password: ")

    if password != correct_password:
        print("Incorrect password. Try again!")

print("Login successful!")


# Challenge 12: Number guessing game

print("\nChallenge 12: Number Guessing")

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))

    if guess != secret_number:
        print("Wrong guess. Try again!")

print("Correct! You guessed the number.")


# Challenge 13: Count products with stock below 5

print("\nChallenge 13: Low Stock")

stock = [10, 0, 25, 3, 0, 15, 2]

i = 0
count = 0

while i < len(stock):
    if stock[i] < 5:
        count += 1

    i += 1

print("Low-Stock Products:", count)


# Challenge 14: Sales total and average

print("\nChallenge 14: Sales Analyzer")

sales = [1500, 2500, 3000, 2000, 4000]

i = 0
total = 0

while i < len(sales):
    total += sales[i]
    i += 1

average = total / len(sales)

print("Total Sales:", total)
print("Average Sales:", average)


# Challenge 15: Menu-driven list

print("\nChallenge 15: Menu-Driven List")

items = []

while True:
    print("\n===== MENU =====")
    print("1. Add Item")
    print("2. View List")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        items.append(item)
        print("Item added successfully!")

    elif choice == "2":
        print("Current List:", items)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")


# =====================================================
# BONUS: Keep accepting numbers until 0 is entered
# =====================================================

print("\nBonus: Sum of User-Entered Numbers")

total = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    total += number

print("Final Total:", total)


# =====================================================
# End of Day 11 Challenge Solutions
# =====================================================

