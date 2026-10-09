# Day 05 — Python Strings

## 1. What is a String?

A string is a collection of characters/text written inside quotes.

```python
name = "Rohit"
city = "Delhi"
course = "Data Analytics"
```

---

## 2. Single and Double Quotes

Both are valid:

```python
name = "Rohit"
city = 'Delhi'
```

---

## 3. String Concatenation

Two or more strings can be joined using `+`.

```python
first_name = "Rohit"
last_name = "Maurya"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Rohit Maurya
```

---

## 4. len()

`len()` is used to find the number of characters in a string.

```python
course = "Data Analytics"

print(len(course))
```

---

## 5. String Indexing

Python indexing starts from **0**.

```python
language = "Python"

print(language[0])   # P
print(language[1])   # y
print(language[2])   # t
```

### Memory Trick

```text
P y t h o n
0 1 2 3 4 5
```

---

## 6. Negative Indexing

Negative indexing starts from the last character.

```python
language = "Python"

print(language[-1])   # n
print(language[-2])   # o
```

### Memory Trick

```text
P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
```

---

## 7. String Slicing

Slicing is used to extract a part of a string.

Syntax:

```python
string[start:end]
```

The `end` position is not included.

Example:

```python
language = "Python"

print(language[0:3])
```

Output:

```text
Pyt
```

More examples:

```python
print(language[:3])   # Pyt
print(language[3:])   # hon
print(language[:])    # Python
```

---

## 8. upper()

Converts text into uppercase.

```python
name = "rohit"

print(name.upper())
```

Output:

```text
ROHIT
```

---

## 9. lower()

Converts text into lowercase.

```python
name = "ROHIT"

print(name.lower())
```

Output:

```text
rohit
```

---

## 10. strip()

Removes extra spaces from the beginning and end.

```python
city = "   Delhi   "

print(city.strip())
```

Output:

```text
Delhi
```

---

## 11. replace()

Used to replace text.

```python
city = "Mumbai"

print(city.replace("Mumbai", "Delhi"))
```

Output:

```text
Delhi
```

---

## 12. find()

Used to find the position of a character or word.

```python
name = "Rohit"

print(name.find("h"))
```

Output:

```text
3
```

If the text is not found, `find()` returns:

```text
-1
```

---

# ⭐ Important String Functions

| Function     | Use                 |
| ------------ | ------------------- |
| `len()`      | Find length         |
| `.upper()`   | Uppercase           |
| `.lower()`   | Lowercase           |
| `.strip()`   | Remove extra spaces |
| `.replace()` | Replace text        |
| `.find()`    | Find position       |

---

# 📊 Data Analytics Connection

String operations are very important in Data Analytics because real-world data often contains:

* Extra spaces
* Different capitalization
* Incorrect text
* Inconsistent city names
* Inconsistent customer names

Example:

```python
customer = "   rohit maurya   "

clean_customer = customer.strip().title()

print(clean_customer)
```

Output:

```text
Rohit Maurya
```

This is a basic example of **Data Cleaning**.

---

# 🧠 Day 05 Memory Trick

Remember this sequence:

**String → Index → Slice → Clean → Analyze**

```text
String
   ↓
Index
   ↓
Slice
   ↓
Clean
   ↓
Analyze
```

---

# ⚠️ Common Mistakes

### Mistake 1 — Forgetting brackets

Wrong:

```python
name.upper
```

Correct:

```python
name.upper()
```

### Mistake 2 — Wrong index

For:

```python
name = "Rohit"
```

The valid positive indexes are:

```text
0 1 2 3 4
```

So:

```python
name[5]
```

will cause an error.

### Mistake 3 — Joining string and number directly

Wrong:

```python
price = 500
print("Price: " + price)
```

Correct:

```python
print("Price: " + str(price))
```

---

# 🎯 Day 05 Summary

Today we learned:

* What is a String
* String creation
* Concatenation
* `len()`
* Positive indexing
* Negative indexing
* Slicing
* `.upper()`
* `.lower()`
* `.strip()`
* `.replace()`
* `.find()`
* Basic text cleaning
* Data Analytics connection

## Next Day

### Day 06 — Python Lists 🐍📊

We will learn how to store multiple values together using Lists.
