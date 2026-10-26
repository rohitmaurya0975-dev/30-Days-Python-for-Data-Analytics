# ==========================================
# DAY 10 - BUSINESS PROBLEM
# Sales Data Analyzer
# 30 Days Python Challenge for Data Analytics
# ==========================================

print("===== SALES DATA ANALYZER =====")

# Daily sales data in rupees
sales = [1200, 3500, 1800, 4500, 2500, 5000, 4000]

# Variables
total_sales = 0
high_sales_count = 0
low_sales_count = 0

# Analyze sales using for loop
for amount in sales:

    # Calculate total sales
    total_sales = total_sales + amount

    # Count high sales (3000 or more)
    if amount >= 3000:
        high_sales_count = high_sales_count + 1

    # Count low sales (less than 3000)
    else:
        low_sales_count = low_sales_count + 1

# Calculate average sales
average_sales = total_sales / len(sales)

# Display results
print("\nTotal Days:", len(sales))
print("Total Sales: Rs.", total_sales)
print("Average Sales: Rs.", average_sales)
print("High Sales Days:", high_sales_count)
print("Low Sales Days:", low_sales_count)

print("\n===== ANALYSIS COMPLETED =====")


