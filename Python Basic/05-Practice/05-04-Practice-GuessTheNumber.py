while True:
    secret_number = int(input("Chairman, please enter a secret number (between 0 and 99): "))
    if 0 <= secret_number <= 99:
        print("The chairman has set a secret number.")
        break
    else:
        print("Please enter a number between 0 and 99. Please enter again.")

min_guess = 0
max_guess = 99

while True:
    print(f"Guess between {min_guess} and {max_guess}.")
    guess = int(input("Player, please guess a number: "))

    if guess < min_guess or guess > max_guess:
        print(f"Please enter a number between {min_guess} and {max_guess}. Please guess again.")
        continue

    if guess < secret_number:
        print("The secret number is greater than your guess.")
        min_guess = max(min_guess, guess + 1)
    elif guess > secret_number:
        print("The secret number is less than your guess.")
        max_guess = min(max_guess, guess - 1)
    else:
        print(f"Congratulations! You guessed the secret number {secret_number}.")
        break
