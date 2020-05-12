def add_pkcs7_padding(text, desired_length, padding=b"\04"):
    res = bytearray()
    res += text
    while len(res) < desired_length:
        res += padding
    return res

text = b"YELLOW SUBMARINE"
text_with_padding = add_pkcs7_padding(text, 20)

print(text_with_padding)