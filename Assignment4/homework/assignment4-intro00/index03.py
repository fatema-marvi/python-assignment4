def main():
    print("Twemperature in farheheit! :")
    farheheit = float(input("Enter temperature in farheheit: "))
    celsius = (farheheit - 32) * 5 / 9
    print("Temperature in celsius is: " + str(celsius) + ".")

# This line should be at the same indentation level as the main() function
if __name__ == "__main__":
    main()
