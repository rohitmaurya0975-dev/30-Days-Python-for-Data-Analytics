
# ==================================================
# Day 12 - My Solutions
# Topic: break, continue and pass
# 30 Days Python Challenge for Data Analytics
# ==================================================


# Q1. Print numbers from 1 to 10.
# Stop when the number becomes 5.

print("Q1: Break Statement")

for i in range(1, 11):
    if i == 5:
        break
    print(i)


# Q2. Print numbers from 1 to 10, but skip 5.

print("\nQ2: Continue Statement")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# Q3. Use pass when the number is 3.

print("\nQ3: Pass Statement")

for i in range(1, 6):
    if i == 3:
        pass
    print(i)


# Q4. Print numbers from 1 to 20, skipping even numbers.

print("\nQ4: Skip Even Numbers")

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)


# Q5. Print numbers from 1 to 15.
# Stop when the number becomes 8.

print("\nQ5: Stop at 8")

for i in range(1, 16):
    if i == 8:
        break
    print(i)


# Q6. Skip zero-sales values.

print("\nQ6: Skip Zero Sales")

sales = [1000, 0, 2000, 0, 3000, 4000]

for sale in sales:
    if sale == 0:
        continue
    print(sale)


# Q7. Find the first number divisible by 7.

print("\nQ7: First Multiple of 7")

for number in range(1, 51):
    if number % 7 == 0:
        print("First multiple of 7:", number)
        break


# Q8. Print only positive numbers.

print("\nQ8: Skip Negative Numbers")

numbers = [10, -5, 20, -2, 30, -8, 40]

for number in numbers:
    if number < 0:
        continue
    print(number)


# Q9. Stop inventory checking when stock becomes zero.

print("\nQ9: Inventory Stock Check")

stock = [10, 8, 5, 2, 0, 7, 9]

for quantity in stock:
    if quantity == 0:
        print("Out of Stock")
        break

    print("Available Stock:", quantity)


# Q10. Skip sales below 1000.

print("\nQ10: Filter Sales")

sales = [500, 1500, 800, 2500, 1200, 700]

for sale in sales:
    if sale < 1000:
        continue
    print(sale)


# Q11. Search for number 48.

print("\nQ11: Search for a Number")

numbers = [12, 25, 37, 48, 59, 60]

for number in numbers:
    if number == 48:
        print("Number found:", number)
        break

    print("Checking:", number)


# Q12. Allow up to 5 password attempts.

print("\nQ12: Password Attempts")

correct_password = "python123"

for attempt in range(1, 6):
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect password")

else:
    print("Maximum attempts reached!")


# Q13. Print the table of 5, skipping multiplication by 5.

print("\nQ13: Multiplication Table")

for i in range(1, 11):
    if i == 5:
        continue

    print(f"5 x {i} = {5 * i}")


# Q14. Difference between break, continue and pass.

print("\nQ14: Difference Between Statements")

print("break: Exits the loop completely.")
print("continue: Skips the current iteration.")
print("pass: Does nothing; acts as a placeholder.")


# Example of break
print("\nBreak Example")

for i in range(1, 6):
    if i == 3:
        break
    print(i)


# Example of continue
print("\nContinue Example")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# Example of pass
print("\nPass Example")

for i in range(1, 6):
    if i == 3:
        pass
    print(i)


# Q15. Business Problem - Sales Analysis.

print("\nQ15: Sales Analysis")

sales = [1200, 0, 2500, 800, 3500, 0, 4200]

total = 0

for sale in sales:
    if sale == 0:
        continue

    if sale < 1000:
        continue

    print("Valid Sale:", sale)
    total += sale

print("Total Valid Sales:", total)


# Bonus Challenge
# Find the first number divisible by both 3 and 7.

print("\nBonus: Number Search")

for number in range(1, 101):
    if number % 3 == 0 and number % 7 == 0:
        print("First number divisible by both 3 and 7:", number)
        break

