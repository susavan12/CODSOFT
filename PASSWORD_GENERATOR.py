import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for better security.")
        return ""
    characters = string.ascii_letters + string.digits + string.punctuation    # All possible characters
    password = [                              # Ensure the password contains at least one lowercase, one uppercase, one digit, and one symbol
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    password += random.choices(characters, k=length - 4) # Fill the rest of the password length with random choices
    random.shuffle(password)# Shuffle the result to avoid predictable placement
    return ''.join(password)
try:
    user_length = int(input("Enter the password length: "))# Prompt user for input
    generated_password = generate_password(user_length)
    if generated_password:
        print("Generated Password:", generated_password)
except ValueError:
    print("Please enter a valid number.")