import base64
import random


def count_readable_letters(text):
    n = 0
    for ch in text:
        if ord('a') <= ch <= ord('z') or ord('A') <= ch <= ord('Z') or ch == ord(' '):
            n += 1
    return n


def xor_repeating_key(text, key):
    ct = bytearray()
    for i in range(len(text)):
        ct.append(text[i] ^ key[i % len(key)])
    return ct


def ct_from_base64_file(filename):
    f = open(filename, 'r')
    ct_base64 = ""
    for line in f:
        ct_base64 += line.strip()
    f.close()

    return base64.b64decode(ct_base64)
