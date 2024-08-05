# Module
print("===[Module]===")

# Using import
import M08_random_number_generator

print(M08_random_number_generator.generate_random_number(1, 100))
print(M08_random_number_generator.generate_random_float(0.0, 1.0))

# Using from
from M08_random_number_generator import generate_random_number, generate_random_float

print(generate_random_number(1, 100))
print(generate_random_float(0.0, 1.0))

from M08_random_number_generator import *

print(generate_random_number(1, 100))
print(generate_random_float(0.0, 1.0))


print("run_count in module:", M08_random_number_generator.run_count)

if __name__ == '__main__':
    print("__main__ is running.")

# Package
print("===[Package]===")

# Using import
import tools.random_number_generator

print(tools.random_number_generator.generate_random_number(1, 100))
print(tools.random_number_generator.generate_random_float(0.0, 1.0))

# Using from
from tools.random_number_generator import generate_random_number, generate_random_float

print(generate_random_number(1, 100))
print(generate_random_float(0.0, 1.0))

from tools.random_number_generator import *

print(generate_random_number(1, 100))
print(generate_random_float(0.0, 1.0))

print("run_count in package:", tools.random_number_generator.run_count)
