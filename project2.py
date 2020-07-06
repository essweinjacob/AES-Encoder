from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import time


def main():
    # Menu
    fileChoice = input("Please choose which file you would like to encrypt and decrypt: \n(S)mall\n(L)arge\n")

    if (fileChoice == 'L' or fileChoice == 'l'):
        print("Large file choosen")
        inputFile = "large.txt"
        outputFile = "large.encoded"
        keySize = int(input("What size key would you like to use?\n16\n32\n"))

    else:
        print("Small file choosen")
        inputFile = "small.txt"
        outputFile = "small.encoded"
        keySize = int(input("What size key would you like to use?\n16\n32\n"))

    with open(inputFile, 'rb') as f:
        plaintext = f.read()

    # Make sure message is base 16
    paddedMessage = padMessage(plaintext)
    #print(len(paddedMessage))

    # Run for a certain amount of time
    timerEnd = time.time() + 1
    counter = 0
    while time.time() < timerEnd:
         # Encrypt Message
        encryptMessage(paddedMessage, keySize)
        counter = counter + 1
    
    print("The message was encrypted and decrypted " + str(counter) + " times")


def padMessage(message):
    while len(message) % 16 != 0:
        message = message + " "
    return message

def encryptMessage(message, keySize):
    backend = default_backend()
    key = os.urandom(keySize)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message) + encryptor.finalize()
    #print("Your encoded message is: ")
    #print(ciphertext)
    decryptMessage(ciphertext, cipher)

def decryptMessage(codedMessage, cipher):
    decryptor = cipher.decryptor()
    decodedMessage = decryptor.update(codedMessage) + decryptor.finalize()
    #print("The decoded message is: ")
    #print(decodedMessage)

main()