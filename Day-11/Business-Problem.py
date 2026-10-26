
# =====================================================
# Day 11: Business Problem
# Sales Performance Analyzer
# 30 Days Python for Data Analytics
# =====================================================

print("=" * 40)
print("       SALES PERFORMANCE ANALYZER")
print("=" * 40)


# Business Data: Daily Sales
sales = [1200, 3500, 1800, 4500, 2500, 5000, 4000]

# Variables
i = 0
total_sales = 0
high_sales_days = 0
low_sales_days = 0

# Business Rules
high_sales_target = 3000
low_sales_target = 2000

# Process sales using a while loop
while i < len(sales):

    current_sale = sales[i]

    # Calculate total sales
    total_sales += current_sale

    # Count high-sales days
    if current_sale >= high_sales_target:
        high_sales_days += 1

    # Count low-sales days
    if current_sale < low_sales_target:
        low_sales_days += 1

    i += 1


# Calculate average sales
average_sales = total_sales / len(sales)


# Display Report
print("\nDAILY SALES DATA")
print("-" * 40)
print("Sales:", sales)

print("\nSALES PERFORMANCE REPORT")
print("-" * 40)
print("Total Sales:", total_sales)
print("Average Daily Sales:", round(average_sales, 2))
print("High-Sales Days:", high_sales_days)
print("Low-Sales Days:", low_sales_days)


# Business Performance Evaluation
print("\nBUSINESS INSIGHTS")
print("-" * 40)

if average_sales >= high_sales_target:
    print("Performance: Good")
else:
    print("Performance: Needs Improvement")

print("High-Sales Target:", high_sales_target)
print("Low-Sales Threshold:", low_sales_target)

print("\nAnalysis completed successfully!")
print("=" * 40)


# =====================================================
# END OF SALES PERFORMANCE ANALYZER
# =====================================================

