from Crypto.Cipher import AES
import base64

def xor(t, key):
    r = bytearray()
    for i in range(len(t)):
        r.append(t[i] ^ key[i % len(key)])
    return r


def aes_cbc_decrypt(ct, iv, key):
    key_len = len(key)
    ct_blocks = [ct[i:i+key_len] for i in range(0, len(ct), key_len)]
    cipher = AES.new(key, AES.MODE_ECB)

    result = bytearray()
    previous_ct = iv
    for block in ct_blocks:
        decrypted = cipher.decrypt(block)
        pt = xor(decrypted, previous_ct)
        result += pt
        previous_ct = block
    return result


def read_ct():
    f = open('10.txt', 'r')
    ct_base64 = ""
    for line in f:
        ct_base64 += line.strip()
    f.close()

    return base64.b64decode(ct_base64)


key = b"YELLOW SUBMARINE"
ct = read_ct()
pt = aes_cbc_decrypt(ct, b"\0" * 16, key)
print(pt)
