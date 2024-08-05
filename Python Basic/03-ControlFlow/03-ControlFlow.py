# 1. Comparison Operators
print("===[1. Comparison Operators]===")

is_equal = 10 == 20
is_not_equal = 10 != 20
smaller_than = 10 < 20
less_than_or_equal = 10 <= 20
greater_than = 10 > 20
greater_than_or_equal = 10 >= 20
print("is_equal: ", is_equal)
print("is_not_equal: ", is_not_equal)
print("smaller_than: ", smaller_than)
print("less_than_or_equal: ", less_than_or_equal)
print("greater_than: ", greater_than)
print("greater_than_or_equal: ", greater_than_or_equal)

# 2. Logical Operators
print("===[2. Logical Operators]===")

x = True
y = False
is_both_true = x and y
is_either_true = x or y
is_x_false = not x
print(is_both_true)
print(is_either_true)
print(is_x_false)

# 3. if Statement
print("===[3. if Statement]===")

# Example A: Checking Adulthood
print("***[Example A: Checking Adulthood]***")

age = int(input("Please enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
# 4. elif Statements
print("===[4. elif Statements]===")

# Example B: Grading Evaluation
print("***[Example B: Grading Evaluation]***")
grade = input("Please enter your letter grade (A, B, C, D, or F): ")
if grade == "A":
    print("Excellent!")
elif grade == "B":
    print("Very Good!")
elif grade == "C":
    print("Average")
elif grade == "D":
    print("Pass")
else:
    print("Invalid grade. Please enter A, B, C, D, or F.")

