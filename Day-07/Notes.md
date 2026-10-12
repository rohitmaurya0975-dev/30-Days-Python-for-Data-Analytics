# 🐍 Day 07 — Python Tuples & Sets

## 30 Days Python Challenge for Data Analytics

**Topics:** Tuples, Indexing, Immutability, Sets, Unique Values, `len()`, `add()`, `remove()`, `discard()`

---

## 1. What is a Tuple?

A **Tuple** is an ordered collection of items in Python.

Tuples are written using round brackets `()`.

### Example

```python
fruits = ("Apple", "Mango", "Banana")

print(fruits)
```

**Output:**

```text
('Apple', 'Mango', 'Banana')
```

### Important Features of Tuples

* Tuples are ordered.
* Tuples allow duplicate values.
* Tuples support indexing.
* Tuples can contain different data types.
* Tuple items cannot be changed after creation.

### Example with Different Data Types

```python
student = ("Rohit", 85, 21, True)

print(student)
```

---

## 2. Tuple Indexing

Indexing is used to access individual items from a tuple.

Python indexing starts from `0`.

### Example

```python
courses = ("Python", "SQL", "Power BI", "Excel")

print(courses[0])
print(courses[1])
print(courses[2])
print(courses[3])
```

**Output:**

```text
Python
SQL
Power BI
Excel
```

| Item     | Index |
| -------- | ----: |
| Python   |     0 |
| SQL      |     1 |
| Power BI |     2 |
| Excel    |     3 |

### Negative Indexing

Negative indexing accesses items from the end.

* `-1` → Last item
* `-2` → Second-last item
* `-3` → Third-last item

```python
cities = ("Delhi", "Mumbai", "Surat", "Jaipur")

print(cities[-1])
print(cities[-2])
```

**Output:**

```text
Jaipur
Surat
```

---

## 3. Tuple Immutability

**Immutable** means that an item's value cannot be changed after the tuple is created.

### Example

```python
marks = (70, 80, 90)

print(marks[0])
```

Output:

```text
70
```

Trying to update an item directly causes a `TypeError`.

```python
marks = (70, 80, 90)

marks[0] = 100
```

This code raises an error because tuple items cannot be reassigned.

### Remember

* List → Mutable (items can be changed).
* Tuple → Immutable (items cannot be changed).

---

## 4. List vs Tuple

| Feature                 | List                   | Tuple                                |
| ----------------------- | ---------------------- | ------------------------------------ |
| Brackets                | `[]`                   | `()`                                 |
| Ordered                 | Yes                    | Yes                                  |
| Allows duplicates       | Yes                    | Yes                                  |
| Supports indexing       | Yes                    | Yes                                  |
| Items can be reassigned | Yes                    | No                                   |
| Common use              | Changeable collections | Collections that should remain fixed |

### Example: List

```python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

Output:

```text
[100, 20, 30]
```

### Example: Tuple

```python
numbers = (10, 20, 30)

print(numbers[0])
```

Output:

```text
10
```

---

## 5. The `len()` Function

The `len()` function returns the number of items in a tuple or set.

### Example: Tuple

```python
marks = (85, 90, 78, 92, 88)

print(len(marks))
```

Output:

```text
5
```

### Example: Set

```python
numbers = {10, 20, 30, 40}

print(len(numbers))
```

Output:

```text
4
```

**Remember:** `len()` counts items; it does not calculate their sum.

---

## 6. What is a Set?

A **Set** is a collection that stores unique items.

Sets are generally created using curly brackets `{}`.

### Example

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

Output contains:

```text
{10, 20, 30, 40}
```

### Important Features of Sets

* Sets store unique values.
* Duplicate values are removed.
* Sets do not support indexing.
* Sets are mutable, so items can be added or removed.
* The order of set items is not guaranteed.
* A set can contain different hashable data types.

### Example: Duplicate Values

```python
products = {
    "Laptop",
    "Mouse",
    "Laptop",
    "Keyboard",
    "Mouse"
}

print(products)
print(len(products))
```

The set contains three unique product names. The order displayed may vary.

**Remember:** Set = Unique Values.

### Important: Empty Set

```python
empty_set = set()
```

Use `set()` to create an empty set.

`{}` creates an empty dictionary, not an empty set.

---

## 7. The `add()` Method

The `add()` method adds an item to a set.

### Example

```python
skills = {"Python", "SQL", "Excel"}

skills.add("Power BI")

print(skills)
```

The set now includes `"Power BI"`.

Adding a value that already exists does not create a duplicate.

```python
skills.add("Python")

print(skills)
```

Python still appears only once in the set.

---

## 8. The `remove()` Method

The `remove()` method removes a specified item from a set.

### Example

```python
products = {"Laptop", "Mouse", "Keyboard"}

products.remove("Mouse")

