# SecureStringEncryptor

`SecureStringEncryptor` is a simple yet powerful console-based application designed to securely encrypt and decrypt text using a password. This program is ideal for anyone who needs to protect sensitive information with encryption and wants a straightforward tool to do so.

## Features

- **Encrypt any text**: Convert your plain text into a secure encrypted string.
- **Decrypt encrypted text**: Recover the original text using the correct password.
- **User-friendly console interface**: The application runs in a loop, allowing you to encrypt and decrypt as many strings as needed.
- **Password-protected encryption**: Uses the password you provide to generate a unique encryption key.

## How It Works

1. **Encryption**: The program takes your plain text and a password, then uses the password to generate an encryption key. The text is encrypted using this key and can only be decrypted with the same password.

2. **Decryption**: To decrypt an encrypted string, you must provide the same password used during encryption. If the password matches, the original text is recovered.

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You will also need the `cryptography` package. Install it using pip:

```bash
pip install cryptography
```

### Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/Sez-A/SecureStringEncryptor.git
    cd SecureStringEncryptor
    ```

2. Run the program:
    ```bash
    python3 secure_string_encryptor.py
    ```

3. Follow the on-screen instructions to encrypt or decrypt text.

### Example

```bash
Choose an option:
1. Encrypt a string
2. Decrypt a string
3. Exit
Enter your choice (1/2/3): 1
Enter the string to encrypt: This is a secret message.
Enter the password: mysecurepassword
Encrypted Text: gAAAAABf1...

Choose an option:
1. Encrypt a string
2. Decrypt a string
3. Exit
Enter your choice (1/2/3): 2
Enter the encrypted string: gAAAAABf1...
Enter the password: mysecurepassword
Decrypted Text: This is a secret message.
```

## Legal Disclaimer

**NOTE**: This program is provided "as is", without warranty of any kind, express or implied. Use it at your own risk. The authors of `SecureStringEncryptor` are not responsible for any damage, loss, or legal issues that arise from the use of this program. Always ensure you are using encryption responsibly and in accordance with applicable laws.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Sez-A/SecureStringEncryptor/blob/master/LICENSE) file for details.
