import random

run_count = 0


def generate_random_number(min_value, max_value):
    print("This is package function")
    global run_count
    run_count += 1
    return random.randint(min_value, max_value)


def generate_random_float(min_value, max_value):
    print("This is package function")
    global run_count
    run_count += 1
    return random.uniform(min_value, max_value)


if __name__ == '__main__':
    print("the package function, random_number_generator, is running.")
