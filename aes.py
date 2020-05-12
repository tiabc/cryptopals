from Crypto.Cipher import AES


def decode_aes_ecb(ct, key):
    key_len = len(key)
    ct_blocks = [ct[i:i+key_len] for i in range(0, len(ct), key_len)]
    res_pt = bytearray()
    cipher = AES.new(key, AES.MODE_ECB)
    for b in ct_blocks:
        res_pt += cipher.decrypt(b)
    return res_pt
