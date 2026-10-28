
# ==================================================
# Day 12 - Challenge Solutions
# Topics: break, continue and pass
# 30 Days Python Challenge for Data Analytics
# ==================================================


# Challenge 1: Stop when the number becomes 12

print("Challenge 1: Stop at 12")

for i in range(1, 21):
    if i == 12:
        break
    print(i)


# Challenge 2: Skip numbers divisible by 3

print("\nChallenge 2: Skip Multiples of 3")

for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)


# Challenge 3: Print only positive numbers

print("\nChallenge 3: Positive Numbers")

numbers = [10, -5, 0, 25, -8, 40, 0, 15]

for number in numbers:
    if number <= 0:
        continue
    print(number)


# Challenge 4: Find the first number divisible by 5 and 7

print("\nChallenge 4: Find the Number")

for number in range(1, 101):
    if number % 5 == 0 and number % 7 == 0:
        print("Number found:", number)
        break


# Challenge 5: Print sales >= 2000

print("\nChallenge 5: Sales Filter")

sales = [1200, 2500, 800, 3500, 1800, 4200, 900]

for sale in sales:
    if sale < 2000:
        continue
    print("Valid Sale:", sale)


# Challenge 6: Stop when stock becomes zero

print("\nChallenge 6: Inventory Check")

stock = [25, 18, 10, 5, 0, 12, 8]

for quantity in stock:
    if quantity == 0:
        print("Out of Stock!")
        break
    print("Available Stock:", quantity)


# Challenge 7: Use pass when the number is 5

print("\nChallenge 7: Use pass")

for i in range(1, 11):
    if i == 5:
        pass
    print(i)


# Challenge 8: Find the first negative number

print("\nChallenge 8: Find Negative Number")

numbers = [10, 20, 30, -5, 40, -8]

for number in numbers:
    if number < 0:
        print("First negative number:", number)
        break
    print("Checking:", number)


# Challenge 9: Print non-zero values and calculate total

print("\nChallenge 9: Non-Zero Total")

values = [100, 0, 250, 0, 400, 150, 0, 300]

total = 0

for value in values:
    if value == 0:
        continue

    print(value)
    total += value

print("Total:", total)


# Challenge 10: Search for employee ID 104

print("\nChallenge 10: Employee Search")

employee_ids = [101, 102, 103, 104, 105, 106]

for employee_id in employee_ids:
    if employee_id == 104:
        print("Employee ID found:", employee_id)
        break
    print("Checking ID:", employee_id)


# Bonus Challenge:
# Skip even numbers and stop at the first multiple of 7

print("\nBonus Challenge")

for number in range(1, 51):
    if number % 7 == 0:
        print("Stopped at:", number)
        break

    if number % 2 == 0:
        continue

    print(number)