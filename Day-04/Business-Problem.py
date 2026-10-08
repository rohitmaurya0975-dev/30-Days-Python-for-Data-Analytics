# ==========================================
# Day 04 - Business Problem
# Sales & Profit Calculator
# 30 Days Python Challenge for Data Analytics
# ==========================================

# A shop wants to calculate its total sales,
# discount, expenses, and final profit.

# Step 1: Take product information
product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity sold: "))

# Step 2: Calculate total sales
total_sales = product_price * quantity

# Step 3: Take discount percentage
discount_percent = float(input("Enter discount percentage: "))

# Step 4: Calculate discount amount
discount_amount = total_sales * discount_percent / 100

# Step 5: Calculate final sales amount
final_sales = total_sales - discount_amount

# Step 6: Take business expenses
expenses = float(input("Enter total expenses: "))

# Step 7: Calculate profit
profit = final_sales - expenses

# Step 8: Display results
print("\n========== SALES REPORT ==========")

print("Product Price:", product_price)
print("Quantity Sold:", quantity)
print("Total Sales:", total_sales)
print("Discount Amount:", discount_amount)
print("Final Sales:", final_sales)
print("Expenses:", expenses)
print("Profit:", profit)

print("==================================")