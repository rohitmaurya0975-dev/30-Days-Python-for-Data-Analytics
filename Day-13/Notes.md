# 🐍 Day 13 — Python Functions

## 1. What is a Function?    

A function is a reusable block of code that performs a particular task.

Instead of writing the same code again and again, we can create a function and call it whenever required.

Example:

```python
def greet():
    print("Hello Python")

greet()
```

Output:

```text
Hello Python
```

---

## 2. Why Do We Use Functions?

Functions help us to:

* Reuse code.
* Reduce repetition.
* Organize programs.
* Make code easier to understand.
* Simplify debugging.
* Perform repeated calculations.

---

## 3. Creating a Function

Python uses the `def` keyword to define a function.

Syntax:

```python
def function_name():
    # Code to execute
```

Example:

```python
def welcome():
    print("Welcome to Python")

welcome()
```

Important:

* `def` defines a function.
* Function name identifies the function.
* Parentheses `()` are used for parameters.
* Colon `:` starts the function body.
* Indentation defines the function body.

---

## 4. Calling a Function

A function is executed when we call it.

Example:

```python
def greet():
    print("Hello Rohit")

greet()
```

Output:

```text
Hello Rohit
```

Remember: Defining a function does not execute its body automatically.

---

## 5. Parameters and Arguments

Parameters are variables written inside the function definition.

Arguments are actual values passed when calling the function.

Example:

```python
def welcome(name):
    print(f"Welcome {name}")

welcome("Rohit")
```

Here:

* `name` = Parameter
* `"Rohit"` = Argument

---

## 6. Multiple Parameters

A function can accept multiple parameters.

Example:

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

---

## 7. Return Statement

The `return` statement sends a result back from a function.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

We can store the returned value in a variable and use it in further calculations.

---

## 8. Difference Between print() and return

| print()                                       | return                             |
| --------------------------------------------- | ---------------------------------- |
| Displays output                               | Sends result back                  |
| Mainly used to show information               | Used to provide a result           |
| Does not automatically give a reusable result | Result can be stored in a variable |
| Used for displaying messages                  | Useful for calculations            |

Example:

```python
def using_print(a, b):
    print(a + b)

def using_return(a, b):
    return a + b

using_print(10, 20)

result = using_return(10, 20)
print(result)
```

---

## 9. Function with Conditions

We can use `if` and `else` inside functions.

Example:

```python
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))
```

Output:

```text
Even
```

---

## 10. Data Analytics Examples

### A. Calculate Profit

```python
def calculate_profit(revenue, cost):
    return revenue - cost

profit = calculate_profit(15000, 9000)

print(profit)
```

Output:

```text
6000
```

### B. Calculate Total Sales

```python
def calculate_sales(price, quantity):
    return price * quantity

total = calculate_sales(500, 4)

print(total)
```

Output:

```text
2000
```

### C. Calculate Average

```python
def calculate_average(a, b, c):
    return (a + b + c) / 3

print(calculate_average(70, 80, 90))
```

Output:

```text
80.0
```

---

## 11. Common Mistakes

### Mistake 1: Forgetting Parentheses

Wrong:

```python
greet
```

Correct:

```python
greet()
```

### Mistake 2: Incorrect Indentation

Wrong:

```python
def greet():
print("Hello")
```

Correct:

```python
def greet():
    print("Hello")
```

### Mistake 3: Missing Arguments

Wrong:

```python
def add(a, b):
    return a + b

add(10)
```

Correct:

```python
add(10, 20)
```

### Mistake 4: Forgetting Return

Wrong:

```python
def square(number):
    number * number
```

Correct:

```python
def square(number):
    return number * number
```

---

## 12. Important Function Rules

1. Use `def` to create a function.
2. Use parentheses to call a function.
3. Pass the required arguments.
4. Maintain proper indentation.
5. Use `return` when you need a result.
6. Choose meaningful function names.
7. A function can be called multiple times.

---

# 🧠 Day 13 Memory Trick

Remember:

**Define → Call → Input → Process → Return**

```text
Define Function
      ↓
Call Function
      ↓
Pass Arguments
      ↓
Perform Calculation
      ↓
Return Result
```

---

# 🎯 Day 13 Summary

Today we learned:

* What is a function?
* Why functions are useful.
* `def` keyword.
* Function definition.
* Function calling.
* Parameters and arguments.
* Multiple parameters.
* `return` statement.
* Difference between `print()` and `return`.
* Conditional statements inside functions.
* Real-world Data Analytics calculations.

---

## 📊 Business Applications

Functions can be used in Data Analytics for:

* Calculating revenue.
* Calculating profit.
* Calculating average sales.
* Calculating employee salaries.
* Calculating discounts.
* Analyzing business performance.

---

## 🚀 Next Day

# Day 14 — Python Function Arguments & Return

We will learn:

* Positional arguments.
* Keyword arguments.
* Default arguments.
* Multiple return values.
* Local and global variables.

**Keep Practicing! 🐍**

30 Days • 30 Concepts • One Goal → Data Analytics Mastery
