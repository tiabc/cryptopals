def xor_single_key(text, key):
    res = bytearray()
    for char in text:
        res.append(char ^ key)
    return res


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
