# TODO 1: Income Tax Calculator
# Name: Alvie Ahmed
# Date:11/16/2026
# Description: Calculate taxable income based on gross income, number of dependents
# TODO 2: 

gross_income = float(input('Enter gross annual income: $'))
dependents = int(input('Enter number of dependants: '))

tax_rate = .20
standard_deduction = 10000
dependent_deduction = 2000 * dependents

total_deductions = dependent_deduction + standard_deduction

taxable_income = gross_income - total_deductions

income_tax = taxable_income * tax_rate


print('INCOME TAX CALCULATOR')
print('------------------------------------------\n')

print('INCOME TAX SUMMARY')
print('-------------------------------------------')
print(f'Gross Income: ${gross_income:,.2f}')
print(f'Standard Deduction: ${standard_deduction:,.2f}')
print(f'Dependent Deduction: ${dependent_deduction:,.2f}')
print(f'Total Deductions: ${total_deductions:,.2f}')
print(f'Taxable Income: ${taxable_income:,.2f}')
print(f'Tax Rate: {tax_rate * 100}%')
print(f'Estimated Income Tax: ${income_tax:,.2f}')

# REFLECTION QUESTIONS
# --------------------

# 1. Why must gross income be converted to float data type?

#    Gross income must be converted to float because it is a moneteary value
#    which might include decimal values.

# 2. Why is the number of dependents converted to an int data type?

#    Dependants is converted to an integer because it is keeping count of
#    people. This can only be a whole number.

# 3. What is the purpose of the .2f format specifier in an f-string?

#   .2f tells the output to showcase up to the first two decimal points
