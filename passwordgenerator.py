import random
import string

def generate_password(length):
    # Define characters for password generation
    characters = string.ascii_letters + string.digits 

    # Generate a random password using specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        # Prompt the user for the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        
        # Check if the length is greater than 0
        if length > 0:
            # Generate and display the password
            password = generate_password(length)
            print("Generated Password:", password)
        else:
            print("Please enter a valid password length (greater than 0).")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
