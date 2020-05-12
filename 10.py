from block_crypto import *

key = b"YELLOW SUBMARINE"
ct = ct_from_base64_file('10.txt')
pt = aes_cbc_decrypt(b"\0" * 16, ct, key)
print(pt)
