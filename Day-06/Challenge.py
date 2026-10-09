
# Day 06 - Python Lists Challenge
# 30 Days Python Challenge for Data Analytics
# Topic: Python Lists


# Challenge 1: Create a List
# Create a list of 5 favourite foods and print it.

foods = ["Pizza", "Burger", "Dosa", "Sandwich", "Pasta"]
print("Favourite Foods:", foods)


# Challenge 2: Access List Items
# Print the first and last item.

cities = ["Delhi", "Mumbai", "Surat", "Jaipur", "Pune"]

print("First City:", cities[0])
print("Last City:", cities[-1])


# Challenge 3: Count List Items
# Find the total number of employees.

employees = ["Amit", "Priya", "Rahul", "Neha", "Karan", "Riya"]

print("Total Employees:", len(employees))


# Challenge 4: Update a Value
# Change the second product price to 250.

prices = [100, 200, 300, 400]

prices[1] = 250

print("Updated Prices:", prices)


# Challenge 5: Add a New Item
# Add a new employee to the list.

employees = ["Amit", "Priya", "Rahul"]

employees.append("Neha")

print("Updated Employees:", employees)


# Challenge 6: Insert an Item
# Insert "Python" at index 1.

courses = ["Excel", "SQL", "Power BI"]

courses.insert(1, "Python")

print("Updated Courses:", courses)


# Challenge 7: Remove an Item
# Remove "Banana" from the list.

fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.remove("Banana")

print("Updated Fruits:", fruits)


# Challenge 8: Use pop()
# Remove the last number from the list.

numbers = [10, 20, 30, 40, 50]

removed_value = numbers.pop()

print("Removed Value:", removed_value)
print("Remaining Numbers:", numbers)


# Challenge 9: Sort Salaries
# Arrange salaries from highest to lowest.

salaries = [35000, 50000, 28000, 65000, 42000]

salaries.sort(reverse=True)

print("Highest to Lowest Salaries:", salaries)


# Challenge 10: Sales Data Analysis
# Count sales records and arrange sales in ascending order.

sales = [4500, 3200, 5800, 2100, 6700, 3900]

print("Total Sales Records:", len(sales))

sales.sort()

print("Sales in Ascending Order:", sales)

