# ==========================================
# DAY 10 - PYTHON FOR LOOP CHALLENGE
# 30 Days Python Challenge for Data Analytics
# ==========================================

print("===== DAY 10: FOR LOOP CHALLENGE =====")


# Challenge 1
# Print numbers from 1 to 20 using a for loop.

for i in range(1,21):
    print(i)

# Challenge 2
# Print even numbers from 2 to 50.

for i in range(2,51,2):
    print(i)

# Challenge 3
# Print the multiplication table of 7.

for number in range(1, 11):
    print("7 x", number, "=", 7 * number)


# Challenge 4
# Calculate the sum of numbers from 1 to 50.

total = 0

for number in range(1, 103):
    total = total + number

print("Total:", total)


# Challenge 5
# Find the sum of all numbers in this list.
numbers = [10, 20, 30, 40, 50]


print("\nChallenge 5: List Sum")

numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total = total + number

print("Sum:", total)

# Challenge 6
# Count how many numbers are greater than 25.
numbers = [10, 35, 20, 45, 50, 15, 30]


numbers = [10, 35, 20, 45, 50, 15, 30]
count = 0

for number in numbers:
    if number > 25:
        count = count + 1

print("Count:", count)


# Challenge 7
# Print sales values greater than or equal to 3000.

sales = [1500, 2500, 3000, 2000, 4000]
for amount in sales:
 if amount >=3000:
    print(amount)


# Challenge 8
# Calculate the total sales.

sales = [1500, 2500, 3000, 2000, 4000]
total_sales = 0

for amount in sales:
    total_sales = total_sales + amount

print("Total Sales:", total_sales)

# Challenge 9
# Find the largest number without using max().

numbers = [12, 45, 23, 67, 34, 89, 10]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest Number:", largest)

# Challenge 10
# Calculate the average sales.

sales = [1000, 2000, 3000, 4000, 5000]
total_sales = 0

for amount in sales:
    total_sales = total_sales + amount

average = total_sales / len(sales)

print("Total Sales:", total_sales)
print("Average Sales:", average)


# Bonus Challenge
# Count how many sales are greater than or equal to 3000.
# Also calculate their total.

sales = [1000, 3500, 1800, 4500, 5000, 1200, 4000]
count=0
for i in sales:
  if i>= 3000:
      count=count+1
      print(count)
print("===== CHALLENGES COMPLETED =====")


name ='aryan'
print (name)

agg = 14
print (agg)

name =input("apna name batao")
print (name)

agg =int(input("apna agg likho"))

a=3
b=5
print (a-b)

a 