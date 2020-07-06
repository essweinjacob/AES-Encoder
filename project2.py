from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


def main():
    # Get plaintext
    plaintext = "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    #print(len(plaintext))

    # Make sure message is base 16
    paddedMessage = padMessage(plaintext)
    #print(len(paddedMessage))

    # Encrypt Message
    encryptMessage(paddedMessage)


def padMessage(message):
    while len(message) % 16 != 0:
        message = message + " "
    return message

def encryptMessage(message):
    backend = default_backend()
    key = os.urandom(16)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    print(ciphertext)
    decryptMessage(ciphertext, cipher)

def decryptMessage(codedMessage, cipher):
    decryptor = cipher.decryptor()
    decodedMessage = decryptor.update(codedMessage) + decryptor.finalize()
    print(decodedMessage)

main()