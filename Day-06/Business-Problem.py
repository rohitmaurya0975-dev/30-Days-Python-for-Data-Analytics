
# Day 06 - Business Problem
# 30 Days Python Challenge for Data Analytics
# Topic: Python Lists
# Project: Shop Inventory Analyzer


# Step 1: Store Product Names

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

print("Shop Products:", products)


# Step 2: Store Product Prices

prices = [50000, 500, 1500, 12000, 2000]

print("Product Prices:", prices)


# Step 3: Store Available Stock

stock = [10, 50, 25, 8, 30]

print("Available Stock:", stock)


# Step 4: Count Total Products

print("Total Product Types:", len(products))


# Step 5: Add a New Product

products.append("Webcam")
prices.append(2500)
stock.append(15)

print("Updated Products:", products)


# Step 6: Update Laptop Price
prices[0] = 48000

print("Updated Prices:", prices)


# Step 7: Remove a Product
products.remove("Mouse")
prices.pop(1)
stock.pop(1)

print("Products After Removal:", products)


# Step 8: Calculate Inventory Value
inventory_value = 0

for i in range(len(products)):
    inventory_value = inventory_value + (prices[i] * stock[i])

print("Total Inventory Value:", inventory_value)


# Step 9: Display Final Inventory Report
print("\n===== INVENTORY REPORT =====")

for i in range(len(products)):
    print(
        "Product:", products[i],
        "| Price:", prices[i],
        "| Stock:", stock[i],
        "| Value:", prices[i] * stock[i]
    )

print("============================")

