#### **CaesarCipher-Python**

This project is a Python implementation of the classic Caesar Cipher algorithm. It provides an easy-to-use interface for encrypting and decrypting text with a customizable shift value.

---

#### **Features**
- Encrypts and decrypts alphanumeric text.
- Handles case insensitivity.
- Customizable shift values.
- Simple, reusable design.

---

#### **Usage**

```python
from caesar_cipher import CaesarCipher

cipher = CaesarCipher()

# Encrypting
text = "hello world 123"
encrypted = cipher.encrypt(text, shift=5)
print("Encrypted:", encrypted)

# Decrypting
decrypted = cipher.decrypt(encrypted, shift=-5)
print("Decrypted:", decrypted)
```

---

#### **Example Output**
```plaintext
Encrypted: "rovvy 6y1vn bcd"
Decrypted: "hello world 123"
```

#### **Installation**
Clone the repository and run the Python script:
```bash
git clone https://github.com/mobinic1101/CaesarCipher-Python.git
cd CaesarCipher-Python
python3 caesar_cipher.py
```