print(products)
```

The set no longer contains `"Mouse"`.

### Important

If the specified item does not exist, `remove()` raises a `KeyError`.

Use `remove()` when you expect the item to exist.

---

## 9. The `discard()` Method

The `discard()` method removes a specified item if it exists.

If the item does not exist, Python does not raise an error.

### Example

```python
departments = {"HR", "IT", "Sales"}

departments.discard("Finance")

print(departments)
```

The set remains unchanged because `"Finance"` was not present.

### Difference Between `remove()` and `discard()`

| Method      | Item exists      | Item does not exist |
| ----------- | ---------------- | ------------------- |
| `remove()`  | Removes the item | Raises `KeyError`   |
| `discard()` | Removes the item | No error            |

---

## 10. Tuples and Sets in Data Analytics

### Example 1: Store Fixed Product Prices

```python
product_prices = (50000, 500, 1500, 12000)

print("Product Prices:", product_prices)
print("First Product Price:", product_prices[0])
print("Number of Price Records:", len(product_prices))
```

A tuple can be useful for storing a collection of values that should not be reassigned item by item.

### Example 2: Find Unique Customer IDs

```python
customer_ids = {101, 102, 101, 103, 102, 104}

print("Unique Customer IDs:", customer_ids)
print("Unique Customer Count:", len(customer_ids))
```

The set stores each unique customer ID once.

### Example 3: Add a New Customer

```python
customer_ids = {101, 102, 103, 104}

customer_ids.add(105)

print(customer_ids)
```

The new customer ID is added to the set.

**Business applications:**

* Store a fixed collection of product prices.
* Count unique customer IDs.
* Find unique product categories.
* Remove unwanted values from a set.
* Manage collections of unique identifiers.

**Important:** A set is useful for uniqueness, but it does not preserve the original order of records.

---

## 11. Common Mistakes

### Mistake 1: Using an Invalid Tuple Index

Incorrect:

```python
courses = ("Python", "SQL", "Excel")

print(courses[3])
```

Correct:

```python
print(courses[2])
```

The last valid positive index is `2`.

### Mistake 2: Trying to Update a Tuple

Incorrect:

```python
marks = (70, 80, 90)

marks[0] = 100
```

Tuple items cannot be reassigned directly.

### Mistake 3: Using `add()` Incorrectly

Incorrect:

```python
skills.add["Python"]
```

Correct:

```python
skills.add("Python")
```

### Mistake 4: Forgetting the Item in `remove()`

Incorrect:

```python
products.remove()
```

Correct:

```python
products.remove("Mouse")
```

### Mistake 5: Using Indexing on a Set

Incorrect:

```python
numbers = {10, 20, 30}

print(numbers[0])
```

Sets do not support indexing.

### Mistake 6: Creating an Empty Set Incorrectly

Incorrect:

```python
numbers = {}
```

This creates an empty dictionary.

Correct:

```python
numbers = set()
```

---

## 12. Day 07 Quick Revision

| Concept           | Purpose                       | Example                  |
| ----------------- | ----------------------------- | ------------------------ |
| Tuple             | Ordered, immutable collection | `numbers = (10, 20, 30)` |
| Tuple indexing    | Access an item                | `numbers[0]`             |
| Negative indexing | Access from the end           | `numbers[-1]`            |
| `len()`           | Count items                   | `len(numbers)`           |
| Set               | Store unique items            | `numbers = {10, 20, 30}` |
| `add()`           | Add an item                   | `numbers.add(40)`        |
| `remove()`        | Remove an existing item       | `numbers.remove(20)`     |
| `discard()`       | Remove safely if present      | `numbers.discard(50)`    |

---

## 13. Memory Tricks 🧠

**Tuple = Fixed Collection**

* Uses `()`.
* Ordered.
* Allows duplicates.
* Items cannot be reassigned.

**Set = Unique Collection**

* Usually uses `{}`.
* Removes duplicate values.
* Does not support indexing.
* Items can be added or removed.

**List vs Tuple vs Set**

* List `[]` → Changeable and ordered.
* Tuple `()` → Ordered and immutable.
* Set `{}` → Unique items; order is not guaranteed.

---

## 14. Day 07 Completion Checklist

* [ ] Create tuples.
* [ ] Access tuple items using positive indexing.
* [ ] Access tuple items using negative indexing.
* [ ] Understand tuple immutability.
* [ ] Understand List vs Tuple.
* [ ] Create sets.
* [ ] Understand duplicate removal.
* [ ] Count items using `len()`.
* [ ] Add items using `add()`.
* [ ] Remove items using `remove()`.
* [ ] Safely discard items using `discard()`.
* [ ] Complete practice and debugging exercises.
* [ ] Run the Customer & Product Analyzer.

---

## 📅 Next Day: Day 08 — Python Dictionaries

In Day 08, we will learn:

* What dictionaries are.
* Keys and values.
* Accessing dictionary values.
* Adding and updating entries.
* Removing entries.
* Counting and managing records.

**Keep practising one concept at a time. Strong basics make Data Analytics easier!** 🐍📊
