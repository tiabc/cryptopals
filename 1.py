import binascii
import base64

hex_encoded = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

binary_str = binascii.unhexlify(hex_encoded)

b64_encoded = base64.b64encode(binary_str)
print(b64_encoded)
