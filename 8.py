import binascii
import math
import base64
from Crypto.Cipher import AES

key_len = 16
f = open('8.txt', 'r')
for line in f:
    ct = base64.b64decode(line.strip())
    for block_start in range(0, len(ct) - key_len, key_len):
        block = ct[block_start:block_start + key_len]
        if block in ct[block_start + key_len:]:
            print('potential ECB: ', binascii.hexlify(ct), ' with repeating block ', binascii.hexlify(block))
            break
f.close()
