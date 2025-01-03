# CaesarCipher Encryption Tool

CaesarCipher is a Python-based encryption and decryption tool that implements the classic Caesar Cipher algorithm. It supports both uppercase and lowercase letters, digits, and retains non-alphanumeric characters unaltered.

---

## Features

- Encrypts and decrypts text using the Caesar Cipher algorithm.
- Handles:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Digits (0-9)
  - Non-alphanumeric characters are preserved without modification.
- Customizable shift values for encryption and decryption.

---

## How It Works

The Caesar Cipher works by shifting each character in the input text by a fixed number of places in the alphabet or digit sequence. Non-alphanumeric characters are ignored during the process.

### Example

- **Original Text**: `Hello World 1357$**`
- **Shift Value**: `10`
- **Encrypted Text**: `Rovvy 6yBvn bdfh$**`
- **Decrypted Text**: `Hello World 1357$**`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mobinic1101/CaesarCipher-Python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CaesarCipher-Python
   ```
3. Run the script:
   ```bash
   python caesar_cipher.py
   ```

---

## Usage

### Encrypt Text

Call the `encrypt` method with your input text and a shift value.

```python
from caesar_cipher import CaesarCipher

cipher = CaesarCipher()
text = "Hello World 1357"
shift = 10
encrypted = cipher.encrypt(text, shift)
print(encrypted)  # Output: Rovvy 6yBvn bdfh
```

### Decrypt Text

Call the `decrypt` method with your encrypted text and the same shift value (negative for decryption).

```python
from caesar_cipher import CaesarCipher

cipher = CaesarCipher()
encrypted = "Rovvy 6yBvn bdfh"
shift = -10
decrypted = cipher.decrypt(encrypted, shift)
print(decrypted)  # Output: Hello World 1357
```

---

## Testing

To test the implementation:

1. Run the script:
   ```bash
   python caesar_cipher.py
   ```
2. It will output the results for encryption and decryption.

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

