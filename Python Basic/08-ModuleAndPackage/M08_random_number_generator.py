import random

run_count = 0


def generate_random_number(min_value, max_value):
    print("This is module function")
    global run_count
    run_count += 1
    return random.randint(min_value, max_value)


def generate_random_float(min_value, max_value):
    print("This is module function")
    global run_count
    run_count += 1
    return random.uniform(min_value, max_value)


if __name__ == '__main__':
    print("The module function, random_number_generator, is running.")

