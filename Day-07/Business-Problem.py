# Day 07 - Business Problem
# 30 Days Python Challenge for Data Analytics
# Project: Customer & Product Analyzer
# Concepts: Tuples, Sets, Indexing, len(), add(), discard()

print("===== CUSTOMER & PRODUCT ANALYZER =====")

# Step 1: Store Product Names in a Tuple
products = ("Laptop", "Mouse", "Keyboard", "Monitor")

print("\nProduct List:", products)
print("First Product:", products[0])
print("Last Product:", products[-1])
print("Total Product Records:", len(products))


# Step 2: Store Product Prices in a Tuple
prices = (50000, 500, 1500, 12000)

print("\nProduct Prices:", prices)
print("Laptop Price:", prices[0])
print("Total Price Records:", len(prices))


# Step 3: Store Customer IDs in a Set
customer_ids = {101, 102, 101, 103, 104, 102, 105}

print("\nCustomer IDs:", customer_ids)
print("Total Unique Customers:", len(customer_ids))


# Step 4: Add a New Customer
customer_ids.add(106)

print("\nAfter Adding Customer 106:", customer_ids)
print("Updated Unique Customer Count:", len(customer_ids))


# Step 5: Remove a Customer Safely
customer_ids.discard(103)

print("\nAfter Removing Customer 103:", customer_ids)


# Step 6: Store Product Categories in a Set
categories = {
    "Electronics",
    "Accessories",
    "Electronics",
    "Computer Parts",
    "Accessories"
}

print("\nUnique Product Categories:", categories)
print("Total Unique Categories:", len(categories))


# Step 7: Add a New Product Category
categories.add("Office Equipment")

print("\nUpdated Categories:", categories)
print("Updated Category Count:", len(categories))


# Step 8: Final Business Summary
print("\n===== BUSINESS SUMMARY =====")
print("Total Product Records:", len(products))
print("Total Price Records:", len(prices))
print("Total Unique Customers:", len(customer_ids))
print("Total Unique Categories:", len(categories))

print("\nAnalysis Completed Successfully!")