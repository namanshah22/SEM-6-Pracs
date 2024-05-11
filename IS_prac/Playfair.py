def create_matrix(key, list1=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']):
    key_letters = []  # List to store unique letters from the key
    compElements = []  # List to store all unique letters including the ones from the key and default list
    matrix = []  # List to store the final matrix

    # Extract unique letters from the key and add them to key_letters and compElements
    for i in key:
        if i not in key_letters:
            key_letters.append(i)
            compElements.append(i) 

    # Add remaining unique letters from the default list to compElements
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    # Create the matrix by adding elements from compElements in chunks of 5 until compElements is empty
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]

    return matrix

def separate_same_letters(message):
    """
    Insert 'X' between consecutive identical letters in the message.
    """
    index = 0
    while (index < len(message)):
        # If it's the last letter and the message length is odd, append 'X'
        if len(message)%2!=0:
            message+='X'
        l1 = message[index]
        l2 = message[index + 1]
        # If two consecutive letters are the same, insert 'X' between them
        if l1 == l2:
            message = message[:index + 1] + "X" + message[index + 1:]
        index += 2
    return message

def indexOf(letter, matrix):
    """
    Find the row and column index of a letter in the Playfair matrix.
    """
    for i in range(5):
        try:
            index = matrix[i].index(letter)
            return (i, index)
        except:
            continue

def playfair(key, message, encrypt=True):
    """
    Perform Playfair encryption or decryption based on the given key and message.
    """
    # Determine the increment based on encryption or decryption
    inc = 1
    if encrypt == False:
        inc = -1
    
    # Create the Playfair matrix
    matrix = create_matrix(key)
    
    # Preprocess the message
    message = message.upper()
    message = message.replace(' ', '')
    message = separate_same_letters(message)
    
    # Initialize cipher text
    cipher_text = ''
    
    # Iterate through pairs of letters in the message
    for (l1, l2) in zip(message[0::2], message[1::2]):
        # Find the row and column indices of the current pair of letters
        row1, col1 = indexOf(l1, matrix)
        row2, col2 = indexOf(l2, matrix)
        
        # Handle three cases: same row, same column, and different rows and columns
        if row1 == row2:
            cipher_text += matrix[row1][(col1 + inc) % 5] + matrix[row2][(col2 + inc) % 5]
        elif col1 == col2:
            cipher_text += matrix[(row1 + inc) % 5][col1] + matrix[(row2 + inc) % 5][col2]
        else:
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    
    return cipher_text

plainText = input("Enter the Plain text: ").upper()
key = input("Enter Key: ").upper()
cipherText = playfair(key, plainText)
print(f'Encrypted:{cipherText}\nDecrypted:{playfair(key, cipherText, encrypt=False)}')
