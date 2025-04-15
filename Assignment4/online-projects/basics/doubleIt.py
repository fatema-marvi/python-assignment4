def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))

    # Double and print values until curr_value is 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")

# Call the main function to run the program
main()
