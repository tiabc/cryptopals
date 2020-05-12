import base64
from block_crypto import *

key_len = 16
f = open('8.txt', 'r')
for line in f:
    ct = base64.b64decode(line.strip())
    if is_potential_ecb(ct, key_len):
        print('potential ECB: ', binascii.hexlify(ct))
f.close()
