import binascii
from lib import *

encrypted_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
encrypted = binascii.unhexlify(encrypted_hex)

max_eng_letters_key = 0
max_eng_letters = 0
for key in range(0, 256):
    decrypted = xor_single_key(encrypted, key)
    cur_eng_letters = count_readable_letters(decrypted)
    if cur_eng_letters > max_eng_letters:
        max_eng_letters = cur_eng_letters
        max_eng_letters_key = key

print(max_eng_letters, max_eng_letters_key)
print(xor_single_key(encrypted, max_eng_letters_key))
