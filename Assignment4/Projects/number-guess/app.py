import random

def main():
    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (1-100): ")

        # Check if input is valid
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} tries!")
            break

if __name__ == "__main__":
    main()
