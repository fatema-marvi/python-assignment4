def main():
    print("Welcome to Mad Libs! Fill in the blanks below. Let's make a funny story!\n")

    # Collect words from the user
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    place = input("Enter a place: ")
    adverb = input("Enter an adverb: ")
    emotion = input("Enter an emotion: ")
    silly_word = input("Enter a silly word: ")

    # Construct the story
    print("\nHere's your Mad Lib story:\n")
    print(f"One day, a {adjective} {noun} {verb} through the {place} {adverb}.")
    print(f"Everyone who saw it felt very {emotion}.")
    print(f"Suddenly, someone shouted, '{silly_word.upper()}!' and the adventure continued...\n")
    print("Thanks for playing Mad Libs!")

if __name__ == "__main__":
    main()
