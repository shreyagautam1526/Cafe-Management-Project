menu = {"Pizza":80,
        "Salad":40,
        "Coffee":50,
        "Icecream":25,
        "Burger":50}

# Greet
print("!!!Welcome to Pylance Cafe!!!")
print(menu,sep='\n')

# Asking user to order
item1 = input("Enter the item name:")

order_total = 0

if item1 in menu:
    order_total += menu[item1]
    print(f"Your item {item1} has been added")

else:
    print("Sorry! Ordered item is not available yet.")

another_order = input("Do you want to add another item (Yes/No)?:")
if another_order == "Yes":
    item_2 = input("Enter the item 2 name:")
    if item_2 in menu:
     order_total += menu[item_2]
     print(f"Your item {item_2} has been added.")
     print(f"Your total bill is:",order_total)
    else:
       print(f"Ordered item is not available yet.")
else:
   print(f"Your total ordered bill is:", order_total)







         


 