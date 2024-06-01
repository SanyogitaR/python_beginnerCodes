menu = {
    'pizza': 40,
    'pasta': 45,
    'maggi': 30,
    'coke': 20,
    'salad': 70,
    'oats': 50,
}

print("WELCOME TO OUR RESTAURANT")
print('pizza: 40\npasta: 45\nmaggi: 30\ncoke: 20\nsalad: 70\noats: 50')

order_total = 0

while True:
    item = input('Enter the name of the item you want to order: ')
    
    if item in menu:
        quantity = int(input(f"How much {item} would you like to order? "))
        order_total += (menu[item] * quantity)
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Ordered item {item} is not available yet.")
    
    another_order = input("Do you want to add another item? (yes/no): ").lower()
    
    if another_order != "yes":
        break

print(f"The total amount to pay is {order_total}")
