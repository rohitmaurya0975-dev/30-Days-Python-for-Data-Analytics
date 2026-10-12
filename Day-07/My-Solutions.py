# Day 07 - My Solutions
# 30 Days Python Challenge for Data Analytics
# Topic: Python Tuples & Sets


# Q01. Create a Tuple
fruits = ("Apple", "Mango", "Banana")
print("Q01 - Fruits:", fruits)


# Q02. Access Tuple Items
courses = ("Python", "SQL", "Power BI", "Excel")
print("Q02 - First Course:", courses[0])
print("Q02 - Third Course:", courses[2])


# Q03. Negative Indexing
cities = ("Delhi", "Mumbai", "Surat", "Jaipur")
print("Q03 - Last City:", cities[-1])
print("Q03 - Second-Last City:", cities[-2])


# Q04. Count Tuple Items
marks = (85, 90, 78, 92, 88)
print("Q04 - Total Marks Records:", len(marks))


# Q05. Tuple vs List
numbers = [10, 20, 30]
numbers[0] = 100
print("Q05 - Updated List:", numbers)


# Q06. Create a Set
numbers_set = {10, 20, 10, 30, 20, 40}
print("Q06 - Unique Numbers:", numbers_set)


# Q07. Count Unique Values
products = {
    "Laptop",
    "Mouse",
    "Laptop",
    "Keyboard",
    "Mouse"
}
print("Q07 - Unique Products:", len(products))


# Q08. Add an Item to a Set
skills = {"Python", "SQL", "Excel"}
skills.add("Power BI")
print("Q08 - Updated Skills:", skills)


# Q09. Remove an Item from a Set
cities = {"Delhi", "Mumbai", "Surat", "Jaipur"}
cities.remove("Mumbai")
print("Q09 - Updated Cities:", cities)


# Q10. Use discard()
employees = {"Rahul", "Priya", "Amit"}
employees.discard("Neha")
print("Q10 - Updated Employees:", employees)


# BONUS - Unique Customer Analyzer

customer_ids = {101, 102, 101, 103, 104, 102, 105}

# Step 1: Print unique customer IDs
print("Bonus - Unique Customer IDs:", customer_ids)

# Step 2: Count unique customers
print("Bonus - Unique Customer Count:", len(customer_ids))

# Step 3: Add a new customer
customer_ids.add(106)

# Step 4: Remove customer ID 103
customer_ids.remove(103)

# Step 5: Print the final set
print("Bonus - Final Customer IDs:", customer_ids)