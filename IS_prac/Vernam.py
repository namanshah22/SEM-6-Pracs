def encrypt_vernam(plain_text, key):
    ciphertext = ""
    if len(plain_text) == len(key):
        for i in range(len(plain_text)):
            conversion = (ord(plain_text[i]) - 65) ^ (ord(key[i]) - 65)
            conversion = conversion % 26
            ciphertext += chr(65 + conversion)
        return ciphertext
    else:
        return "Key and plaintext lengths are not equal"

plain_text = input("Enter plain text: ").upper()
key = input("Enter key: ").upper()

ciphertext = encrypt_vernam(plain_text, key)
print("Cipher text is:", ciphertext)

decrypted_text = encrypt_vernam(ciphertext, key) 
print("Decrypted text is:", decrypted_text)
