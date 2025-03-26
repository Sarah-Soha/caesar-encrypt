# Caesar Cipher Encryption Tool

This is a simple **Caesar Cipher encryption** tool written in Python. It shifts each letter in the input string by a given number of positions in the alphabet. Non-alphabetic characters (such as spaces, punctuation, etc.) remain unchanged.

# How It Works

The Caesar cipher is one of the oldest encryption techniques, where each letter in the plaintext is shifted by a fixed number of positions. The Python implementation provided here can encrypt both uppercase and lowercase letters, while leaving non-alphabetic characters intact.

# Features:
- **Encrypts** text using a Caesar cipher.
- Works with both **uppercase** and **lowercase** letters.
- Leaves **non-alphabet characters** (spaces, punctuation, etc.) unchanged.
- Can be adjusted for **different shift values**.

# How to Use:

1. Clone this repository or download the `.py` file.
2. Open the script in a Python environment (Python 3 recommended).
3. Modify the `InString` and `Shift` values in the code as needed.
4. Run the script:
   ```bash
   python caesar_cipher.py
# Example:  
  code = caesar_encrypt("Hello, World!", 3)  
  print(code)  

  OUTPUT: Khoor, Zruog!
