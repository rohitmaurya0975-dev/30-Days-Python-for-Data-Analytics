# 🐍 DAY 09 — PYTHON CONDITIONAL STATEMENTS
## 30 Days Python Challenge for Data Analytics

---

## 📚 1. What Are Conditional Statements?

Conditional statements help a program make decisions based on conditions.

Real-life example:
- If marks are 33 or more → Pass
- Otherwise → Fail

Python conditional statements:
1. if
2. if-else
3. if-elif-else
4. Nested if

---

## 📌 2. The if Statement

The if statement executes code when a condition is True.

Example:

    marks = 75

    if marks >= 33:
        print("Pass")

Output:

    Pass

Important:
- Write a condition after if.
- Use a colon (:) after the condition.
- Indent the code inside the if block.

---

## 📌 3. The if-else Statement

The if-else statement selects between two alternatives.

Example:

    marks = 25

    if marks >= 33:
        print("Pass")
    else:
        print("Fail")

Output:

    Fail

Memory Trick:
- if = Agar
- else = Nahi toh

---

## 📌 4. The if-elif-else Statement

Use elif when you need to check multiple conditions.

Example:

    marks = 85

    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 33:
        print("Grade D")
    else:
        print("Fail")

Output:

    Grade B

Important:
Python checks conditions from top to bottom.
The first True condition's block executes.
The remaining conditions are skipped.

Tip:
When classifying ranges, check higher thresholds first.

---

## 📌 5. Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| == | Equal to | a == b |
| != | Not equal to | a != b |
| > | Greater than | a > b |
| < | Less than | a < b |
| >= | Greater than or equal to | a >= b |
| <= | Less than or equal to | a <= b |

Important Difference:

    a = 10

The = operator assigns a value.

    a == 10

The == operator compares values.

---

## 📌 6. Logical Operators

Logical operators combine or reverse conditions.

### AND

Both conditions must be True.

    age = 20
    has_id = True

    if age >= 18 and has_id:
        print("Entry Allowed")

### OR

At least one condition must be True.

    day = "Sunday"

    if day == "Sunday" or day == "Saturday":
        print("Weekend")

### NOT

Reverses a Boolean condition.

    is_raining = False

    if not is_raining:
        print("No Rain")

---

## 📌 7. Nested if Statement

A nested if is an if statement inside another if statement.

Example:

    number = 8

    if number > 0:
        if number % 2 == 0:
            print("Positive Even Number")
        else:
            print("Positive Odd Number")
    else:
        print("Number is not Positive")

Output:

    Positive Even Number

Use nested if when a second decision depends on the first decision.

---

## 📌 8. Checking Positive, Negative, or Zero

Example:

    number = -5

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

Remember:
- Greater than zero → Positive
- Less than zero → Negative
- Equal to zero → Zero

---

## 📌 9. Checking Even or Odd

The modulus operator (%) returns the remainder.

Example:

    number = 8

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

Memory Trick:
- Remainder 0 after division by 2 → Even
- Otherwise → Odd

---

## 📌 10. Input Validation

Always validate data when the program requires valid ranges.

Example:

    marks = float(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid Marks")
    elif marks >= 33:
        print("Pass")
    else:
        print("Fail")

Here, or checks whether either invalid condition is True.

Note:
This example checks the numerical range. It does not handle non-numeric input.

---

## 📌 11. Important Business Formulas

### Discount

    discount = amount * discount_rate

### Final Amount

    final_amount = amount - discount

### Profit

    profit = revenue - cost

### Loss

    loss = cost - revenue

### Sales Target Achievement

    achievement = (sales / target) * 100

Important:
Check that target is greater than zero before dividing.

---

## 📊 12. Conditional Statements in Data Analytics

Conditional statements help analysts:

- Classify sales performance
- Calculate student grades
- Identify profit or loss
- Create inventory alerts
- Check sales targets
- Categorize customers
- Apply business rules to data

Example:

    sales = 75000

    if sales >= 100000:
        print("Excellent")
    elif sales >= 50000:
        print("Good")
    elif sales >= 20000:
        print("Average")
    else:
        print("Low")

Output:

    Good

---

## ⚠️ 13. Common Mistakes

### Mistake 1: Missing Colon

Incorrect:

    if marks >= 33
        print("Pass")

Correct:

    if marks >= 33:
        print("Pass")

### Mistake 2: Using = Instead of ==

Incorrect:

    if number % 2 = 0:
        print("Even")

Correct:

    if number % 2 == 0:
        print("Even")

### Mistake 3: Incorrect Indentation

Incorrect:

    if marks >= 33:
    print("Pass")

Correct:

    if marks >= 33:
        print("Pass")

### Mistake 4: Incorrect Condition Order

Incorrect:

    if marks >= 33:
        print("Pass")
    elif marks >= 90:
        print("Excellent")

Why?
A score of 95 already satisfies marks >= 33, so Python never reaches the second condition.

Correct:

    if marks >= 90:
        print("Excellent")
    elif marks >= 33:
        print("Pass")
    else:
        print("Fail")

---

## 🧠 14. Quick Revision

| Statement | Purpose |
|-----------|---------|
| if | Check a condition |
| else | Handle the alternative |
| elif | Check another condition |
| Nested if | Check a condition inside another |
| == | Compare equality |
| and | Both conditions must be True |
| or | At least one condition must be True |
| not | Reverse a Boolean condition |
| % | Calculate the remainder |

Memory Trick:

if → Agar
elif → Warna agar
else → Warna

---

## 🎯 15. Day 09 Checklist

- [ ] Understand if statements
- [ ] Understand if-else statements
- [ ] Understand if-elif-else
- [ ] Practice comparison operators
- [ ] Practice logical operators
- [ ] Understand nested if
- [ ] Solve Challenge.py questions
- [ ] Check Challenge-Solutions.py
- [ ] Complete Debugging.py
- [ ] Complete Business-Problem.py
- [ ] Upload Day 09 files to GitHub

---

## 🚀 Next Day Preview

Day 10 — Python for Loops

Topics:
- What is a loop?
- for loop
- range()
- Iterating through sequences
- Practical exercises

Remember:
Practice consistently and understand the logic
instead of memorizing code.

END OF DAY 09 NOTES