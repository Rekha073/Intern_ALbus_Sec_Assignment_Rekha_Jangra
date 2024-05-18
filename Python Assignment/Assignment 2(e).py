import random
import string

def generate_password(length):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure each character set is included in the password
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Generate the rest of the password
    password.extend(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password to mix the characters
    random.shuffle(password)

    # Convert the password list to a string
    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print("Generated Password:", password)

