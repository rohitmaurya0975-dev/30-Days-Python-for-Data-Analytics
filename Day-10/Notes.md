# 🐍 Day 10: Python For Loops

## 30 Days Python Challenge for Data Analytics

---

## 📌 1. What Is a For Loop?

A `for` loop is used to repeat a block of code for each item in a sequence.

### Example

```python
for i in range(5):
    print(i)
```

### Output

```text
0
1
2
3
4
```

**Explanation:**

* `for` starts the loop.
* `i` stores the current number.
* `range(5)` generates numbers from 0 to 4.
* `print(i)` prints each number.

**Remember:** `range(5)` does not include 5.

---

## 🔢 2. Understanding the range() Function

The `range()` function generates a sequence of numbers.

### A. range(stop)

```python
for i in range(5):
    print(i)
```

Output: `0, 1, 2, 3, 4`

### B. range(start, stop)

```python
for i in range(1, 6):
    print(i)
```

Output: `1, 2, 3, 4, 5`

### C. range(start, stop, step)

```python
for i in range(2, 11, 2):
    print(i)
```

Output: `2, 4, 6, 8, 10`

### Meaning

| Parameter | Meaning                    |
| --------- | -------------------------- |
| `start`   | Starting number            |
| `stop`    | Ending limit, excluded     |
| `step`    | Difference between numbers |

**Memory Trick:** Start included, stop excluded!

---

## 🔄 3. Printing Numbers in Reverse

To print numbers from 10 to 1:

```python
for i in range(10, 0, -1):
    print(i)
```

**Explanation:**

* `10` is the starting number.
* `0` is the stopping limit and is excluded.
* `-1` decreases the number by one each time.

Output: `10, 9, 8, 7, 6, 5, 4, 3, 2, 1`

---

## 📋 4. Using a For Loop with a List

A `for` loop can process each item in a list.

```python
sales = [1000, 2000, 3000]

for amount in sales:
    print(amount)
```

### Output

```text
1000
2000
3000
```

**Explanation:** The variable `amount` receives one sales value at a time.

---

## ➕ 5. Calculating the Sum of Numbers

To calculate a total, initialize a variable with `0`.

```python
numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total = total + number

print("Total:", total)
```

### Output

```text
Total: 150
```

### How It Works

| Number | Calculation | Total |
| -----: | ----------- | ----: |
|     10 | 0 + 10      |    10 |
|     20 | 10 + 20     |    30 |
|     30 | 30 + 30     |    60 |
|     40 | 60 + 40     |   100 |
|     50 | 100 + 50    |   150 |

**Memory Trick:** For calculating a sum, start with `total = 0`.

---

## 🔢 6. Counting Items Using a Condition

Example: Count sales greater than or equal to ₹3,000.

```python
sales = [1000, 3500, 1800, 4500, 5000]
count = 0

for amount in sales:
    if amount >= 3000:
        count = count + 1

print("High Sales Days:", count)
```

### Output

```text
High Sales Days: 3
```

**Explanation:**

* `count = 0` initializes the counter.
* `if amount >= 3000` checks the condition.
* `count = count + 1` increases the count whenever the condition is true.

**Memory Trick:** For counting, start with `count = 0`.

---

## ✅ 7. Using if Inside a For Loop

Example: Print numbers greater than 25.

```python
numbers = [10, 35, 20, 45, 50, 15, 30]

for number in numbers:
    if number > 25:
        print(number)
```

### Output

```text
35
45
50
30
```

**Explanation:** The loop checks every number, and the `if` condition decides which numbers to print.

---

## ✖️ 8. Multiplication Table Using a For Loop

Example: Print the multiplication table of 5.

```python
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)
```

### Output

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

## 🔍 9. Finding the Largest Number

Find the largest number without using `max()`.

```python
numbers = [12, 45, 23, 67, 34, 89, 10]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest Number:", largest)
```

### Output

```text
Largest Number: 89
```

**Explanation:**

1. Assume the first number is the largest.
2. Compare each number with `largest`.
3. If a bigger number is found, update `largest`.
4. Print the final largest number.

---

## 📊 10. Calculating Average Sales

### Formula

**Average = Total ÷ Number of Values**

```python
sales = [1000, 2000, 3000, 4000, 5000]
total = 0

for amount in sales:
    total = total + amount

average = total / len(sales)

print("Total Sales:", total)
print("Average Sales:", average)
```

### Output

```text
Total Sales: 15000
Average Sales: 3000.0
```

**Explanation:**

* The loop calculates total sales.
* `len(sales)` returns the number of values.
* The total is divided by the number of values to calculate the average.

---

## 💼 11. Real-World Use in Data Analytics

For loops are useful for:

* Calculating total sales.
* Finding average revenue.
* Counting high-sales days.
* Identifying the largest transaction.
* Checking inventory quantities.
* Processing data one item at a time.

### Business Example

```python
sales = [1200, 3500, 1800, 4500, 5000]
total_sales = 0

for amount in sales:
    total_sales = total_sales + amount

print("Total Sales:", total_sales)
```

### Output

```text
Total Sales: 16000
```

---

## ⚠️ 12. Common Mistakes

### Mistake 1: Incorrect range

Incorrect:

```python
for i in range(1, 10):
    print(i)
```

This prints numbers from 1 to 9.

Correct:

```python
for i in range(1, 11):
    print(i)
```

### Mistake 2: Incorrect indentation

Incorrect:

```python
for i in range(5):
print(i)
```

Correct:

```python
for i in range(5):
    print(i)
```

### Mistake 3: Replacing instead of adding

Incorrect:

```python
total = 0

for number in [10, 20, 30]:
    total = number
```

Correct:

```python
total = 0

for number in [10, 20, 30]:
    total = total + number
```

### Mistake 4: Dividing by the wrong number

Incorrect:

```python
average = total / 2
```

Correct:

```python
average = total / len(numbers)
```

Use the number of values in the list to calculate the average.

---

## 🧠 13. Quick Revision Table

| Task                    | Code Pattern             |
| ----------------------- | ------------------------ |
| Print numbers           | `for i in range(1, 11):` |
| Print even numbers      | `range(2, 11, 2)`        |
| Process a list          | `for item in items:`     |
| Calculate a sum         | `total = total + number` |
| Count items             | `count = count + 1`      |
| Check a condition       | `if number >= 3000:`     |
| Find the largest number | `if number > largest:`   |
| Calculate an average    | `total / len(numbers)`   |

---

## 📝 14. Practice Checklist

Before moving to the next topic, make sure you can:

* [ ] Print numbers from 1 to 20.
* [ ] Print even numbers from 2 to 50.
* [ ] Print a multiplication table.
* [ ] Calculate the sum of a list.
* [ ] Count numbers that match a condition.
* [ ] Find the largest number.
* [ ] Calculate average sales.
* [ ] Use `if` inside a `for` loop.
* [ ] Explain how `range()` works.

---

## 🎉 Day 10 Completed!

### Topics Learned

* Python `for` loops
* The `range()` function
* Looping through lists
* Calculating totals
* Counting items
* Conditional checks
* Fin
