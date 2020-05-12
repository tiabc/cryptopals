from vigenere import *

ct = ct_from_base64_file('6.txt')
pt = break_vigenere(ct)

print(pt)
