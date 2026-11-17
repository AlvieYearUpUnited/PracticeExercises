# Alvie Ahmed
# 11/10/2026

# Inclass Practice 1

student1 = 'Moses Jura'
student2 = 'Ardita Mrapshtija'

print (f'My two classmates are ' + student1 + ', and ' + student2 + '.') 

print (f"My two classmates are {student1}, and {student2}.")

# ----------------------------------------------------------------------------

item1 = 25.75
item2 = 45.67
item3 = 45.75
item4 = 55.67
item5 = 45.60

subtotal = item1 + item2 + item3 + item4 + item5

tax = 15.29

total_cost = subtotal + tax

print (f'Sub-Total = {subtotal}')
print (f'Tax = {tax}')
print (f'Total Cost = {total_cost}')

# ----------------------------------------------------------------------------

c_temp = 30

f_temp = (9 / 5) * c_temp + 32

print (f'{c_temp} degrees Celsius is equivalent to {f_temp:.2f} degrees Fahrenheit.')

# ---------------------------------------------------------------------------

mealcost = float(input('Enter the cost of the meal: $'))
tip = mealcost * .20
tax = mealcost * .0825

total = mealcost + tip + tax

print ('\n----- Meal Cost Breakdown -----')
print (f'Meal Cost:      $ {mealcost:.2f}')
print (f'Tip (20%):      $ {tip:.2f}')
print (f'Tax (8.25%):    $ {tax:.2f}')

print ('-----------------------')
print (f'Total Cost:      $ {total:.2f}')
    


