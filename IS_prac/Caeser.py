def encrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: 
            letter_index = (alpha.find(letter) + key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    return result

def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: 
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    return result

word = "information security"
encrypted = encrypt(3,word)
print(encrypted)
decrypted = decrypt(3,encrypted)
print(decrypted)    
