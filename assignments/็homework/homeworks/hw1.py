"""
Personal Finance Calculator
Student: Raphiphat Saenkla
Date: 7/22/2025
Purpose: Calculate monthly budget and savings
"""
income = float(input("User's monthly income in THB: "))  #รับรายได้มา
rent = float(input("Monthly rent: "))  #รับค่าเช่ามา
food = int(input("Monthly food budget in THB: "))  #รับค่าอาหารมา
transportation = float(input("Monthly transportation expenses: "))  #รับค่าเดินทาง
entertainment = int(input("Monthly entertainment budget: "))  #รับค่าพักผ่อน
emergency = float(input("Percentage to save for emergency percent: "))  #รับค่า%เงินฉุกเฉิน
investment = float(input("Percentage to invest percent: "))  #รับจำนวนเปอร์เซ็นต์ที่จะลงทุน

TotalFixed = rent+transportation  #ค่าใช้จ่ายคงที่
TotalVariable = food+entertainment  #ค่าใช้จ่ายไม่คงที่
Totalexpenses = TotalFixed+TotalVariable  #ค่าใช้จ่ายรวม
Remaining_Income = income-Totalexpenses  #เงินเหลือหลังหักค่าใช้จ่าย
Emergency_Fund_Amount = income*(emergency/100)  #เงินฉุกเฉิน
Investment_Amount = income*(investment/100)  #เงินลงทุน
Available_for_Savings = Remaining_Income-Emergency_Fund_Amount-Investment_Amount  #เงินออมสุทธิ
Expense_Ratio = (Totalexpenses/income)*100  #%ค่าใช้จ่ายต่อรายได้

print("=====MONTHLY BUDGET REPORT=====")
print(f"Income: {income:.2f} THB")
print(f"Fixed Expenses: {TotalFixed:.2f} THB")
print(f"Variable Expenses: {TotalVariable:.2f} THB")
print(f"Total Expenses: {Totalexpenses:.2f} THB")
print(f"Remaining: {Remaining_Income:.2f} THB")

print("=====SAVINGS BREAKDOWN=====")
print(f"Emergency Fund ({emergency}%): {Emergency_Fund_Amount:.2f} THB")
print(f"Investment ({investment}%): {Investment_Amount:.2f} THB")
print(f"Available for Savings: {Available_for_Savings:.2f} THB")

print("=====SUMMARY=====")
print(f"Expense Ratio: {Expense_Ratio:.2f}%")
# f หลัง print เพื่อใช้ float และประกาศ.2f เพื่อระบุจำนวนทศนิยม

