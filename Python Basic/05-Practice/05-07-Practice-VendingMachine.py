vending_machine = {
    "1": {"item": "Cola", "price": 1.50},
    "2": {"item": "Chips", "price": 1.00},
    "3": {"item": "Candy", "price": 0.75},
    "4": {"item": "Water", "price": 1.25}
}
balance = 0
available_coins = [0.25, 0.5, 1, 2, 5]

while True:
    print("\nVending Machine Items:")
    for key, value in vending_machine.items():
        print(f"{key}: {value['item']} - ${value['price']:.2f}")

    print(f"\nCurrent Balance: ${balance:.2f}")

    action = input("\nEnter 'i' to insert money, 's' to select an item, or 'q' to quit: ")

    if action == 'q':
        break
    elif action == 'i':
        while True:
            try:
                coin = float(input("Insert coin (0.25, 0.5, 1, 2, 5): "))
                if coin in available_coins:
                    balance += coin
                    break
                else:
                    print("Invalid coin. Please insert a valid coin.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif action == 's':
        # Select item
        item_selection = input("Enter item number to purchase: ")
        if item_selection in vending_machine:
            item_price = vending_machine[item_selection]["price"]
            if balance >= item_price:
                print(f"You have purchased {vending_machine[item_selection]['item']} for ${item_price:.2f}. Enjoy!")
                balance -= item_price
            else:
                print("Insufficient balance. Please insert more money.")
        else:
            print("Invalid item selection. Please enter a valid item number.")
    else:
        print("Invalid action. Please enter 'i', 's', or 'q'.")

print("Thank you for using the vending machine. Have a great day!")
