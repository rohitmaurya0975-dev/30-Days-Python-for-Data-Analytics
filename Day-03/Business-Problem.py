# ==========================================
# Day 03 - Business Problem
# ==========================================

# A shopkeeper wants to calculate a customer's final bill.
#
# Product Price
# Quantity
# Discount
#
# Formula:
# Total Price = Product Price * Quantity
# Final Amount = Total Price - Discount


product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount: "))

total_price = product_price * quantity
final_amount = total_price - discount

print("Total Price:", total_price)
print("Discount:", discount)
print("Final Amount:", final_amount)

