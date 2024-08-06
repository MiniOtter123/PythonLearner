# 1. Iterator
print("===[1. Iterator]===")

# 1.1 Simple iterator
print("===[1.1 Simple iterator]===")

mydata = [1, 2, 3, 4]
iterator = iter(mydata)

while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        print("StopIteration")
        break


# 1.2 Class Iterator
print("===[1.2 Class Iterator]===")


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            print("StopIteration")
            raise StopIteration


my_iter = MyIterator(mydata)

for item in my_iter:
    print(item)

# 2. Generator
print("===[2. Generator]===")

# 2.1 Simple generator
print("===[2.1 Simple generator]===")


def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4


for item in my_generator():
    print(item)

# 2.2 Generator function
print("===[2.2 Generator function]===")


def my_generator_function(start, end):
    index = start
    while index < end:
        yield index
        index += 1


for num in my_generator_function(0, 10):
    print(num)

# 2.3 Range()
print("===[2.3 Range()]===")

for num in range(0, 10):
    print(num)

