import random
import string

def encrypt_message(message):
    encrypted = ""
    for char in message:
        encrypted += char + random.choice(string.ascii_letters)
    return encrypted

def decrypt_message(encrypted_message):
    decrypted = ""
    for i in range(0, len(encrypted_message), 2):
        decrypted += encrypted_message[i]
    return decrypted

message = "fish"
encrypted = encrypt_message(message)
print("Зашифроване повідомлення:", encrypted)

decrypted = decrypt_message(encrypted)
print("Розшифроване повідомлення:", decrypted)
