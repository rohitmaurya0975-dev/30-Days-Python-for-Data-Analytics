# Day 05 - Business Problem
# 30 Days Python Challenge for Data Analytics
# Topic: Python Strings + Basic Data Cleaning

# Business Problem:
# A company has customer data with extra spaces
# and inconsistent capitalization.
# Clean the customer information before analysis.

customer_name = input("Enter customer name: ")
city = input("Enter customer city: ")
product = input("Enter product name: ")

# Remove extra spaces
clean_name = customer_name.strip()
clean_city = city.strip()
clean_product = product.strip()

# Standardize text
clean_name = clean_name.title()
clean_city = clean_city.title()
clean_product = clean_product.title()

# Display cleaned data
print("\n--- Clean Customer Data ---")
print("Customer Name:", clean_name)
print("City:", clean_city)
print("Product:", clean_product)

# Find name length
print("Name Length:", len(clean_name))

# Check first and last character
print("First Character:", clean_name[0])
print("Last Character:", clean_name[-1])