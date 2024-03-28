import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Main program
if __name__ == "__main__":
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))
    # Generate the password
    password = generate_password(length)
    # Display the password
    print(f"Generated password: {password}")
