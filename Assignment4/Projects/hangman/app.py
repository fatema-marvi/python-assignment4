import random

# List of words to choose from
WORDS = ["python", "hangman", "developer", "keyboard", "laptop", "program", "debug"]

def main():
    print("🪓 Welcome to Hangman!")
    word = random.choice(WORDS)
    guessed_letters = []
    tries = 6  # Number of lives

    print("_ " * len(word))  # Display blank spaces

    while tries > 0:
        guess = input("\nGuess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
        else:
            tries -= 1
            print(f"❌ Nope! {tries} tries left.")

        # Display the word with blanks and correct guesses
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())

        # Check for win
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You guessed the word! You win!")
            break
    else:
        print(f"\n💀 You're out of tries! The word was '{word}'. Better luck next time!")

if __name__ == "__main__":
    main()
