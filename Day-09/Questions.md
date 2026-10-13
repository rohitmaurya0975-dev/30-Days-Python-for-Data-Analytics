# 🐍 Day 09 — Python Conditional Statements
## 30 Days Python Challenge for Data Analytics

**Topics:** if, if-else, if-elif-else, Comparison Operators, Nested if

---

## 🟢 Beginner Level

### Q01. Positive Number
Create a program that checks whether a number is positive.
If the number is greater than 0, print "Positive Number".

### Q02. Even or Odd
Write a program to check whether a number is even or odd.

### Q03. Pass or Fail
A student passes if marks are 33 or more.
Write a program that prints "Pass" or "Fail".

### Q04. Voting Eligibility
Write a program that checks whether a person is eligible to vote.
Assume the minimum voting age is 18.

### Q05. Compare Two Numbers
Take two numbers and print the greater number.
If both numbers are equal, print "Both are Equal".

---

## 🟡 Intermediate Level

### Q06. Grade Calculator
Create a grade calculator using these rules:

- Marks >= 90: Grade A
- Marks >= 75: Grade B
- Marks >= 60: Grade C
- Marks >= 33: Grade D
- Marks < 33: Fail

### Q07. Largest of Three Numbers
Write a program to find the largest among three numbers.

### Q08. Discount Calculator
A shop gives discounts according to the purchase amount:

- Amount >= 5000: 20% discount
- Amount >= 3000: 10% discount
- Amount >= 1000: 5% discount
- Amount < 1000: No discount

Calculate and print the discount and final amount.

### Q09. Positive, Negative, or Zero
Write a program that checks whether a number is positive,
negative, or zero.

### Q10. Login Check
Assume the correct username is "admin"
and the correct password is "python123".

Check both values and print:
- "Login Successful" if both are correct.
- "Invalid Credentials" otherwise.

---

## 🔴 Nested if Practice

### Q11. Nested if
Check whether a number is positive.
If it is positive, check whether it is even or odd.

### Q12. Employee Bonus
An employee is eligible for a bonus if their performance score
is at least 80.

If eligible:
- Salary >= 50000: Print "Bonus: 10000"
- Salary < 50000: Print "Bonus: 5000"

Otherwise, print "No Bonus".

---

## 📊 Data Analytics Business Questions

### Q13. Sales Performance
Classify sales using these rules:

- Sales >= 100000: "Excellent"
- Sales >= 50000: "Good"
- Sales >= 20000: "Average"
- Sales < 20000: "Low"

### Q14. Profit or Loss
Given revenue and cost, calculate profit or loss.

- Revenue > Cost: Print "Profit"
- Revenue < Cost: Print "Loss"
- Revenue == Cost: Print "No Profit No Loss"

Also calculate the profit or loss amount.

### Q15. Inventory Alert
A product has a certain stock quantity.

- Stock == 0: "Out of Stock"
- Stock <= 10: "Low Stock"
- Stock <= 50: "Stock Available"
- Stock > 50: "High Stock"

Print the correct stock status.

---

## ⭐ Bonus Challenge

### Q16. Electricity Bill Calculator
Calculate the electricity bill using these rates:

- First 100 units: ₹5 per unit
- Next 100 units: ₹7 per unit
- Units above 200: ₹10 per unit

Rules:
- For units <= 100, bill = units * 5
- For units <= 200, bill = 100 * 5 + remaining units * 7
- For units > 200, bill = 100 * 5 + 100 * 7 + remaining units * 10

Print the total bill.

Example:
Input: 250 units
Output: ₹1700

---

## 📌 Instructions

1. Solve the questions using Python conditional statements.
2. Use if, if-else, if-elif-else, and nested if where appropriate.
3. Do not use loops in this day's solutions.
4. Try to solve each question yourself before checking My-Solutions.py.
5. Test your programs with different inputs.