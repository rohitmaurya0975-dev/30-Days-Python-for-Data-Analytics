# 🐍 Day 06 — Python Lists Notes

## 30 Days Python Challenge for Data Analytics

---

## 1. What is a List?

A **List** is a collection used to store multiple items in a single variable.

Lists are written using square brackets `[]`.

### Example

```python
fruits = ["Apple", "Mango", "Banana"]

print(fruits)
```

**Output:**

```text
['Apple', 'Mango', 'Banana']
```

### Why do we use Lists?

Lists help us store and manage multiple values together.

Examples:

* Student names
* Employee salaries
* Product prices
* Daily sales
* Customer names

---

## 2. Creating Different Types of Lists

### List of Numbers

```python
marks = [85, 90, 78, 92]

print(marks)
```

### List of Strings

```python
employees = ["Rahul", "Priya", "Amit"]

print(employees)
```

### Mixed Data Types

```python
data = ["Rohit", 21, 85.5, True]

print(data)
```

A Python list can contain different data types.

---

## 3. Positive Indexing

Indexing is used to access individual items from a list.

**Remember:** Python indexing starts from `0`, not `1`.

```python
fruits = ["Apple", "Mango", "Banana", "Orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
```

**Output:**

```text
Apple
Mango
Banana
Orange
```

| Item   | Index |
| ------ | ----: |
| Apple  |     0 |
| Mango  |     1 |
| Banana |     2 |
| Orange |     3 |

**Memory Trick:** First item = index `0`.

---

## 4. Negative Indexing

Negative indexing accesses list items from the end.

* `-1` = Last item
* `-2` = Second-last item
* `-3` = Third-last item

### Example

```python
fruits = ["Apple", "Mango", "Banana", "Orange"]

print(fruits[-1])
print(fruits[-2])
```

**Output:**

```text
Orange
Banana
```

---

## 5. The `len()` Function

The `len()` function returns the total number of items in a list.

### Example

```python
students = ["Rahul", "Priya", "Amit", "Neha"]

print(len(students))
```

**Output:**

```text
4
```

### Data Analytics Example

```python
daily_sales = [1200, 1800, 950, 2100, 1600]

print("Total Sales Records:", len(daily_sales))
```

**Output:**

```text
Total Sales Records: 5
```

**Remember:** `len()` counts items; it does not calculate their sum.

---

## 6. Updating List Items

Python lists are **mutable**, which means their items can be changed after the list is created.

### Example

```python
marks = [70, 80, 60, 90]

marks[2] = 75

print(marks)
```

**Output:**

```text
[70, 80, 75, 90]
```

Here, `marks[2] = 75` changes the third item from `60` to `75`.

**Remember:** The third item has index `2`.

---

## 7. The `append()` Method

The `append()` method adds a new item to the end of a list.

### Example

```python
employees = ["Rahul", "Priya", "Amit"]

employees.append("Neha")

print(employees)
```

**Output:**

```text
['Rahul', 'Priya', 'Amit', 'Neha']
```

### Sales Example

```python
sales = [1200, 1800, 950]

sales.append(2100)

print(sales)
```

**Output:**

```text
[1200, 1800, 950, 2100]
```

**Remember:** `append()` adds an item at the end.

---

## 8. The `insert()` Method

The `insert()` method adds an item at a specified index.

### Syntax

```python
list_name.insert(index, item)
```

### Example

```python
courses = ["Excel", "SQL", "Power BI"]

courses.insert(1, "Python")

print(courses)
```

**Output:**

```text
['Excel', 'Python', 'SQL', 'Power BI']
```

Here:

* `1` is the index.
* `"Python"` is the item being inserted.

**Remember:** `insert()` adds an item at a specific position.

---

## 9. The `remove()` Method

The `remove()` method removes the first matching item by value.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)
```

**Output:**

```text
['Apple', 'Mango']
```

**Remember:** `remove()` takes the item value, not its index.

---

## 10. The `pop()` Method

The `pop()` method removes an item using its index and returns the removed item.

### Example 1: Remove by Index

```python
numbers = [10, 20, 30, 40]

removed_value = numbers.pop(1)

print("Removed Value:", removed_value)
print("Updated List:", numbers)
```

**Output:**

```text
Removed Value: 20
Updated List: [10, 30, 40]
```

### Example 2: Remove the Last Item

```python
numbers = [10, 20, 30, 40]

numbers.pop()

