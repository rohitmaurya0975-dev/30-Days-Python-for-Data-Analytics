# Day 07 - Python Tuples & Sets Challenge
# 30 Days Python Challenge for Data Analytics

# Challenge 1: Create a Tuple
subjects = ("DBMS", "Python", "SQL", "DAA")
print("Subjects:", subjects)


# Challenge 2: Access Tuple Items
employees = ("Amit", "Priya", "Rahul", "Neha")
print("First Employee:", employees[0])
print("Last Employee:", employees[-1])


# Challenge 3: Count Tuple Items

sales = (1200, 1500, 1800, 2000, 2500)
print("Total Sales Records:", len(sales))


# Challenge 4: Store Product Prices in a Tuple
prices = (500, 1200, 800, 2500)
print("First Product Price:", prices[0])
print("Total Products:", len(prices))


# Challenge 5: Create a Set of Cities
cities = {"Delhi", "Mumbai", "Surat", "Delhi", "Mumbai"}
print("Unique Cities:", cities)
print("Total Unique Cities:", len(cities))


# Challenge 6: Create a Set of Skills
skills = {"Excel", "SQL", "Python"}
skills.add("Power BI")
print("Updated Skills:", skills)


# Challenge 7: Remove a Product
products = {"Laptop", "Mouse", "Keyboard", "Monitor"}
products.remove("Mouse")
print("Remaining Products:", products)


# Challenge 8: Safely Discard an Item
departments = {"HR", "IT", "Sales"}
departments.discard("Finance")
print("Departments:", departments)


# Challenge 9: Unique Customer IDs
customer_ids = {101, 102, 103, 101, 104, 102}
print("Unique Customer IDs:", customer_ids)
print("Unique Customer Count:", len(customer_ids))


# Challenge 10: Unique Product Categories
categories = {
    "Electronics",
    "Clothing",
    "Electronics",
    "Grocery",
    "Clothing",
    "Books"
}

print("Unique Categories:", categories)
print("Total Unique Categories:", len(categories))