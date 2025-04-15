import random

NUM_SIDES = 6

def roll_dice():
    """Simulate rolling two dice and return the result."""
    die1: int = random.randint(1, NUM_SIDES)
    die2: int  = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:" , total )

def main():
    die1: int = 10
    print("die1 in main() starts as:" + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() ends as:" + str(die1))
if __name__ == "__main__":
    main()