from common import *
from block_crypto import *

ct = ct_from_base64_file('7.txt')
key = b"YELLOW SUBMARINE"
pt = aes_ecb_decrypt(ct, key)

print(pt)
