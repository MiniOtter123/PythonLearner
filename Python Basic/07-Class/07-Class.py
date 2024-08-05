# 1. Class
print("\n===[1. Class]===")


class Person1:
    pass


p1 = Person1()

# 2. Class and instance variables
print("\n===[2. Class and instance variables]===")


class Person2:
    # Class variable
    count = 0

    def __init__(self, first_name, last_name, age):
        # Instance variable
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person2.count += 1

    def fullname(self):
        return self.first_name + self.last_name

    def say_hello(self):
        print(f"My name is {self.fullname()}")


p1 = Person2('Mini', 'Otter', 32)
p1.say_hello()
print("p1.age is ", p1.age)
p2 = Person2('Chris', 'Tom', 50)
print("p2.age is ", p2.age)
print(Person2.count)

# 3. Inheritance
print("\n===[3. Inheritance]===")


class Student(Person2):
    def __init__(self, first_name, last_name, age, school):
        super().__init__(first_name, last_name, age)
        self.school = school

    # Function overriding
    def say_hello(self):
        print(f"My name is {self.fullname()} and I am a student at {self.school}")


s1 = Student('Mini', 'Otter', 32, 'MIT')
s1.say_hello()
print("s1's school is ", s1.age)
print("s1's school is ", s1.school)

# 4. Multiple inheritance
print("\n===[4. Multiple inheritance]===")


class Person4:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}")


class Employee:
    def __init__(self, company):
        self.company = company

    def work(self):
        print(f"I work at {self.company}")


class Worker(Person4, Employee):
    def __init__(self, name, company, school):
        # Call Person's init
        Person4.__init__(self, name)
        # Call Employee's init
        Employee.__init__(self, company)
        self.school = school

    def work_study(self):
        print(f"I work at {self.company} and study at {self.school}")


w1 = Worker('Alice', 'Google', 'MIT')
w1.say_hello()
w1.work()
w1.work_study()

# 4.1 isinstance() and issubclass()
print("\n===[4.1 isinstance() and issubclass()]===")

is_person = isinstance(w1, Person4)
print("Is w1 instance by Person4:", is_person)

is_employee = isinstance(w1, Employee)
print("Is w1 instance by Employee:", is_employee)

is_worker_subclass_of_person = issubclass(Worker, Person4)
print("Is worker subclass by Person4:", is_worker_subclass_of_person)

is_employee_subclass_of_worker = issubclass(Employee, Worker)
print("Is employee subclass by Worker:", is_employee_subclass_of_worker)

# 5. Private variables
print("\n===[5. Private variables]===")


class Person5:

    def __init__(self, name, age):
        self.name = name
        # The name of __age will be converted to _Person5__age.
        self.__age = age

    def say_hello(self):
        print(f"My name is {self.name}. I am {self.__age} years old")


p1 = Person5('Otter', 32)
print(p1.name)
print(p1._Person5__age)
# print(p1.__age)
p1.say_hello()

