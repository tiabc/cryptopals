from block_crypto import *

text = b"YELLOW SUBMARINE"
text_with_padding = add_pkcs7_padding(text, 20)

print(text_with_padding)
