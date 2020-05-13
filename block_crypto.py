from Crypto.Cipher import AES
from common import *


def aes_cbc_encrypt(iv, pt, key):
    key_len = len(key)
    pt_blocks = [pt[i:i + key_len] for i in range(0, len(pt), key_len)]
    pt_blocks[-1] = add_pkcs7_padding(pt_blocks[-1], key_len)

    cipher = AES.new(key, AES.MODE_ECB)
    result = bytearray()
    prev_pt = iv
    for pt_block in pt_blocks:
        xored = xor_repeating_key(pt_block, prev_pt)
        encrypted = cipher.encrypt(xored)
        result += encrypted
        prev_pt = pt_block
    return result


def aes_cbc_decrypt(iv, ct, key):
    key_len = len(key)
    ct_blocks = [ct[i:i + key_len] for i in range(0, len(ct), key_len)]
    cipher = AES.new(key, AES.MODE_ECB)

    result = bytearray()
    previous_ct = iv
    for block in ct_blocks:
        decrypted = cipher.decrypt(block)
        pt = xor_repeating_key(decrypted, previous_ct)
        result += pt
        previous_ct = block
    return result


def aes_ecb_encrypt(pt, key):
    key_len = len(key)
    pt_blocks = [pt[i:i + key_len] for i in range(0, len(pt), key_len)]
    pt_blocks[-1] = add_pkcs7_padding(pt_blocks[-1], key_len)

    res_pt = bytearray()
    cipher = AES.new(key, AES.MODE_ECB)
    for b in pt_blocks:
        res_pt += cipher.encrypt(b)
    return res_pt


def aes_ecb_decrypt(ct, key):
    key_len = len(key)
    ct_blocks = [ct[i:i + key_len] for i in range(0, len(ct), key_len)]
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


def detect_block_size(encrypt_func):
    feed = bytearray()
    prev_len = len(encrypt_func(feed))
    while True:
        feed += b"A"
        length = len(encrypt_func(feed))
        if length != prev_len:
            return length - prev_len, len(feed) - 1


def detect_last_byte(encrypt_func, prefix, block_size, block_num, char_num):
    ctmap = {}
    for char in range(0, 256):
        ct = encrypt_func(prefix + bytes([char]))
        ct_block = bytes(ct[0:block_size])
        ctmap[ct_block] = bytes([char])
    ct = encrypt_func(prefix[0:len(prefix) - char_num])
    return ctmap[bytes(ct[block_num * block_size:(block_num + 1) * block_size])]


def break_aes_ecb(encrypt_func):
    block_size, chars_to_fill_block = detect_block_size(encrypt_func)
    print("(block size: %d)" % block_size)

    is_ecb = is_potential_ecb(encrypt_func(b"A" * block_size * 3), block_size)
    if not is_ecb:
        raise Exception("the encryption mode doesn't seem ECB")

    ct_len = len(encrypt_func(b""))

    plaintext = b""
    block_num = 0
    prefix = b"A" * (block_size - 1)
    while block_num < ct_len / block_size:
        for i in range(0, block_size):
            # print(prefix, len(prefix))
            first_byte = detect_last_byte(
                encrypt_func,
                prefix,
                block_size,
                block_num,
                i,
            )
            prefix = prefix[1:] + first_byte
            plaintext += first_byte
        prefix = plaintext[-block_size + 1:]
        block_num += 1

    return plaintext
