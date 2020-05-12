from Crypto.Cipher import AES
from common import *


def aes_cbc_decrypt(iv, ct, key):
    key_len = len(key)
    ct_blocks = [ct[i:i+key_len] for i in range(0, len(ct), key_len)]
    cipher = AES.new(key, AES.MODE_ECB)

    result = bytearray()
    previous_ct = iv
    for block in ct_blocks:
        decrypted = cipher.decrypt(block)
        pt = xor_repeating_key(decrypted, previous_ct)
        result += pt
        previous_ct = block
    return result


def aes_ecb_decrypt(ct, key):
    key_len = len(key)
    ct_blocks = [ct[i:i+key_len] for i in range(0, len(ct), key_len)]
    res_pt = bytearray()
    cipher = AES.new(key, AES.MODE_ECB)
    for b in ct_blocks:
        res_pt += cipher.decrypt(b)
    return res_pt


def is_potential_ecb(ct, key_len):
    for block_start in range(0, len(ct) - key_len, key_len):
        block = ct[block_start:block_start + key_len]
        if block in ct[block_start + key_len:]:
            return True
    return False


def add_pkcs7_padding(text, desired_length, padding=b"\04"):
    res = bytearray()
    res += text
    while len(res) < desired_length:
        res += padding
    return res
