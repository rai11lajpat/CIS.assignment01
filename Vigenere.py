def preprocess_text(text):
    return ''.join([c.upper() for c in text if c.isalpha()])

def vigenere_encrypt(plain_text, key):
    plain_text = preprocess_text(plain_text)
    key = (key * ((len(plain_text) // len(key)) + 1))[:len(plain_text)]
    cipher_text = ''.join([chr((ord(p) - ord('A') + ord(k) - ord('A')) % 26 + ord('A')) for p, k in zip(plain_text, key)])
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    cipher_text = preprocess_text(cipher_text)
    key = (key * ((len(cipher_text) // len(key)) + 1))[:len(cipher_text)]
    plain_text = ''.join([chr((ord(c) - ord('A') - (ord(k) - ord('A'))) % 26 + ord('A')) for c, k in zip(cipher_text, key)])
    return plain_text

plain_text = input("Enter plain text: ")
key = input("Enter key: ")
encrypted_text = vigenere_encrypt(plain_text, key)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")

