# 🐍 Day 03 — Input & Type Conversion

## 1. input()

`input()` is used to take information from the user.

```python
name = input("Enter your name: ")
print(name)
2. Important Rule

By default, input() returns a string.

age = input("Enter your age: ")

print(type(age))

Even if the user enters 20, Python treats it as:

<class 'str'>
3. int()

Use int() for whole numbers.

age = int(input("Enter your age: "))
4. float()

Use float() for decimal numbers.

price = float(input("Enter price: "))
5. str()

Use str() to convert a value into text.

age = 20
age_text = str(age)
6. Input + Calculation
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(total)
7. Common Mistake

Wrong:

age = input("Enter age: ")
print(age + 1)

Why?

input() returns a string, while 1 is an integer.

Correct:

age = int(input("Enter age: "))
print(age + 1)
🧠 Easy Memory Trick

input() → User input, normally string

int(input()) → Whole number

float(input()) → Decimal number

str(value) → Text

📊 Data Analytics Connection

Input and type conversion help us handle numeric data correctly before performing calculations.

sales = float(input("Enter sales: "))
expenses = float(input("Enter expenses: "))

profit = sales - expenses

print(profit)
✅ Day 03 Summary

Today I learned:

input()
User input
Input as string
int()
float()
str()
type()
Input with calculations
Basic business calculations
Common type-conversion mistakes
Next Step

Day 04 → Operators







a =("Rohan","Rahul","Sumit","Ramesh","Suresh")

for i in a 
   prin(i)