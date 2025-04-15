def main():
    anton : int = 21 #anton age is 21
    beth : int = 6 +anton #beth age is anton age + 6
    chen :int =20 + beth #chen age is beth age + 20
    drew : int = chen + anton #drew age is chen age + anton age
    ethan : int = chen #ethan age is chen age

    #print the ages of anton, beth, chen, drew and ethan
    print("anton age is " + str(anton) + ".")
    print("beth age is " + str(beth) + ".")         
    print("chen age is " + str(chen) + ".")
    print("drew age is " + str(drew) + ".")
    print("ethan age is " + str(ethan) + ".")

    # This line should be at the same indentation level as the main() function
if __name__ == "__main__":
    main()

