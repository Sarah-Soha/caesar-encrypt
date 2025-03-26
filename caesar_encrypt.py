import string


def caesar_encrypt(InString, Shift):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypted = ""

    for char in InString:
        if char in uppercase:
            new_char = uppercase[(uppercase.index(char) + Shift) % 26]
        elif char in lowercase:
            new_char = lowercase[(lowercase.index(char) + Shift) % 26]
        else:
            new_char = char
        encrypted = encrypted + new_char
    return "" + str(encrypted)


code = caesar_encrypt("Hello, World!", 3)
print(code)
