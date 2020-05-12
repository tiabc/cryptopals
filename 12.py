from binascii import *
from base64 import *
from block_crypto import *


def encrypt(supplied_pt):
    key = b",\xfb\xae\xfb\x178pO\xf8\x9d\xdb\xbfZ\xa3\xf9d"
    appended = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
    pt = supplied_pt + b64decode(appended)
    ct = aes_ecb_encrypt(pt, key)
    return ct


def detect_last_byte(prefix, block_size, block_num, char_num):
    ctmap = {}
    for char in range(0, 256):
        ct = encrypt(prefix + bytes([char]))
        ct_block = bytes(ct[0:block_size])
        ctmap[ct_block] = bytes([char])
    ct = encrypt(prefix[0:len(prefix) - char_num])
    return ctmap[bytes(ct[block_num * block_size:(block_num + 1) * block_size])]


block_size, chars_to_fill_block = detect_block_size(encrypt)
print("block size: %d" % block_size)

is_ecb = is_potential_ecb(encrypt(b"A" * block_size * 2), block_size)
print("is_ecb: %d" % is_ecb)

ct_len = len(encrypt(b""))

plaintext = b""
block_num = 0
prefix = b"A" * (block_size - 1)
while block_num < ct_len / block_size:
    for i in range(0, block_size):
        print(prefix, len(prefix))
        first_byte = detect_last_byte(prefix, block_size, block_num, i)
        prefix = prefix[1:] + first_byte
        plaintext += first_byte
    prefix = plaintext[-block_size + 1:]
    block_num += 1

print(plaintext)
