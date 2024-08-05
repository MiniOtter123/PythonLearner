string_items = "Hello"
list_items = [1, 2, 3, 4, 5]
tuple_items = (1, 2, 3, 4, 5)
set_items = {1, 2, 3, 4, 5}
dict_items = {"name": "John", "age": 30, "city": "New York"}

# 1. For loop
print("===[1. For loop]===")

# Example A: Iterate over a string using a for loop
print("***[Example A: Iterate over a string using a for loop]***")

for item in string_items:
    print(item, end=" ")
print(end="\n")

# Example B: Iterate over a list using a for loop
print("***[Example B: Iterate over a list using a for loop]***")

for item in list_items:
    print(item, end=" ")
print(end="\n")

# Example C: Iterate over a tuple using a for loop
print("***[Example C: Iterate over a tuple using a for loop]***")

for item in tuple_items:
    print(item, end=" ")
print(end="\n")

# Example D: Iterate over a set using a for loop
print("***[Example D: Iterate over a set using a for loop]***")

for item in set_items:
    print(item, end=" ")
print(end="\n")

# Example E: Iterate over a dictionary using a for loop
print("***[Example E: Iterate over a dictionary using a for loop]***")

for key, value in dict_items.items():
    print(f"{key}: {value}")
print(end="\n")

# 2. while loop
print("===[2. while loop]===")

# Example F: Iterate over a string using a while loop
print("***[Example F: Iterate over a string using a while loop]***")

index = 0
while index < len(string_items):
    item = string_items[index]
    print(item, end=" ")
    index += 1
print(end="\n")

# Example G: Iterate over a list using a while loop
print("***[Example G: Iterate over a list using a while loop]***")

index = 0
while index < len(list_items):
    item = list_items[index]
    print(item, end=" ")
    index += 1
print(end="\n")

# Example H: Iterate over a tuple using a while loop
print("***[Example H: Iterate over a tuple using a while loop]***")

index = 0
while index < len(tuple_items):
    item = tuple_items[index]
    print(item, end=" ")
    index += 1
print(end="\n")

# Example I: Iterate over a set using a while loop
print("***[Example I: Iterate over a set using a while loop]***")

index = 0
list_set_items = list(set_items)
while index < len(list_set_items):
    item = list_set_items[index]
    print(item, end=" ")
    index += 1
print(end="\n")

# Example J: Iterate over a dictionary using a while loop
print("***[Example J: Iterate over a dictionary using a while loop]***")

index = 0
while index < len(dict_items.items()):
    key, value = list(dict_items.items())[index]
    print(f"{key}: {value}", end=" ")
    index += 1
print(end="\n")

# 3. Break and Continue statement
print("===[3. Break and Continue]===")

# Example K: Break statement
print("***[Example K: Break statement]***")

for item in list_items:
    if item == 3:
        break
    print(item, end=" ")
print(end="\n")

# Example L: Continue statement
print("***[Example L: Continue statement]***")

for item in list_items:
    if item == 3:
        continue
    print(item, end=" ")
print(end="\n")
