


import statistics
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

sales = [1250, 1480, 1100, 1650, 1850,
         1420, 1700, 1300, 2100, 1950]

print('DAILY SALES REPORT')
print('------------------')

for i in range(len(days)):
    print(f'{days[i]}: ${sales[i]:,.2f}')

print(f'\nAverage:              ${statistics.mean(sales):,.2f}')
print(f'Median:               ${statistics.median(sales):,.2f}')
print(f'Mode:                 ${statistics.mode(sales):,.2f}')
print(f'Standard Deviation:   ${statistics.stdev(sales):,.2f}')
print(f'Total Sales:          ${sum(sales):,.2f}')
print(f'Lowest Sales Amount:  ${min(sales):,.2f}')
print(f'Highest Sales Amount: ${max(sales):,.2f}')


if sales >= 1800:
    performance = 'Excellent'
elif sales == 


