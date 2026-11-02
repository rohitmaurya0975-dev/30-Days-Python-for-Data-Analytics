
# ==================================================
# 🐍 DAY 13 - PYTHON FUNCTIONS
# BUSINESS PROBLEM: EMPLOYEE SALARY ANALYZER
# ==================================================

# Business Scenario:
# A company wants to calculate employee salaries,
# bonuses, deductions, and final payouts using functions.


# 1. Calculate Total Salary
def calculate_total_salary(basic_salary, bonus):
    return basic_salary + bonus


# 2. Calculate Deduction
def calculate_deduction(total_salary, deduction_rate):
    return total_salary * deduction_rate / 100


# 3. Calculate Final Salary
def calculate_final_salary(total_salary, deduction):
    return total_salary - deduction


# 4. Calculate Average Salary
def calculate_average_salary(salary1, salary2, salary3):
    return (salary1 + salary2 + salary3) / 3


# ==================================================
# EMPLOYEE DATA
# ==================================================

employee1 = "Rohit"
employee2 = "Aman"
employee3 = "Priya"

basic1 = 30000
bonus1 = 5000

basic2 = 35000
bonus2 = 7000

basic3 = 40000
bonus3 = 8000

deduction_rate = 5


# ==================================================
# EMPLOYEE 1
# ==================================================

total1 = calculate_total_salary(basic1, bonus1)
deduction1 = calculate_deduction(total1, deduction_rate)
final1 = calculate_final_salary(total1, deduction1)

print("\n========== EMPLOYEE 1 ==========")
print("Name:", employee1)
print("Basic Salary: ₹", basic1)
print("Bonus: ₹", bonus1)
print("Total Salary: ₹", total1)
print("Deduction: ₹", deduction1)
print("Final Salary: ₹", final1)


# ==================================================
# EMPLOYEE 2
# ==================================================

total2 = calculate_total_salary(basic2, bonus2)
deduction2 = calculate_deduction(total2, deduction_rate)
final2 = calculate_final_salary(total2, deduction2)

print("\n========== EMPLOYEE 2 ==========")
print("Name:", employee2)
print("Basic Salary: ₹", basic2)
print("Bonus: ₹", bonus2)
print("Total Salary: ₹", total2)
print("Deduction: ₹", deduction2)
print("Final Salary: ₹", final2)


# ==================================================
# EMPLOYEE 3
# ==================================================

total3 = calculate_total_salary(basic3, bonus3)
deduction3 = calculate_deduction(total3, deduction_rate)
final3 = calculate_final_salary(total3, deduction3)

print("\n========== EMPLOYEE 3 ==========")
print("Name:", employee3)
print("Basic Salary: ₹", basic3)
print("Bonus: ₹", bonus3)
print("Total Salary: ₹", total3)
print("Deduction: ₹", deduction3)
print("Final Salary: ₹", final3)


# ==================================================
# BUSINESS SUMMARY
# ==================================================

average_salary = calculate_average_salary(
    final1, final2, final3
)

total_payout = final1 + final2 + final3

print("\n========== BUSINESS SUMMARY ==========")
print("Total Employees:", 3)
print("Total Company Payout: ₹", total_payout)
print(f"Average Final Salary: ₹{average_salary:.2f}")


# ==================================================
# 🎉 BUSINESS ANALYZER COMPLETED!
# ==================================================

