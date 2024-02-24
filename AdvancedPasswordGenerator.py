import secrets
import string
import hashlib

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def hash_password(password):
    # Use a strong hashing algorithm like SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))

    if password_length < 16:
        print("Warning: Passwords shorter than 16 characters may be less secure.")

        proceed = input("Do you still want to proceed? (y/n): ").lower()
        if proceed != 'y':
            print("Password generation aborted.")
            exit()

    generated_password = generate_password(length=password_length)
    hashed_password = hash_password(generated_password)

    print("Generated Password:", generated_password)
    print("Hashed Password:", hashed_password)