print(numbers)
```

**Output:**

```text
[10, 20, 30]
```

**Remember:**

* `pop(1)` removes the item at index `1`.
* `pop()` without an index removes the last item.

---

## 11. The `sort()` Method

The `sort()` method arranges list items in ascending or descending order.

### Ascending Order

Smallest to largest.

```python
sales = [5000, 7500, 6200, 9000, 8500]

sales.sort()

print(sales)
```

**Output:**

```text
[5000, 6200, 7500, 8500, 9000]
```

### Descending Order

Largest to smallest.

```python
sales = [5000, 7500, 6200, 9000, 8500]

sales.sort(reverse=True)

print(sales)
```

**Output:**

```text
[9000, 8500, 7500, 6200, 5000]
```

**Remember:**

* `sort()` = Ascending order.
* `sort(reverse=True)` = Descending order.

---

## 12. Lists in Data Analytics

Lists can store simple business data, such as daily sales.

### Example

```python
daily_sales = [1200, 1800, 950, 2100, 1600]

print("Daily Sales:", daily_sales)
print("Number of Records:", len(daily_sales))

daily_sales.append(2500)

print("Updated Sales:", daily_sales)

daily_sales.sort()

print("Sorted Sales:", daily_sales)
```

**What did we learn?**

1. Store multiple sales records.
2. Count the records using `len()`.
3. Add a new record using `append()`.
4. Arrange the records using `sort()`.

**Note:** This example only counts and organizes the records; it does not calculate total sales.

---

## 13. Common Mistakes

### Mistake 1: Using the Wrong Index

Incorrect:

```python
fruits = ["Apple", "Mango", "Banana"]
print(fruits[3])
```

Correct:

```python
print(fruits[2])
```

The third item is at index `2`.

### Mistake 2: Incorrect `append()` Syntax

Incorrect:

```python
fruits.append["Orange"]
```

Correct:

```python
fruits.append("Orange")
```

### Mistake 3: Incorrect `insert()` Syntax

Incorrect:

```python
fruits.insert(1 "Orange")
```

Correct:

```python
fruits.insert(1, "Orange")
```

### Mistake 4: Confusing `remove()` and `pop()`

```python
fruits.remove("Mango")
```

Removes an item by value.

```python
fruits.pop(1)
```

Removes an item by index.

### Mistake 5: Forgetting That Indexing Starts at Zero

For a list containing four items, the valid positive indexes are `0`, `1`, `2`, and `3`.

---

## 14. Day 06 Quick Revision

| Concept           | Purpose                    | Example                      |
| ----------------- | -------------------------- | ---------------------------- |
| Create a list     | Store multiple items       | `numbers = [10, 20, 30]`     |
| Indexing          | Access an item             | `numbers[0]`                 |
| Negative indexing | Access from the end        | `numbers[-1]`                |
| `len()`           | Count the items            | `len(numbers)`               |
| Update            | Change an item             | `numbers[0] = 50`            |
| `append()`        | Add at the end             | `numbers.append(40)`         |
| `insert()`        | Add at a position          | `numbers.insert(1, 15)`      |
| `remove()`        | Remove by value            | `numbers.remove(20)`         |
| `pop()`           | Remove by index            | `numbers.pop(0)`             |
| `sort()`          | Arrange in ascending order | `numbers.sort()`             |
| Descending sort   | Largest to smallest        | `numbers.sort(reverse=True)` |

---

## 15. Day 06 Memory Trick 🧠

**Create → Access → Count → Update → Add → Remove → Sort**

* **Create:** Make a list using `[]`.
* **Access:** Use indexing.
* **Count:** Use `len()`.
* **Update:** Change an item using its index.
* **Add:** Use `append()` or `insert()`.
* **Remove:** Use `remove()` or `pop()`.
* **Sort:** Use `sort()`.

---

## ✅ Day 06 Completion Checklist

* [ ] Understand Python Lists.
* [ ] Create lists with different data types.
* [ ] Use positive and negative indexing.
* [ ] Count items using `len()`.
* [ ] Update list items.
* [ ] Add items using `append()` and `insert()`.
* [ ] Remove items using `remove()` and `pop()`.
* [ ] Sort items in ascending and descending order.
* [ ] Complete the Day 06 questions.
* [ ] Practice the Shop Inventory example without using loops.

---

## 📅 Next Day: Day 07 — Python Tuples and Sets

In Day 07, we will learn:

* What tuples are.
* How tuples differ from lists.
* What sets are.
* How sets handle duplicate values.
* Basic tuple and set operations.

**Important:** We will learn loops separately when their turn comes. We will not use an unlearned concept in your practice files.
