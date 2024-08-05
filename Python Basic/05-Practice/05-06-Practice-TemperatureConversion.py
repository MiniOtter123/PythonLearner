while True:
    print("\nOptions:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")

    choice = input("\nEnter your choice (1-3): ")

    if choice == '3':
        break

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue

    temperature = float(input("Enter temperature value: "))

    if choice == '1':
        fahrenheit = (temperature * 9/5) + 32
        print(f"{temperature} Celsius is equal to {fahrenheit:.2f} Fahrenheit")
    elif choice == '2':
        celsius = (temperature - 32) * 5/9
        print(f"{temperature} Fahrenheit is equal to {celsius:.2f} Celsius")

print("Temperature conversion program ended. Bye!")
