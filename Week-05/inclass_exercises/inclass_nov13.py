

day = 1

monday = 1200
tuesday = 1500
wednesday = 1100
thursday = 1800
friday = 1400

total_sales = 0

""" 
while day <= 5:

    if day == 1:
        total_sales = total_sales + monday
        
    elif day == 2:
        total_sales = total_sales + tuesday
        

    elif day == 3:
        total_sales = total_sales + wednesday
        
    elif day == 4:
        total_sales = total_sales + thursday
        

    else:
        total_sales = total_sales + friday

    day += 1

average_sales = total_sales / 5

print(f'Total Sales: {total_sales:,.2f}')
print(f'Average Sales: {average_sales:,.2f}')

"""

for day in range(5):

    if day == 1:
        total_sales = total_sales + monday
            
    elif day == 2:
        total_sales = total_sales + tuesday
            
    
    elif day == 3:
        total_sales = total_sales + wednesday
            
    elif day == 4:
        total_sales = total_sales + thursday
            
    else:
        total_sales = total_sales + friday
    
    day += 1
    
    average_sales = total_sales / 5
    
print(f'Total Sales: {total_sales:,.2f}')
print(f'Average Sales: {average_sales:,.2f}')





