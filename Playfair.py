import numpy as np

# Helper function to preprocess the text
def preprocess_text(text, remove_spaces=True):
    text = text.replace(" ", "") if remove_spaces else text
    return ''.join([c.upper() for c in text if c.isalpha()])

# Helper function to create the 5x5 Playfair key matrix
def create_playfair_matrix(key):
    key = preprocess_text(key)
    key_matrix = []
    used_letters = set()
    
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J is usually merged with I
        if char not in used_letters and char != 'J':
            key_matrix.append(char)
            used_letters.add(char)
    
    return np.array(key_matrix).reshape(5, 5)

# Helper function to format plaintext for Playfair cipher
def format_playfair_text(text):
    text = preprocess_text(text)
    formatted_text = ""
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            formatted_text += text[i] + 'X'
            i += 1
        elif text[i] == text[i + 1]:
            formatted_text += text[i] + 'X'
            i += 1
        else:
            formatted_text += text[i] + text[i + 1]
            i += 2
    return formatted_text

# Function to find position of a letter in the matrix
def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None, None

# Playfair encryption
def playfair_encrypt(plain_text, key):
    matrix = create_playfair_matrix(key)
    plain_text = format_playfair_text(plain_text)
    cipher_text = ""
    
    for i in range(0, len(plain_text), 2):
        r1, c1 = find_position(matrix, plain_text[i])
        r2, c2 = find_position(matrix, plain_text[i + 1])
        
        if r1 == r2:
            cipher_text += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            cipher_text += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            cipher_text += matrix[r1][c2] + matrix[r2][c1]
    
    return cipher_text

# Playfair decryption
def playfair_decrypt(cipher_text, key):
    matrix = create_playfair_matrix(key)
    plain_text = ""
    
    for i in range(0, len(cipher_text), 2):
        r1, c1 = find_position(matrix, cipher_text[i])
        r2, c2 = find_position(matrix, cipher_text[i + 1])
        
        if r1 == r2:
            plain_text += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            plain_text += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else:
            plain_text += matrix[r1][c2] + matrix[r2][c1]
    
    return plain_text

# Input and Output demonstration
if __name__ == "__main__":
    plain_text = input("Enter the plain text: ")
    key = input("Enter the key: ")
    
    encrypted_text = playfair_encrypt(plain_text, key)
    print("Encrypted Text:", encrypted_text)
    
    decrypted_text = playfair_decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)
