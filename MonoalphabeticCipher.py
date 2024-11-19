def preprocess_text(text, remove_spaces=True):
    text = ''.join([c for c in text if c.isalpha()])  
    if remove_spaces:
        text = text.replace(" ", "")
    return text.upper() 

def additive_encrypt(plain_text, key):
    plain_text = preprocess_text(plain_text)
    cipher_text = ""
    for char in plain_text:
        shifted = (ord(char) - ord('A') + key) % 26
        encrypted_char = chr(shifted + ord('A'))
        cipher_text += encrypted_char
    return cipher_text

def additive_decrypt(cipher_text, key):
    cipher_text = preprocess_text(cipher_text)
    plain_text = ""
    for char in cipher_text:
        shifted = (ord(char) - ord('A') - key) % 26
        decrypted_char = chr(shifted + ord('A'))
        plain_text += decrypted_char
    return plain_text


plain_text = input("Enter plain text: ")
key = int(input("Enter key (0-25): "))
encrypted_text = additive_encrypt(plain_text, key)
decrypted_text = additive_decrypt(encrypted_text, key)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
