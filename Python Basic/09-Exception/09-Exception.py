
# 1. Syntax error
print("===[1. Syntax error]===")

# 2. Exceptions
print("===[2. Exceptions]===")

# 2.1 Handling exceptions
print("===[2.1 Handling exceptions]===")

try:
    open("nonexistent.txt")
except FileNotFoundError as e:
    print(f"file not found{e.filename}")
except Exception as e:
    print(f"other exceptions{e}")
finally:
    print("This is finally section")

# 2.2 The raise keyword
print("===[2.2 The raise keyword]===")


def is_even(number):
    if number % 2 != 0:
        raise ValueError("Number must be even")


try:
    is_even(5)
except ValueError as e:
    print(e)

# 2.3 Exception chaining
print("===[2.3 Exception chaining]===")

def open_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        raise OSError(f"Unable to open file: {filename}")


try:
    content = open_file("nonexistent.txt")
except OSError as e:
    print(f"Error: {e}")


# 2.4 Custom exceptions
print("===[2.--- Custom exceptions]===")


class QuitInputError(ValueError):
    pass


def is_even2(number):
    if number == "q":
        raise QuitInputError("Input 'q'")
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    if number % 2 != 0:
        raise ValueError("Number must be even")


try:
    is_even2(4)
    print("4 is even")
    is_even2(5)
except QuitInputError:
    print("User canceled input.")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

try:
    is_even2("q")
except QuitInputError:
    print("User canceled input.")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

