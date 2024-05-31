menu={
    'pizza':40,
    'pasta':45,
    'maggi':30,
    'coke':20,
    'salad':70,
    'oats':50,
}
print("WELCOME TO OUR RESTAURANT")
print('pizza:40\npasta:45\nmaggi:30\ncoke:20\nsalad:70\noats:50')
order_total=0

item_1=input('Enter the name of item you want to order=')
quantity=int(input(f"how much {item_1} you would like to order "))
if item_1 in menu:
    order_total +=(menu[item_1]*quantity)
    print(f"Your item{item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available yet")

another_order=input("Do you want to add another item? (yes/no)")
Another_order=another_order.lower()
if Another_order =="yes":
    item_2=input("Enter the name of second item=")
    quantity_2=int(input(f"how much {item_2} you would like to order "))
    if item_2 in menu:
        order_total +=(menu[item_2]*quantity_2)
        print(f"Item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available!")



print(f"The total amount of items  to pay is {order_total}")



