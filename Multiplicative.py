def mod_inverse(a, m):
    for x in range(m):
        if (a * x) % m == 1:
            return x
    return -1

def preprocess_text(text):
    return ''.join([c.upper() for c in text if c.isalpha()])

def multiplicative_encrypt(plain_text, key):
    plain_text = preprocess_text(plain_text)
    cipher_text = ""
    for char in plain_text:
        encrypted_char = chr(((ord(char) - ord('A')) * key % 26) + ord('A'))
        cipher_text += encrypted_char
    return cipher_text

def multiplicative_decrypt(cipher_text, key):
    cipher_text = preprocess_text(cipher_text)
    inverse_key = mod_inverse(key, 26)
    if inverse_key == -1:
        raise ValueError("No modular inverse exists for the provided key.")
    
    plain_text = ""
    for char in cipher_text:
        decrypted_char = chr(((ord(char) - ord('A')) * inverse_key % 26) + ord('A'))
        plain_text += decrypted_char
    return plain_text

plain_text = input("Enter plain text: ")
key = int(input("Enter key (must be coprime with 26): "))
encrypted_text = multiplicative_encrypt(plain_text, key)
decrypted_text = multiplicative_decrypt(encrypted_text, key)

print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
