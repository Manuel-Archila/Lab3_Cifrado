from utils import *
binascii


plaintext = 'Hola'

# Convertir el texto a ascii
ascii_letters = word2ascii(plaintext)
binaries = [decimal2binary(letter) for letter in ascii_letters]

print('Texto en binario:', binaries)
joined_binaries = ''.join(binaries)
print('Texto en binario concatenado:', joined_binaries)

# Generar keystream
keystream = generate_keystream(len(joined_binaries))

# Cifrar el texto
ciphertext, cyphered_bytes = encrypt(joined_binaries, keystream)
print('Texto cifrado:', ciphertext)

# Descifrar el texto
plaintext, decyphered_bytes = decrypt(cyphered_bytes, keystream)
print('Texto descifrado:', plaintext)

print("1.¿Cómo cambia el mensaje cifrado cuando cambias la clave?")
print("El mensaje cifrado cambia completamente, ya que el keystream es diferente, por lo que el resultado del XOR no es el mismo.\n")

print("2.¿Qué sucede si utilizas el mismo Keystream para cifrar dos mensajes diferentes?")
print("La seguridad de la llave se ve comprometida, ya que si se conoce el keystream, se puede descifrar cualquier mensaje cifrado con el mismo keystream.\n")

print("3.¿Cómo afecta la longitud del Keystream a la seguridad del cifrado?")
print("Si el keystream es muy corto o se repite, la seguridad del cifrado se ve comprometida, ya que se pueden introducir patrones en el mensaje cifrado que permitan descifrarlo.\n")


print("\nDES")

key = get_random_bytes(8)
plaintext = "Este es mi mensaje secreto".encode()

ciphertext_DES = des_encrypt(key, plaintext)
print("Texto cifrado:", binascii.hexlify(ciphertext_DES))

plaintext_DES = des_decrypt(key, ciphertext_DES)
print("Texto descifrado:", plaintext_DES)

print("\n3DES")

key = get_random_bytes(24)
plaintext = "Este es mi mensaje secreto".encode()

ciphertext_3DES = des3_encrypt(key, plaintext)
print("Texto cifrado:", binascii.hexlify(ciphertext_3DES))

plaintext_3DES = des3_decrypt(key, ciphertext_3DES)
print("Texto descifrado:", plaintext_3DES)

print("\nAES")

key = get_random_bytes(32)

plaintext = "Este es mi mensaje secreto".encode()
ciphertext_AES = aes_encrypt(key, plaintext)
print("Texto cifrado:", binascii.hexlify(ciphertext_AES))

plaintext_AES = aes_decrypt(key, ciphertext_AES)
print("Texto descifrado:", plaintext_AES)

key = get_random_bytes(16)

image_data, size = load_image("./Logo-UVG.webp")

encrypted_image_ecb = encrypt_ecb(image_data, key)
save_image(encrypted_image_ecb, "logo_cifrada_ecb.png", size)

decrypted_image_ecb = decrypt_ecb(encrypted_image_ecb, key)
save_image(decrypted_image_ecb, "logo_descifrada_ecb.png", size)

encrypted_image_cbc = encrypt_cbc(image_data, key)
save_image(encrypted_image_cbc, "logo_cifrada_cbc.png", size)

decrypted_image_cbc = decrypt_cbc(encrypted_image_cbc, key)
save_image(decrypted_image_cbc, "logo_descifrada_cbc.png", size)



