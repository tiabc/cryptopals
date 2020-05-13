from binascii import *
from base64 import *
from block_crypto import *


def encrypt(supplied_pt):
    key = b",\xfb\xae\xfb\x178pO\xf8\x9d\xdb\xbfZ\xa3\xf9d"
    appended = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
    pt = supplied_pt + b64decode(appended)
    ct = aes_ecb_encrypt(pt, key)
    return ct


print(break_aes_ecb(0, encrypt))
