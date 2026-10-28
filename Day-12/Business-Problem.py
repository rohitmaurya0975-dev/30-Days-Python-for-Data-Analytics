
# ==========================================================
# Day 12 - Business Problem
# Project: Sales Performance Analyzer
# Topics: break, continue and pass
# ==========================================================

print("=" * 45)
print("       SALES PERFORMANCE ANALYZER")
print("=" * 45)

# Daily sales data in rupees
sales = [1200, 0, 2500, 800, 3500, 0, 4200, 1800, 5000]

total_sales = 0
valid_sales_count = 0
zero_sales_days = 0
low_sales_days = 0
high_sales_days = 0

print("\nAnalyzing daily sales...\n")

for sale in sales:

    # Skip days with zero sales
    if sale == 0:
        zero_sales_days += 1
        continue

    # Skip sales below Rs. 1000
    if sale < 1000:
        low_sales_days += 1
        continue

    # Process valid sales
    print(f"Valid Sale: Rs. {sale:,}")

    total_sales += sale
    valid_sales_count += 1

    # Count high-sales days
    if sale >= 3500:
        high_sales_days += 1


# Calculate average valid sales
if valid_sales_count > 0:
    average_sales = total_sales / valid_sales_count
else:
    average_sales = 0


# Display final report
print("\n" + "=" * 45)
print("             SALES REPORT")
print("=" * 45)

print(f"Total Days:           {len(sales)}")
print(f"Zero-Sales Days:      {zero_sales_days}")
print(f"Low-Sales Days:       {low_sales_days}")
print(f"Valid Sales Days:     {valid_sales_count}")
print(f"High-Sales Days:      {high_sales_days}")
print(f"Total Valid Sales:    Rs. {total_sales:,}")
print(f"Average Valid Sales:  Rs. {average_sales:,.2f}")

print("=" * 45)
print("Analysis completed successfully!")

