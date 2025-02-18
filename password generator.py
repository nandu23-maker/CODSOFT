import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
length = int(input("Enter the desired password length: "))

# Generate and display password
password = generate_password(length)
if password:
    print("Generated Password:", password)
