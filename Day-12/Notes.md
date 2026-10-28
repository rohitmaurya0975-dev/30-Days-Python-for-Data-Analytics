# 🐍 Day 12 — break, continue and pass

## 📚 Topics Covered

* `break` Statement
* `continue` Statement
* `pass` Statement
* Difference Between break, continue and pass
* Loop Control
* Sales Data Analysis
* Inventory Management
* Python Debugging

---

# 1. The `break` Statement

The `break` statement immediately stops the loop.

### Example

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

### Output

```text
1
2
```

### Explanation

When `i` becomes 3, `break` stops the loop completely.

**Remember:** `break` = Exit the loop.

---

# 2. The `continue` Statement

The `continue` statement skips the current iteration and moves to the next iteration.

### Example

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### Output

```text
1
2
4
5
```

### Explanation

When `i` becomes 3, Python skips `print(i)` for that iteration and continues with the next number.

**Remember:** `continue` = Skip the current iteration.

---

# 3. The `pass` Statement

The `pass` statement does nothing. It is used as a placeholder when a statement is required syntactically but you do not want to perform an action yet.

### Example

```python
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
```

### Output

```text
1
2
3
4
5
```

### Explanation

When `i` becomes 3, `pass` does nothing. The next statement, `print(i)`, still executes.

**Remember:** `pass` = Do nothing.

---

# 4. Difference Between break, continue and pass

| Statement  | Purpose            | Effect                      |
| ---------- | ------------------ | --------------------------- |
| `break`    | Stop the loop      | Exits the loop              |
| `continue` | Skip one iteration | Moves to the next iteration |
| `pass`     | Do nothing         | Continues normal execution  |

### Easy Memory Trick

* 🛑 `break` = Stop
* ⏭️ `continue` = Skip
* ⏸️ `pass` = Placeholder

---

# 5. Using `continue` with Lists

You can use `continue` to skip unwanted values in a list.

### Example: Skip Zero Sales

```python
sales = [1000, 0, 2000, 0, 3000]

for sale in sales:
    if sale == 0:
        continue
    print(sale)
```

### Output

```text
1000
2000
3000
```

### Data Analytics Connection

Real-world datasets may contain zero values that should be excluded from a particular calculation. `continue` can help skip those values when appropriate.

**Important:** Zero is not always invalid data. Whether to exclude it depends on the business problem.

---

# 6. Using `break` to Search for a Value

### Example

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        print("Number found!")
        break
```

### Output

```text
Number found!
```

### Explanation

Once the number 30 is found, there is no need to continue searching.

---

# 7. Inventory Management Example

```python
stock = [10, 8, 5, 2, 0, 7]

for quantity in stock:
    if quantity == 0:
        print("Out of Stock!")
        break

    print("Available Stock:", quantity)
```

### Output

```text
Available Stock: 10
Available Stock: 8
Available Stock: 5
Available Stock: 2
Out of Stock!
```

The loop stops when it encounters zero stock.

---

# 8. Filtering Sales Data

### Problem

Print sales values greater than or equal to ₹1,000.

```python
sales = [500, 1500, 800, 2500, 1200]

for sale in sales:
    if sale < 1000:
        continue

    print(sale)
```

### Output

```text
1500
2500
1200
```

### Explanation

Sales below ₹1,000 are skipped. The remaining values are printed.

---

# 9. Important Rules

1. `break` and `continue` are used inside loops.
2. `break` exits the nearest enclosing loop.
3. `continue` skips the remaining statements in the current iteration.
4. `pass` does not skip an iteration or stop a loop.
5. `pass` is useful when writing a program's structure before implementing its logic.
6. Avoid placing statements after `continue` in the same block if you expect them to execute; they will be skipped.
7. A loop's behavior depends on the position of `break`, `continue`, and `pass`.

---

# 10. Common Mistakes

### Mistake 1: Expecting `pass` to skip a value

```python
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
```

This prints every number, including 3.

To skip 3, use `continue`.

### Mistake 2: Expecting `continue` to stop the loop

`continue` skips only the current iteration. Use `break` when you want to exit the loop.

### Mistake 3: Using `break` outside a loop

`break` cannot be used outside a loop. Python raises a `SyntaxError`.

---

# 11. Day 12 Summary

Today we learned:

* What `break` does
* What `continue` does
* What `pass` does
* Differences between the three statements
* Skipping unwanted values in lists
* Searching for values using loops
* Inventory stock checking
* Filtering sales data
* Applying loop control to business problems
* Common Python mistakes

---

# 🧠 Memory Trick

**BREAK → STOP**

**CONTINUE → SKIP**

**PASS → DO NOTHING**

---

## 🚀 Next Day

### Day 13 — Python Functions

We will learn how to create reusable blocks of code using functions.
