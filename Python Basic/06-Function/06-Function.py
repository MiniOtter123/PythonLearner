# 1. Defining a Function
print("\n===[1. Defining a Function]===")


def function_name():
    pass


function_name()

# 2. Variable scope
print("\n===[2. Variable scope]===")

global_variable = 50


def local_global():
    global global_variable
    local_variable = 10
    print(local_variable, "in which function is local_global()")
    print(global_variable, "in which function is local_global()")
    global_variable = 12
    print(global_variable, "in which function is local_global()")
    return local_variable


local = local_global()
# print(local_variable)
print(local, "in which function is main")
print(global_variable, "in which function is main")


# 3. Positional Arguments
print("\n===[3. Positional Arguments]===")


def greet_position(firstname, lastname):
    print("Hello,", firstname + " " + lastname)


greet_position("Mini", "Otter")


# 4. Default Arguments
print("\n===[4. Default Arguments]===")


def greet_default(firstname, lastname, greeting="Welcome to my house"):
    print("Hello,", firstname + " " + lastname, ".", greeting)


greet_default("Mini", "Otter")

# 5. Keyword Arguments
print("\n===[5. Keyword Arguments]===")

greet_default(lastname="Otter", firstname="Mini")


# 6. Special Arguments
print("\n===[6. Special Arguments]===")

# 6.1 *args: Arbitrary Positional Arguments
print("\n===[6.1 *args: Arbitrary Positional Arguments]===")


def info_tuple(firstname, lastname, *infos):
    print("First name:", firstname)
    print("Last name:", lastname)
    for info in infos:
        print(info)


info_tuple("Mini", "Otter", "Taipei", "Software Engineer")


# 6.2 **kwargs: Arbitrary Keyword Arguments
print("\n===[6.2 **kwargs: Arbitrary Keyword Arguments]===")


def info_dictionary(firstname, lastname, **details):
    print("First name:", firstname)
    print("Last name:", lastname)
    for key, value in details.items():
        print(key, ":", value)


info_dictionary("Alice", 30, city="Taipei", occupation="Software Engineer")

# 7. Lambda Expressions
print("\n===[7. Lambda Expressions]===")

lambda_function = lambda x, y: x + " " + y

result = lambda_function("Mini", "Otter")
print("Lambda definition: ", result)


def greet_lambda(firstname, lastname):
    return firstname + " " + lastname


result = greet_lambda("Mini", "Otter")
print("Function definition: ", result)
