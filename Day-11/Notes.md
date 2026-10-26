````markdown
# 🐍 Day 11 — Python While Loops

## 30 Days Python for Data Analytics Challenge

---

## 1. What Is a While Loop?

A `while` loop repeatedly executes a block of code as long as its condition is `True`.

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
````

### Output

```text
1
2
3
4
5
```

---

## 2. While Loop Syntax

```python
while condition:
    # Code to execute
    # Update the variable when needed
```

Important points:

* The condition is checked before each iteration.
* If the condition is `True`, the loop executes.
* If the condition is `False`, the loop stops.
* Indentation is required.
* Update the loop variable when needed to avoid an infinite loop.

---

## 3. Counter Variable

A counter tracks how many times a loop runs or how far a sequence has progressed.

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

### Increment

```python
i += 1
```

Equivalent to:

```python
i = i + 1
```

### Decrement

```python
i -= 1
```

Equivalent to:

```python
i = i - 1
```

---

## 4. Reverse Counting

```python
i = 10

while i >= 1:
    print(i)
    i -= 1
```

Output:

```text
10
9
8
7
6
5
4
3
2
1
```

Remember to decrease the counter when counting backwards.

---

## 5. Even and Odd Numbers

### Even Numbers from 2 to 20

```python
i = 2

while i <= 20:
    print(i)
    i += 2
```

### Odd Numbers from 1 to 19

```python
i = 1

while i <= 19:
    print(i)
    i += 2
```

---

## 6. Calculate the Sum of Numbers

To calculate the sum from 1 to 10:

```python
i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Total:", total)
```

Output:

```text
Total: 55
```

### Important Concepts

* `total = 0` initializes the accumulator.
* `total += i` adds the current number.
* `i += 1` moves to the next number.

---

## 7. Multiplication Table

```python
number = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1
```

`input()` returns text, so `int()` converts the entered value to an integer.

---

## 8. Lists with While Loops

A `while` loop can process list elements using their indexes.

```python
sales = [1000, 2000, 3000, 4000]

i = 0
total = 0

while i < len(sales):
    total += sales[i]
    i += 1

print("Total Sales:", total)
```

Output:

```text
Total Sales: 10000
```

### Important Concepts

* List indexing starts at `0`.
* `len(sales)` returns the number of elements.
* `sales[i]` accesses the current element.
* Increase `i` to move to the next element.

---

## 9. Creating an Empty List with User Input

```python
items = []
count = 0

while count < 5:
    item = input("Enter an item: ")
    items.append(item)
    count += 1

print("Final List:", items)
```

### Explanation

* `items = []` creates an empty list.
* `input()` asks the user for an item.
* `append()` adds the item to the list.
* The loop asks for five items.

---

## 10. Sum of User-Entered Numbers

```python
total = 0
count = 0

while count < 5:
    number = int(input("Enter a number: "))
    total += number
    count += 1

print("Total:", total)
```

This program accepts five numbers and calculates their sum.

---

## 11. Factorial Using a While Loop

The factorial of a non-negative integer is the product of all positive integers up to that number.

Example:

`5! = 5 × 4 × 3 × 2 × 1 = 120`

```python
number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    i = 1
    factorial = 1

    while i <= number:
        factorial *= i
        i += 1

    print("Factorial:", factorial)
```

The factorial of `0` is `1`.

---

## 12. Sum of Digits

Example: `1234 → 1 + 2 + 3 + 4 = 10`

```python
number = int(input("Enter a non-negative integer: "))
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print("Sum of digits:", total)
```

### Important Operators

* `%` returns the remainder.
* `//` performs integer division.

For example:

```python
1234 % 10   # 4
1234 // 10  # 123
```

---

## 13. Password Validation

```python
correct_password = "python123"
password = ""

while password != correct_password:
    password = input("Enter password: ")

    if password != correct_password:
        print("Incorrect password. Try again!")

print("Login successful!")
```

The loop continues until the entered password matches the expected password.

Note: This is a learning example, not a secure authentication system.

---

## 14. The break Statement

`break` immediately terminates the nearest enclosing loop.

```python
i = 1

while i <= 10:
    if i == 5:
        break

    print(i)
    i += 1
```

Output:

```text
1
2
3
4
```

---

## 15. The continue Statement

`continue` skips the remaining statements in the current iteration and moves to the next iteration.

```python
i = 0

while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

---

## 16. Menu-Driven Program

A menu-driven program repeatedly displays options until the user chooses to exit.

```python
items = []

while True:
    print("\n1. Add Item")
    print("2. View List")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        items.append(item)
        print("Item added!")

    elif choice == "2":
        print("Your List:", items)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
```

### How It Works

* `while True` keeps the menu running.
* Option `1` adds an item.
* Option `2` displays the current list.
* Option `3` exits through `break`.
* Invalid choices display an error message.

---

## 17. Infinite Loops

An infinite loop continues indefinitely because its stopping condition never becomes `False`.

Example:

```python
i = 1

while i <= 5:
    print(i)
```

The counter is never updated, so `i` remains `1`.

### Correct Version

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Always check the loop condition and update logic carefully.

---

## 18. While Loop in Data Analytics

While loops can be used for:

* Processing sales records
* Calculating total revenue
* Counting high-performing sales days
* Checking inventory levels
* Identifying products with zero stock
* Calculating average sales
* Processing values in a list

### Example: Sales Analyzer

```python
sales = [1200, 3500, 1800, 4500, 2500, 5000, 4000]

i = 0
total_sales = 0
high_sales_days = 0

while i < len(sales):
    total_sales += sales[i]

    if sales[i] >= 3000:
        high_sales_days += 1

    i += 1

average_sales = total_sales / len(sales)

print("Total Sales:", total_sales)
print("Average Sales:", round(average_sales, 2))
print("High-Sales Days:", high_sales_days)
```

Expected results:

* Total Sales: `22500`
* Average Sales: `3214.29`
* High-Sales Days: `4`

---

## 19. While Loop vs For Loop

| Feature        | While Loop                        | For Loop                                      |
| -------------- | --------------------------------- | --------------------------------------------- |
| Main use       | Repeats while a condition is true | Iterates over a sequence or range             |
| Condition      | Explicit condition required       | Often controlled by the iterable              |
| Counter update | Often manual                      | Usually automatic when iterating over a range |
| Common use     | Menus and input validation        | Lists, ranges, and repeated tasks             |

Both loops can process lists and perform calculations.

---

## 20. Quick Revision

* `while condition:` repeats while the condition is true.
* `i += 1` increases a counter.
* `i -= 1` decreases a counter.
* `total += value` accumulates values.
* `len(list_name)` returns the number of list elements.
* `list_name[i]` accesses an element by index.
* `append()` adds an item to a list.
* `break` exits the loop.
* `continue` skips to the next iteration.
* `while True` creates a loop that needs an explicit exit.
* Always avoid accidental infinite loops.

---

## 🎯 Day 11 Learning Goal

By completing Day 11, you should be able to:

1. Write basic while loops.
2. Perform counting and reverse counting.
3. Calculate sums and factorials.
4. Accept user input repeatedly.
5. Process lists using indexes.
6. Build menu-driven programs.
7. Use loops to solve basic business and data analytics problems.

**Next: Day 12 — break, continue, and pass**

````

### ✅ File 7 Complete!

**GitHub Commit Message:**
```text
Add Day 11 Python While Loop Notes
````

Bhai, ab `Notes.md` upload kar do. Uske baad hum **File 8: `Day-11-Summary.png`** banayenge — cute, stylish Python-themed infographic ke saath. 🐍📊
