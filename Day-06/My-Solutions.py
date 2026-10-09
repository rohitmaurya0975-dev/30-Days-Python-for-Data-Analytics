
# Day 06 - My Solutions
# 30 Days Python Challenge for Data Analytics
# Topic: Python Lists


# Q01. Create a List
fruits = ["Apple", "Mango", "Banana"]
print(fruits)


# Q02. Access List Items
students = ["Rahul", "Priya", "Amit", "Neha"]

print("First Student:", students[0])
print("Third Student:", students[2])


# Q03. Negative Indexing
print("Last Student:", students[-1])
print("Second-Last Student:", students[-2])


# Q04. Count Items
marks = [85, 90, 78, 92, 88]

print("Total Records:", len(marks))


# Q05. Update a List Item
marks = [70, 80, 60, 90]

marks[2] = 75

print("Updated Marks:", marks)


# Q06. Add an Item Using append()
employees = ["Rahul", "Priya", "Amit"]

employees.append("Neha")

print("Updated Employees:", employees)


# Q07. Insert an Item
students = ["Rahul", "Amit", "Neha"]

students.insert(1, "Priya")

print("Updated Students:", students)


# Q08. Remove an Item
employees = ["Rahul", "Priya", "Amit", "Neha"]

employees.remove("Amit")

print("Employees After Removal:", employees)


# Q09. Use pop()
numbers = [10, 20, 30, 40]

removed_number = numbers.pop(1)

print("Removed Number:", removed_number)
print("Updated Numbers:", numbers)


# Q10. Sort Sales Data
daily_sales = [5000, 7500, 6200, 9000, 8500]

daily_sales.sort()
print("Ascending Sales:", daily_sales)

daily_sales.sort(reverse=True)
print("Descending Sales:", daily_sales)


# BONUS. Mini Data Analytics Task
sales = [1200, 1800, 950, 2100, 1600]

print("Total Sales Records:", len(sales))

sales.append(2500)
sales.sort(reverse=True)

print("Final Sales List:", sales)