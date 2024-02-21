import random

def word2ascii(word):
    ascii_letters = []
    for letter in word:
        ascii_letters.append(ord(letter))
    return ascii_letters

# Funcion que convierte de decimal a binario
def decimal2binary(decimal, length=8):
    binary = ''

    if decimal == 0:
        return '0'
    
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    
    if len(binary) < length:
        binary = '0' * (length - len(binary)) + binary
    return binary

# Funcion que convierte de binario a decimal
def binary2decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2 ** ((len(binary) - 1 - i))
    return decimal

# Funcion que convierte de ascii a palabra
def ascii2word(ascii_letters):
    word = ''
    for ascii_letter in ascii_letters:
        word += chr(ascii_letter)
    return word

# Funcion que genera un keystream
def generate_keystream(length):
    return [random.randint(0, 1) for _ in range(length*8)]

# Funcion que realiza el XOR entre dos keystreams
def xor_streams(stream1, stream2):
    """XOR two keystreams."""
    return [int(s1) ^ int(s2) for s1, s2 in zip(stream1, stream2)]

# Funcion que realiza el XOR entre un keystream y un texto
def encrypt(plaintext, keystream):
    bytes_encrypted = xor_streams(plaintext, keystream)
    bytes_encrypt = ''.join([str(b) for b in bytes_encrypted])
    bytes_encrypt = [bytes_encrypt[i:i+8] for i in range(0, len(bytes_encrypt), 8)]
    bytes_encrypt = [binary2decimal(b) for b in bytes_encrypt]
    bytes_encrypt = ascii2word(bytes_encrypt)
    return bytes_encrypt, bytes_encrypted

# Funcion que realiza el XOR entre un keystream y un texto cifrado
def decrypt(ciphertext, keystream):
    bytes_decrypted = xor_streams(ciphertext, keystream)
    bytes_decrypt = ''.join([str(b) for b in bytes_decrypted])
    bytes_decrypt = [bytes_decrypt[i:i+8] for i in range(0, len(bytes_decrypt), 8)]
    bytes_decrypt = [binary2decimal(b) for b in bytes_decrypt]
    bytes_decrypt = ascii2word(bytes_decrypt)


    return bytes_decrypt, bytes_decrypted


