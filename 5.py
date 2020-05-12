import binascii
from lib import *

plaintexts = [
    b"Burning 'em, if you ain't quick and nimble",
    b"I go crazy when I hear a cymbal",
    b"Hey, brother, I don't know what to do here",
    b"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
]

key = b"ICE"

for pt in plaintexts:
    ct = xor_repeating_key(pt, key)
    print(binascii.hexlify(ct))
