# Day 04 — Python Operators 🐍

## 1. What are Operators?

Operators are symbols used to perform operations on values and variables.

Example:

```python
a = 10
b = 5

print(a + b)
```

Output:

```text
15
```

---

# 2. Arithmetic Operators

Arithmetic operators are used for mathematical calculations.

| Operator | Meaning        | Example   | Result |
| -------- | -------------- | --------- | ------ |
| `+`      | Addition       | `10 + 5`  | `15`   |
| `-`      | Subtraction    | `10 - 5`  | `5`    |
| `*`      | Multiplication | `10 * 5`  | `50`   |
| `/`      | Division       | `10 / 5`  | `2.0`  |
| `%`      | Remainder      | `10 % 3`  | `1`    |
| `//`     | Floor Division | `10 // 3` | `3`    |
| `**`     | Power          | `2 ** 3`  | `8`    |

### Memory Trick

```text
+  → Add
-  → Minus
*  → Multiply
/  → Divide
%  → Remainder
// → Floor
** → Power
```

---

# 3. Addition `+`

Used to add values.

```python
a = 20
b = 10

result = a + b

print(result)
```

Output:

```text
30
```

---

# 4. Subtraction `-`

Used to subtract one value from another.

```python
salary = 50000
expenses = 30000

saving = salary - expenses

print(saving)
```

Output:

```text
20000
```

### Data Analytics Example

```text
Revenue - Expenses = Profit
```

---

# 5. Multiplication `*`

Used to multiply values.

```python
price = 500
quantity = 4

total = price * quantity

print(total)
```

Output:

```text
2000
```

### Business Formula

```text
Total Sales = Price × Quantity
```

---

# 6. Division `/`

Used to divide values.

```python
total = 1000
people = 4

share = total / people

print(share)
```

Output:

```text
250.0
```

Important:

Python `/` generally gives a decimal result.

---

# 7. Modulus `%`

The `%` operator gives the remainder.

```python
print(10 % 3)
```

Output:

```text
1
```

Why?

```text
10 ÷ 3

3 × 3 = 9
Remainder = 1
```

### Even / Odd

```python
number = 10

if number % 2 == 0:
    print("Even")
```

If remainder is `0`, the number is even.

---

# 8. Floor Division `//`

Floor division gives the whole-number part of division.

```python
print(10 // 3)
```

Output:

```text
3
```

Normal division:

```python
10 / 3
```

Output:

```text
3.333...
```

Floor division:

```python
10 // 3
```

Output:

```text
3
```

---

# 9. Power Operator `**`

Used to calculate powers.

```python
result = 2 ** 3

print(result)
```

Output:

```text
8
```

Because:

```text
2 × 2 × 2 = 8
```

---

# 10. Comparison Operators

Comparison operators compare two values.

They return:

```text
True
False
```

| Operator | Meaning               |
| -------- | --------------------- |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |
| `==`     | Equal to              |
| `!=`     | Not equal to          |

Example:

```python
salary1 = 50000
salary2 = 40000

print(salary1 > salary2)
```

Output:

```text
True
```

---

# 11. `=` vs `==`

This is VERY important.

### `=`

Used for assignment.

```python
salary = 50000
```

Meaning:

Store `50000` inside `salary`.

### `==`

Used for comparison.

```python
salary == 50000
```

Meaning:

Is salary equal to 50000?

### Remember

```text
=   → Store
==  → Compare
```

---

# 12. Input + Operators

We can take input and perform calculations.

```python
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Total:", total)
```

Flow:

```text
Input
  ↓
Data Type Conversion
  ↓
Operator
  ↓
Calculation
  ↓
Output
```

---

# 13. Discount Calculation

A very useful business formula:

```python
price = 2000
discount = 10

discount_amount = price * discount / 100
final_price = price - discount_amount
```

Formula:

```text
Discount Amount
= Price × Discount% / 100

Final Price
= Price - Discount Amount
```

---

# 14. Profit Calculation

Business analytics often uses:

```python
sales = 50000
expenses = 30000

profit = sales - expenses
```

Formula:

```text
Profit = Sales - Expenses
```

Profit percentage:

```python
profit_percentage = (profit / sales) * 100
```

---

# 15. Operator Precedence

Python follows a specific order while calculating expressions.

Example:

```python
result = 10 + 5 * 2
```

Output:

```text
20
```

Not:

```text
30
```

Because multiplication happens before addition.

### Easy Order

```text
()
**
* / // %
+ -
```

Remember:

```text
Bracket → Power → Multiply/Divide → Add/Subtract
```

---

# 16. Common Mistakes

## Mistake 1: Using `+` instead of `*`

Wrong:

```python
total = price + quantity
```

Correct:

```python
total = price * quantity
```

---

## Mistake 2: Forgetting percentage formula

Wrong:

```python
discount_amount = price - discount
```

Correct:

```python
discount_amount = price * discount / 100
```

---

## Mistake 3: Confusing `=` and `==`

Wrong for comparison:

```python
salary = 50000
```

Correct:

```python
salary == 50000
```

---

## Mistake 4: Forgetting brackets

Wrong:

```python
average = maths + python + sql / 3
```

Correct:

```python
average = (maths + python + sql) / 3
```

---

# 17. What I Learned Today

Today I learned:

* What operators are
* Arithmetic operators
* Addition
* Subtraction
* Multiplication
* Division
* Modulus
* Floor division
* Power operator
* Comparison operators
* `=` vs `==`
* Operator precedence
* Discount calculation
* Profit calculation
* Business calculations using operators
* How operators are useful in Data Analytics

---

# 18. Data Analytics Connection 📊

Operators are used everywhere in Data Analytics.

Examples:

```text
Sales = Price × Quantity

Profit = Sales - Expenses

Discount = Price × Discount% / 100

Average = Total / Number of Values

Growth = (New - Old) / Old × 100
```

So operators are one of the basic building blocks of analytics.

---

# 19. My Day 04 Memory Trick 🧠

Remember this:

```text
+  → Add
-  → Remove
*  → Multiply
/  → Divide
%  → Remainder
>  → Greater
<  → Smaller
== → Same?
!= → Different?
```

And remember:

```text
=  → Store
== → Compare
```

---

# 20. Day 04 Summary

```text
Day 04
   ↓
Python Operators
   ↓
Arithmetic
   ↓
Comparison
   ↓
Calculations
   ↓
Business Problems
   ↓
Data Analytics Thinking
```

### Next Day 🚀

**Day 05 — Strings**

We will learn:

* What is a String?
* String indexing
* String slicing
* String methods
* Uppercase / lowercase
* Finding text
* Replacing text
* Practical text-data examples
