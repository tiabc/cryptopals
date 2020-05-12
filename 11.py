from block_crypto import *
import random
import os


def encrypt_ecb_or_cbc(supplied_pt, block_size):
    key = os.urandom(block_size)
    prepended_data = os.urandom(random.randint(5, 10))
    appended_data = os.urandom(random.randint(5, 10))

    pt = prepended_data + supplied_pt + appended_data
    if random.randint(0, 1) == 0:
        print("(secretly tell you it's ECB)")
        return aes_ecb_encrypt(pt, key)
    else:
        print("(secretly tell you it's CBC)")
        iv = os.urandom(block_size)
        return aes_cbc_encrypt(iv, pt, key)


def detect_encryption_mode(encrypt_func):
    key_len = 16

    pt = b"A" * (11 + 16 * 2)
    ct = encrypt_func(pt, key_len)

    if is_potential_ecb(ct, key_len):
        return "probably ECB"
    return "probably CBC"


for i in range(50):
    print(detect_encryption_mode(encrypt_ecb_or_cbc), "\n")
