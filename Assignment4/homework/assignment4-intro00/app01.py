def main(): 
    print("This program adds two numbers.")
    num1 = input("Enter first number: ")
    num1 = int(num1)
    num2 = input("Enter second number: ")
    num2 = int(num2)
    total = num1 + num2
    print("The total is: " + str(total) + ".")


# This line should be at the same indentation level as the main() function
if __name__ == "__main__":
    main()