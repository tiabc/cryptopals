import binascii
import math
import base64
from Crypto.Cipher import AES


def read_ct():
    f = open('7.txt', 'r')
    ct_base64 = ""
    for line in f:
        ct_base64 += line.strip()
    f.close()

    return base64.b64decode(ct_base64)


def decode_aes_ecb(ct, key):
    key_len = len(key)
    ct_blocks = [ct[i:i+key_len] for i in range(0, len(ct), key_len)]
    res_pt = bytearray()
    cipher = AES.new(key, AES.MODE_ECB)
    for b in ct_blocks:
        res_pt += cipher.decrypt(b)
    return res_pt


ct = read_ct()
key = b"YELLOW SUBMARINE"
pt = decode_aes_ecb(ct, key)

print(pt)
