def create_matrix(key):
    """
    Create a 5x5 matrix (Playfair square) based on the given key.
    """
    # Convert key to uppercase to ensure consistency
    key = key.upper()
    
    # Initialize a 5x5 matrix with zeros
    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(0)
        matrix.append(row)
    
    # Keep track of letters already added to the matrix
    letters_added = []
    
    # Initialize row and column indices
    row = 0
    col = 0
    
    # Iterate through each letter in the key
    for letter in key:
        # If the letter is not already added to the matrix, add it
        if letter not in letters_added:
            matrix[row][col] = letter
            letters_added.append(letter)
        # Move to the next column if the current column is filled
        if (col == 4):
            col = 0
            row += 1
        else:
            col += 1
    
    # Fill the remaining matrix positions with letters from A to Z (excluding 'J')
    for letter in range(65, 91):
        if letter == 74:  # Skip 'J'
            continue
        if chr(letter) not in letters_added:
            letters_added.append(chr(letter))
    
    # Assign the remaining letters to the matrix
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index += 1
    return matrix

def separate_same_letters(message):
    """
    Insert 'X' between consecutive identical letters in the message.
    """
    index = 0
    while (index < len(message)):
        l1 = message[index]
        # If it's the last letter and the message length is odd, append 'X'
        if index == len(message) - 1:
            message = message + 'X'
            index += 2
            continue
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

# Option selection loop
option = 1
while(option == 1 or option == 2):
    option = int(input("Select an option\n 1 for Encryption\n 2 for Decryption\n 3 for Exit: "))
    if(option == 1):
        plainText = input("Enter the Plain text: ")
        key = input("Enter Key: ")
        print('Encrypting')
        print(playfair(key, plainText))
    if(option == 2):
        cipherText = input("Enter the cipher text: ")
        key = input("Enter Key: ")
        print('Decrypting')
        print(playfair(key, cipherText, False))
    if (option == 3):
        break
