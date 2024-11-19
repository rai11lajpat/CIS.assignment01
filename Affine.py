def preprocess_text(text):
    return ''.join([c.upper() for c in text if c.isalpha()])

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None  

def affine_encrypt(plain_text, key1, key2):
    plain_text = preprocess_text(plain_text)
    cipher_text = ''.join([chr(((ord(c) - ord('A')) * key1 + key2) % 26 + ord('A')) for c in plain_text])
    return cipher_text

def affine_decrypt(cipher_text, key1, key2):
    cipher_text = preprocess_text(cipher_text)
    inverse_key1 = mod_inverse(key1, 26)
    if inverse_key1 is None:
        return "Error: No modular inverse found for the key"
    plain_text = ''.join([chr((inverse_key1 * (ord(c) - ord('A') - key2)) % 26 + ord('A')) for c in cipher_text])
    return plain_text

plain_text = input("Enter plain text: ")
key1 = int(input("Enter key1 (multiplicative key): "))
key2 = int(input("Enter key2 (additive key): "))

encrypted_text = affine_encrypt(plain_text, key1, key2)
decrypted_text = affine_decrypt(encrypted_text, key1, key2)
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")

