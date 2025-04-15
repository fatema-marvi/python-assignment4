import random

NUM_ROUNDS = 5  # You can change this to play more or fewer rounds

def get_user_guess():
    """Prompt user until they enter 'higher' or 'lower'"""
    while True:
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        if guess in ["higher", "lower"]:
            return guess
        print("Please enter either 'higher' or 'lower'.")

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {user_number}")
        user_guess = get_user_guess()

        correct = False
        if user_guess == "higher" and user_number > computer_number:
            correct = True
        elif user_guess == "lower" and user_number < computer_number:
            correct = True

        if correct:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}")
        print()  # Blank line between rounds

    # Final message
    print("Thanks for playing!")
    print(f"Your final score is {score} out of {NUM_ROUNDS}")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Run the game
main()
