def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            encrypted_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            encrypted_text += encrypted_char  
    return encrypted_text

def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            decrypted_char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            decrypted_text += decrypted_char
    return decrypted_text

plain_text = input("Enter Plain text: ")
key = input("Enter key: ")
plain_text = plain_text.upper()
key = key.upper()

encrypted_text = encrypt_vigenere(plain_text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt_vigenere(encrypted_text, key)
print("Decrypted text:", decrypted_text)
