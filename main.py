from utils import *

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
print("El mensaje cifrado cambia completamente, ya que el keystream es diferente, por lo que el resultado del XOR no es el mismo.")

print("2.¿Qué sucede si utilizas el mismo Keystream para cifrar dos mensajes diferentes?")
print("La seguridad de la llave se ve comprometida, ya que si se conoce el keystream, se puede descifrar cualquier mensaje cifrado con el mismo keystream.")

print("3.¿Cómo afecta la longitud del Keystream a la seguridad del cifrado?")
print("Si el keystream es muy corto o se repite, la seguridad del cifrado se ve comprometida, ya que se pueden introducir patrones en el mensaje cifrado que permitan descifrarlo.")