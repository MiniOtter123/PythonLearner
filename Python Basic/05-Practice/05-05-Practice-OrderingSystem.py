menu = {
    "1": {"item": "Burger", "price": 5.99},
    "2": {"item": "Pizza", "price": 8.99},
    "3": {"item": "Salad", "price": 6.49},
    "4": {"item": "Fries", "price": 2.49},
    "5": {"item": "Soda", "price": 1.99}
}

order = []

while True:
    print("\nMenu:")
    for key, value in menu.items():
        print(f"{key}: {value['item']} - ${value['price']}")

    choice = input("\nEnter item number to add to order (or 'q' to finish): ")

    if choice.lower() == 'q':
        break

    if choice not in menu.keys():
        print("Invalid choice. Please select a valid item number.")
        continue

    chosen_item = menu[choice]
    order.append(chosen_item)
    print(f"{chosen_item['item']} added to your order.")

if order:
    print("\nYour order:")
    total = 0
    for item in order:
        print(f"{item['item']} - ${item['price']}")
        total += item['price']
    print(f"Total: ${total:.2f}")
else:
    print("No items ordered. Thank you for visiting!")
