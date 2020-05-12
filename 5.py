import binascii
import math


# def get_ciphertexts():
#     f = open('4.txt', 'r')
#     lines = f.readlines()
#     f.close()
#     return lines
#
#
#
# def decrypt(ct, key):
#     res = bytearray()
#     for ch in ct:
#         res.append(ch ^ key)
#     return res
#
#
# def count_letters(text):
#     n = 0
#     for ch in text:
#         if ord('a') <= ch <= ord('z') or ord('A') <= ch <= ord('Z'):
#             n += 1
#     return n
#
#
# def compute_metric(text):
#     ideal_frequencies = {
#         # 'e': 11.162,
#         # 't':  9.356,
#         # 'a':  8.497,
#         # 'r':  7.587,
#         'i':  7.546,
#         # 'o':  7.507,
#         # 'n':  6.749,
#         # 's':  6.327,
#         # 'h':  6.094,
#     }
#     counts = {}
#     for ch in text:
#         ch = chr(ch).lower()
#         if ch not in counts:
#             counts[ch] = 0
#         counts[ch] += 1
#
#     frequencies = {}
#     text_len = len(text)
#     for f in counts:
#         frequencies[f] = counts[f] / text_len * 100
#
#     deviation = 0.0
#     for ch in ideal_frequencies:
#         if ch in frequencies:
#             deviation += pow(ideal_frequencies[ch] - frequencies[ch], 2)
#
#     return math.sqrt(deviation)
#
#
# # result_pt = b''
# best_score = 0
# for ct_hex in get_ciphertexts():
#     ct = binascii.unhexlify(ct_hex.strip())
#
#     # max_letters_key = 0
#     for key in range(0, 256):
#         decrypted = decrypt(ct, key)
#         s = count_letters(decrypted)
#         if s >= best_score:
#             best_score = s
#             print(best_score, ': ', decrypted)
#         # if 0 < m < min_metric:
#         #     min_metric = m
#         #     # max_letters_key = key
#         #     result_pt = decrypted
#
# # print(min_metric)
# # print(result_pt)
# # print(max_eng_letters, max_eng_letters_key)
# # print(decrypt(encrypted, max_eng_letters_key))


def encrypt_or_decrypt(pt, key):
    ct = bytearray()
    for i in range(len(pt)):
        ct.append(pt[i] ^ key[i % len(key)])
    return ct


plaintexts = [
    b"Burning 'em, if you ain't quick and nimble",
    b"I go crazy when I hear a cymbal",
    b"Hey, brother, I don't know what to do here",
    b"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
]

key = b"ICE"

for pt in plaintexts:
    ct = encrypt_or_decrypt(pt, key)
    print(binascii.hexlify(ct))
