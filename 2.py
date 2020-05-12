import binascii
import base64

str1_hex = '1c0111001f010100061a024b53535009181c'
str2_hex = '686974207468652062756c6c277320657965'

str1 = binascii.unhexlify(str1_hex)
str2 = binascii.unhexlify(str2_hex)

res = bytearray(b'')
for i in range(len(str1)):
    res.append(str1[i] ^ str2[i])

print(binascii.hexlify(res))

# print(base64.b64encode(res))
