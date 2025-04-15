PROMPT: str = "What do you want? "
JOKES: list = [
    "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'",
    "Why do programmers hate nature? It has too many bugs.",
    "There are only 10 kinds of people in this world: those who understand binary and those who don’t.",
    "Why did the developer go broke? Because he used up all his cache."
]
SORRY: str = "Sorry, I only tell jokes."

def main():
    while True:
        user_input = input(PROMPT).strip().lower()
        
        if "joke" in user_input:
            # Pop a joke from the list, or repeat the last one if empty
            if JOKES:
                print(JOKES.pop(0))
            else:
                print("I'm out of jokes for now!")
        elif "bye" in user_input or "exit" in user_input:
            print("Goodbye! Come back for more laughs!")
            break
        else:
            print(SORRY)

if __name__ == "__main__":
    main()
