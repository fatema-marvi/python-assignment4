import random
import string

def generate_password(length):
    # Define the characters we want to include
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter password length: "))
        if length < 4:
            print("Password should be at least 4 characters long.")
            return

        password = generate_password(length)
        print(f"🔐 Your new password is: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
