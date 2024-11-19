def preprocess_text(text):
    return ''.join([c.upper() for c in text if c.isalpha()])

def autokey_encrypt(plain_text, key):
    plain_text = preprocess_text(plain_text)
    key_stream = (key + plain_text)[:len(plain_text)]
    cipher_text = ""
    for p, k in zip(plain_text, key_stream):
        encrypted_char = chr((ord(p) - ord('A') + ord(k) - ord('A')) % 26 + ord('A'))
        cipher_text += encrypted_char
    return cipher_text

def autokey_decrypt(cipher_text, key):
    cipher_text = preprocess_text(cipher_text)
    key_stream = key
    plain_text = ""
    for i in range(len(cipher_text)):
        decrypted_char = chr((ord(cipher_text[i]) - ord('A') - (ord(key_stream[i]) - ord('A'))) % 26 + ord('A'))
        plain_text += decrypted_char
        key_stream += decrypted_char
    return plain_text

plain_text = input("Enter plain text: ")
key = input("Enter key: ")
encrypted_text = autokey_encrypt(plain_text, key)
decrypted_text = autokey_decrypt(encrypted_text, key)

print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
