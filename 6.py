import binascii
import math
import base64


def read_ct():
    f = open('6.txt', 'r')
    ct_base64 = ""
    for line in f:
        ct_base64 += line.strip()
    f.close()

    return base64.b64decode(ct_base64)


def hamming_distance(words):
    comparisons = 0
    d = 0
    for i in range(0, len(words)):
        for j in range(i+1, len(words)):
            comparisons += 1
            for b in range(len(words[i])):
                for byte in range(0, 8):
                    mask = 1 << byte
                    if words[i][b] & mask != words[j][b] & mask:
                        d += 1

    return d / comparisons


def guess_key_len(ct):
    best_key_len = -1
    best_distance = 1 << 30
    for key_len in range(2, 41):
        # TODO: Probably, take more blocks and average the results.
        d = hamming_distance([
            ct[key_len * 0:key_len * 1],
            ct[key_len * 1:key_len * 2],
            ct[key_len * 2:key_len * 3],
            ct[key_len * 3:key_len * 4]
        ]) / key_len
        if d < best_distance:
            best_distance = d
            best_key_len = key_len
        # print(key_len, ' ', d)

    # normalized hamming distance: 1.2
    return best_key_len


def transpose_ct_blocks_by_chars(ct_by_blocks, key_len):
    ct_by_chars = []
    for i in range(0, key_len):
        ct_by_chars.append(bytearray())
        for block in ct_by_blocks:
            if len(block) > i:
                ct_by_chars[i].append(block[i])
    return ct_by_chars


def count_letters(text):
    n = 0
    for ch in text:
        if ord('a') <= ch <= ord('z') or ord('A') <= ch <= ord('Z') or ch == ord(' ') or ch == ord(' '):
            n += 1
    return n


def encrypt_or_decrypt(text, key):
    ct = bytearray()
    for i in range(len(text)):
        ct.append(text[i] ^ key[i % len(key)])
    return ct


def crack_and_return_1key(ct):
    # result_pt = b''
    best_key = -1
    best_score = 0
    for key in range(0, 256):
        decrypted = encrypt_or_decrypt(ct, [key])
        s = count_letters(decrypted)
        if s >= best_score:
            best_score = s
            best_key = key
            result_pt = decrypted
    # print(result_pt)
    return best_key


def break_vigenere(ciphertext):
    key_len = guess_key_len(ciphertext)
    ct_by_blocks = [ciphertext[i:i + key_len] for i in range(0, len(ciphertext), key_len)]
    ct_by_chars = transpose_ct_blocks_by_chars(ct_by_blocks, key_len)

    key = bytearray()
    for ct in ct_by_chars:
        key.append(crack_and_return_1key(ct))

    return encrypt_or_decrypt(ciphertext, key)


ct = read_ct()
pt = break_vigenere(ct)

print(pt)
