


#name = input('Enter your name: ')
#monthly_salary = float(input('Enter your monthly salary: '))

# if monthly_salary >= 5000:
#    print(f'{name}, you are eligible for a bonus')

# print('Done!')

# --------------------------------------------------------


# name = input('Enter employee name: ')
# score = float(input('Enter performance score: '))
# print()

# if score >= 80:
#    category = 'Excellent Performance'

# else:
#    category = 'Needs Improvement'

# print (f'Employee Name: {name}')
# print (f'Performance Score: {score}')
# print (f'Performance Category: {category}')


# ---------------------------------------------------------

name = input('Enter employee name: ')
score = int(input('Enter performance score: '))

if score >= 90:
    rating = 'Outstanding'
elif score >= 80:

    rating = 'Exceeds Expecations'
elif score >= 70:

    rating = 'Meets Expectations'
elif score >= 60:

    rating = 'Below Expectation'
else:
    rating = 'Unsatisfactory'

print (f'Employee Name: {name}')
print (f'Performance Score: {score}')
print (f'Rating: {rating}')

