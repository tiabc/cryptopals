from Crypto.Cipher import AES
import binascii


def decode_aes_ecb(ct, key):
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
