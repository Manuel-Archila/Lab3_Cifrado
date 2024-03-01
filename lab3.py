from PIL import Image
from utils import *



print("Primera parte")
ayno_data = open_image('./ayno_encrypted_image.jpeg')
mr_increible_data = open_image('./mr-increible_encrypted_image.jpeg')

mr_increible_key = read_key('./keys/mr-increible.key')

mr_increible_key = bytes.fromhex(mr_increible_key.decode('utf-8'))



mr_increible_decrypted = aes_decrypt_ecb(mr_increible_key, mr_increible_data)

new_image(mr_increible_decrypted, './mr-increible_decrypted_image.jpeg')




key = "a3ec0f654471b1c1ae7c8b9018680343"
iv = "19fd8ab90f9dbc5a02d27c9969c5671e"


# img = Image.open('encrypted_body.ppm')

# # Guarda la imagen en formato JPG
# img.save('tuxon_cbc.jpg', 'JPEG')

