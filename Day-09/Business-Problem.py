# ============================================================
# DAY 09 - BUSINESS PROBLEM
# Project: Sales Performance Analyzer
# 30 Days Python Challenge for Data Analytics
# File: Business-Problem.py
# ============================================================

# BUSINESS PROBLEM:
# A company wants to analyze its sales performance.
#
# The program should:
# 1. Accept product name, sales amount, and sales target.
# 2. Compare sales with the target.
# 3. Classify sales performance.
# 4. Calculate achievement percentage.
# 5. Display a business report.


# STEP 1: INPUT DATA

product_name = input("Enter product name: ")
sales = float(input("Enter total sales amount (Rs.): "))
target = float(input("Enter sales target (Rs.): "))


# STEP 2: VALIDATE INPUT

if sales < 0 or target < 0:
    print("\nError: Sales and target cannot be negative.")

elif target == 0:
    print("\nError: Sales target must be greater than zero.")

else:

    # STEP 3: CALCULATE ACHIEVEMENT

    achievement = (sales / target) * 100

    # STEP 4: CLASSIFY PERFORMANCE

    if sales >= target * 1.5:
        performance = "Outstanding Performance"

    elif sales >= target:
        performance = "Target Achieved"

    elif sales >= target * 0.75:
        performance = "Needs Improvement"

    else:
        performance = "Poor Performance"

    # STEP 5: CALCULATE DIFFERENCE

    if sales >= target:
        difference = sales - target
        difference_status = "Above Target"

    else:
        difference = target - sales
        difference_status = "Below Target"

    # STEP 6: DISPLAY BUSINESS REPORT

    print("\n================================")
    print("     SALES PERFORMANCE REPORT")
    print("================================")

    print("Product Name:", product_name)
    print("Total Sales: Rs.", round(sales, 2))
    print("Sales Target: Rs.", round(target, 2))
    print("Target Achievement:", round(achievement, 2), "%")
    print("Performance:", performance)
    print(difference_status + " Amount: Rs.", round(difference, 2))

    print("================================")


# ============================================================
# END OF DAY 09 - BUSINESS PROBLEM
# ============================================================