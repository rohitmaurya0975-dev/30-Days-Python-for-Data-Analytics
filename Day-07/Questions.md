# 🐍 Day 07 — Python Tuples & Sets

## 30 Days Python Challenge for Data Analytics

**Topics:** Tuples, Tuple Indexing, Tuple vs List, Sets, Unique Values, `add()`, `remove()`, `discard()`, `len()`

---

### Q01. Create a Tuple

Create a tuple named `fruits` containing `"Apple"`, `"Mango"`, and `"Banana"`. Print the complete tuple.

### Q02. Access Tuple Items

Given:

```python
courses = ("Python", "SQL", "Power BI", "Excel")
```

Print the first course and the third course using indexing.

### Q03. Negative Indexing

Given:

```python
cities = ("Delhi", "Mumbai", "Surat", "Jaipur")
```

Print the last city and the second-last city using negative indexing.

### Q04. Count Tuple Items

Given:

```python
marks = (85, 90, 78, 92, 88)
```

Use `len()` to print the total number of marks.

### Q05. Tuple vs List

Create a list named `numbers` containing `10`, `20`, and `30`. Change the first item to `100` and print the updated list.

### Q06. Create a Set

Create a set containing the values `10`, `20`, `10`, `30`, `20`, and `40`. Print the set.

Observe what happens to the duplicate values.

### Q07. Count Unique Values

Given:

```python
products = {"Laptop", "Mouse", "Laptop", "Keyboard", "Mouse"}
```

Use `len()` to print the number of unique products.

### Q08. Add an Item to a Set

Given:

```python
skills = {"Python", "SQL", "Excel"}
```

Add `"Power BI"` using `add()` and print the updated set.

### Q09. Remove an Item from a Set

Given:

```python
cities = {"Delhi", "Mumbai", "Surat", "Jaipur"}
```

Remove `"Mumbai"` using `remove()` and print the updated set.

### Q10. Use discard()

Given:

```python
employees = {"Rahul", "Priya", "Amit"}
```

Use `discard()` to remove `"Neha"` and print the set.

Observe whether Python raises an error.

---

## ⭐ Bonus — Unique Customer Analyzer

A company recorded the following customer IDs:

```python
customer_ids = {101, 102, 101, 103, 104, 102, 105}
```

Perform the following tasks:

1. Print the set of unique customer IDs.
2. Print the total number of unique customers using `len()`.
3. Add customer ID `106`.
4. Remove customer ID `103`.
5. Print the final set.

---

## 🧠 Day 07 Memory Trick

* **List `[]`** → Items can be changed.
* **Tuple `()`** → Items cannot be changed.
* **Set `{}`** → Stores unique values.

## 📅 Next Day

**Day 08 — Python Dictionaries**
