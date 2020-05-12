import binascii
from lib import *


result_pt = b''
best_score = 0
f = open('4.txt', 'r')
for ct_hex in f:
    ct = binascii.unhexlify(ct_hex.strip())

    # max_letters_key = 0
    for key in range(0, 256):
        decrypted = xor_single_key(ct, key)
        s = count_readable_letters(decrypted)
        if s >= best_score:
            best_score = s
            result_pt = decrypted
f.close()

print(result_pt)
