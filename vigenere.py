from common import *


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
        d = hamming_distance([
            ct[key_len * 0:key_len * 1],
            ct[key_len * 1:key_len * 2],
            ct[key_len * 2:key_len * 3],
            ct[key_len * 3:key_len * 4]
        ]) / key_len
        if d < best_distance:
            best_distance = d
            best_key_len = key_len

    return best_key_len


def transpose_ct_blocks_by_chars(ct_by_blocks, key_len):
    ct_by_chars = []
    for i in range(0, key_len):
        ct_by_chars.append(bytearray())
        for block in ct_by_blocks:
            if len(block) > i:
                ct_by_chars[i].append(block[i])
    return ct_by_chars


def crack_and_return_1key(ct):
    best_key = -1
    best_score = 0
    for key in range(0, 256):
        decrypted = xor_repeating_key(ct, [key])
        s = count_readable_letters(decrypted)
        if s >= best_score:
            best_score = s
            best_key = key
    return best_key


def break_vigenere(ciphertext):
    key_len = guess_key_len(ciphertext)
    ct_by_blocks = [ciphertext[i:i + key_len] for i in range(0, len(ciphertext), key_len)]
    ct_by_chars = transpose_ct_blocks_by_chars(ct_by_blocks, key_len)

    key = bytearray()
    for ct in ct_by_chars:
        key.append(crack_and_return_1key(ct))

    return xor_repeating_key(ciphertext, key)
