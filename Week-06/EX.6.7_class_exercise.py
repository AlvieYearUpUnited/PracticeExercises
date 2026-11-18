

class Product:
    # Constructor method
    def __init__(self, name, category, price, quantity):
            self.name = name
            self.category = category
            self.price = price
            self.quantity = quantity

    # Method to display formatted product report
    def display_info(self):
        print(f'Product Name: {self.name}')
        print(f'Category: {self.category}')
        print(f'Price: ${self.price:,.2f}')
        print(f'Quantity: {self.quantity}')

    def inventory_value(self):
         print(f'Inventory Value for {self.name}: ${(self.price * self.quantity):,.2f}')


name1 = input('Enter Product 1 Name: ')
category1 = input('Enter Category: ')
price1 = float(input('Enter Price: $'))
quantity1 = int(input('Enter Quantity: '))
print()
name2 = input('Enter Product 2 Name: ')
category2 = input('Enter Category: ')
price2 = float(input('Enter Price: $'))
quantity2 = int(input('Enter Quantity: '))

product1 = Product(name1, category1, price1, quantity1)
product2 = Product(name2, category2, price2, quantity2)

print(f'{product1.name}, {product1.category}, ${product1.price:,.2f}, {product1.quantity}\n')
product1.display_info()
product1.inventory_value()
print()
print(f'{product2.name}, {product2.category}, ${product2.price:,.2f}, {product2.quantity}\n')
product2.display_info()
product2.inventory_value()

    

