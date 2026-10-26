
# =====================================================
# Day 11: Python While Loop Debugging
# 30 Days Python for Data Analytics
# =====================================================

# Instructions:
# Har question mein error find karo aur correct karo.
# Har snippet ko alag se run karo.
# Kuch questions mein logical error hai, syntax error nahi.


# Q1. Find the Error
# Expected output: Numbers from 1 to 5

i = 1

while i <= 5:
    print(i)


# Q2. Find the Error
# Expected output: Numbers from 5 to 1

i = 5

while i >= 1:
    print(i)
    i += 1


# Q3. Find the Error
# Expected output: Sum of numbers from 1 to 10 = 55

i = 1
total = 0

while i <= 10:
    total = i
    i += 1

print("Total:", total)


# Q4. Find the Error
# Expected output: Print Python 5 times

count = 1

while count < 5:
    print("Python")
    count += 1


# Q5. Find the Error
# Expected output: Add five items to the list

items = []
count = 0

while count < 5:
    item = input("Enter an item: ")
    items.append(items)
    count += 1

print("Final List:", items)


# Q6. Find the Error
# Expected output: Count positive numbers

numbers = [10, -5, 20, -2, 15]

i = 0
count = 0

while i < len(numbers):
    if numbers[i] > 0:
        count += 1

print("Positive Numbers:", count)


# Q7. Find the Error
# Expected output: Total sales = 13000

sales = [1500, 2500, 3000, 2000, 4000]

i = 0
total = 0

while i < len(sales):
    total += sales[i]
    i += 1

print("Total Sales:", total)


# Q8. Find the Error
# Expected output: Count products with zero stock

stock = [10, 0, 25, 0, 15]

i = 0
count = 0

while i < len(stock):
    if stock[i] == 0:
        count += 1
    i += 1

print("Out-of-Stock Products:", count)


# Q9. Find the Error
# Expected output: Keep asking until the correct password is entered

correct_password = "python123"
password = ""

while password == correct_password:
    password = input("Enter password: ")

print("Login successful!")


# Q10. Find the Error
# Expected output:
# 1. Add Item
# 2. View List
# 3. Exit

items = []

while True:
    print("\n1. Add Item")
    print("2. View List")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        items.append(item)

    elif choice == "2":
        print("Your List:", items)

    elif choice == "3":
        print("Exiting...")
        continue

    else:
        print("Invalid choice!")


# =====================================================
# End of Day 11 Debugging Practice
# =====================================================

