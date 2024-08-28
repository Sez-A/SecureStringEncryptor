from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password: str) -> bytes:
    """Generate a key based on the password"""
    password_bytes = password.encode('utf-8')  # Convert password to bytes
    hashed_password = hashlib.sha256(password_bytes).digest()  # Hash the password to 32 bytes
    key = base64.urlsafe_b64encode(hashed_password)  # Convert to base64 key
    return key

def encrypt_string(text: str, password: str) -> str:
    """Encrypt a string using a password"""
    key = generate_key(password)  # Generate the key from the password
    fernet = Fernet(key)  # Create a Fernet object with the key
    encrypted_text = fernet.encrypt(text.encode('utf-8'))  # Encrypt the text
    return encrypted_text.decode('utf-8')  # Return the encrypted text as a string

def decrypt_string(encrypted_text: str, password: str) -> str:
    """Decrypt an encrypted string using a password"""
    try:
        key = generate_key(password)  # Generate the key from the password
        fernet = Fernet(key)  # Create a Fernet object with the key
        decrypted_text = fernet.decrypt(encrypted_text.encode('utf-8')).decode('utf-8')  # Decrypt the text
        return decrypted_text
    except Exception as e:
        return f"Decryption failed: {str(e)}"

def main():
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a string")
        print("2. Decrypt a string")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter the string to encrypt: ")
            password = input("Enter the password: ")
            encrypted_text = encrypt_string(text, password)
            print(f"Encrypted Text: {encrypted_text}")

        elif choice == '2':
            encrypted_text = input("Enter the encrypted string: ")
            password = input("Enter the password: ")
            decrypted_text = decrypt_string(encrypted_text, password)
            print(f"Decrypted Text: {decrypted_text}")

        elif choice == '3':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

