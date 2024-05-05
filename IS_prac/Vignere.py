import string

def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    uppercase_letters = string.ascii_uppercase
    for i,char in enumerate(plain_text):
        if char.isalpha():
            shift = uppercase_letters.index(key[i % key_length])
            encrypted_char = uppercase_letters[(uppercase_letters.index(char.upper()) + shift) % 26]
            encrypted_text += encrypted_char  
    return encrypted_text

def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    uppercase_letters = string.ascii_uppercase
    for i,char in enumerate(encrypted_text):
        if char.isalpha():
            shift = uppercase_letters.index(key[i % key_length])
            decrypted_char = uppercase_letters[(uppercase_letters.index(char.upper()) - shift) % 26]
            decrypted_text += decrypted_char
    return decrypted_text

# Example usage
plain_text = input("Enter Plain text: ").upper()
key = input("Enter key: ").upper()

encrypted_text = encrypt_vigenere(plain_text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt_vigenere(encrypted_text, key)
print("Decrypted text:", decrypted_text)
