while True:
    print("==========:")
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter '//' for integer division")
    print("Enter '%' for modulus")
    print("Enter 'q' to quit")
    print("==========:")

    operation = input("Enter operation: ")

    if operation == 'q':
        break

    if operation not in ['+', '-', '*', '/', '//', '%']:
        print("Invalid operation. Please enter one of '+', '-', '*', '/', '//', '%', or 'q'")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero!")
            continue
        else:
            result = num1 / num2
    elif operation == '//':
        if num2 == 0:
            print("Error: Division by zero!")
            continue
        else:
            result = num1 // num2
    elif operation == '%':
        if num2 == 0:
            print("Error: Division by zero!")
            continue
        else:
            result = num1 % num2

    print(f"Result: {result}")

print("Calculator program ended. Bye!")
