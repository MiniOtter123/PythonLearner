# 1. Lists: Mutable Ordered Collections
print("***[1. Lists]***")

# 1.1 Creating Lists
print("===[1.1 Creating Lists]===")

my_list = []
print(type(my_list))
print(my_list)

numbers_list = [1, 2, 3, 4, 5]
print(type(numbers_list))
print(numbers_list)

names_list = ["Alice", "Bob", "Charlie"]
print(type(names_list))
print(names_list)

mixed_list = [1, "Hello", 3.14, True]
print(type(mixed_list))
print(mixed_list)

# 1.2 Accessing List Elements
print("===[1.2 Accessing List Elements]===")

first_number = numbers_list[0]
print(first_number)

last_name = names_list[-1]
print(last_name)

second_last_item = mixed_list[-2]
print(second_last_item)

# 1.3 Modifying List Elements
print("===[1.3 Modifying List Elements]===")

numbers_list[0] = 10
print(numbers_list)

names_list[1] = "David"
print(names_list)

# 1.4 Adding Elements to Lists
print("===[1.4 Adding Elements to Lists]===")

numbers_list.append(6)
print(numbers_list)

names_list.append("Emily")
print(names_list)

# 1.5 Removing Elements from Lists
print("===[1.5 Removing Elements from Lists]===")

names_list.remove("David")
print(names_list)

# 1.6 Finding the Length of a List
print("===[1.6 Finding the Length of a List]===")

numbers_list_length = len(numbers_list)
print(numbers_list_length)

names_list_length = len(names_list)
print(names_list_length)

# 2. Tuples: Immutable Ordered Collections
print("***[2. Tuples]***")

# 2.1 Creating Tuples
print("===[2.1 Creating Tuples]===")

my_tuple = ()
print(type(my_tuple))
print(my_tuple)

numbers_tuple = (1, 2, 3, 4, 5)
print(type(numbers_tuple))
print(numbers_tuple)

names_tuple = ("Alice", "Bob", "Charlie")
print(type(names_tuple))
print(names_tuple)

mixed_tuple = (1, "Hello", 3.14, True)
print(type(mixed_tuple))
print(mixed_tuple)

# 2.2 Accessing Elements in Tuples
print("===[2.2 Accessing Elements in Tuples]===")

first_number = numbers_tuple[0]
print(first_number)

last_name = names_tuple[-1]
print(last_name)

second_last_item = mixed_tuple[-2]
print(second_last_item)

# 2.3 Modifying Tuples (Not Allowed)
print("===[2.3 Modifying Tuples]===")

# numbers_tuple[0] = 10
# print(numbers_tuple)

# 3. Dictionaries: Key-Value Pair Collections
print("***[3. Dictionaries]***")

# 3.1 Creating Dictionaries
print("===[3.1 Creating Dictionaries]===")

my_dict = {}
print(type(my_dict))
print(my_dict)

numbers_dict = {"one": 1, "two": 2, "three": 3}
print(type(numbers_dict))
print(numbers_dict)

mixed_dict = {"name": "Alice", "age": 30,
              "hobby": "programming"}
print(type(mixed_dict))
print(mixed_dict)

# 3.2 Accessing Dictionary Values
print("===[3.2 Accessing Dictionary Values===")

first_number = numbers_dict["one"]
print(first_number)

age = mixed_dict["age"]
print(age)

# 3.3 Adding Key-Value Pairs to Dictionaries
print("===[3.3 Adding Key-Value Pairs to "
      "Dictionaries]===")

numbers_dict["four"] = 4
print(numbers_dict)

mixed_dict["city"] = "Taipei"
print(mixed_dict)

# 3.4 Checking if a Key Exists in a Dictionary
print("===[3.4 Checking if a Key Exists in a "
      "Dictionary]===")

key_exists = "three" in numbers_dict
print(key_exists)

key_exists = "hobby" in mixed_dict
print(key_exists)

# 3.5 Removing Key-Value Pairs from Dictionaries
print("===[3.5 Removing Key-Value Pairs from "
      "Dictionaries]===")

del numbers_dict["two"]
print(numbers_dict)

del mixed_dict["city"]
print(mixed_dict)

# 4. Sets: Unordered Collections of Unique Elements
print("***[4. Set]***")

# 4.1 Creating Sets
print("===[4.1 Creating Sets]===")

my_set = set()
print(type(my_set))
print(my_set)

numbers_set = {1, 2, 3, 4, 5}
print(type(numbers_set))
print(numbers_set)

names_set = {"Alice", "Bob", "Charlie"}
print(type(names_set))
print(names_set)

# 4.2 Checking if an Element Exists in a Set
print("===[4.2 Checking if an Element Exists "
      "in a Set]===")

element_exists = 3 in numbers_set
print(element_exists)

element_exists = "Charlie" in names_set
print(element_exists)

# 4.3 Adding Elements to Sets
print("===[4.3 Adding Elements to Sets]===")

numbers_set.add(6)
print(numbers_set)

names_set.add("David")
print(names_set)

# 4.4 Removing Elements from Sets
print("===[4.4 Removing Elements from Sets]===")

numbers_set.remove(4)
print(numbers_set)

names_set.remove("Bob")
print(names_set)

# 4.5 Set Operations: Intersection, Difference, and Union
print("===[4.5 Set Operations]===")

intersection = numbers_set.intersection(names_set)
print(intersection)

difference = numbers_set.difference(names_set)
print(difference)

union = numbers_set.union(names_set)
print(union)
