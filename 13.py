from block_crypto import *


def parse_query_string(string):
    vals = {}
    for kv in string.split('&'):
        kv_split = kv.split('=')
        vals[kv_split[0]] = kv_split[1]
    return vals


def encode_query_string(vals):
    pairs = []
    for k in vals:
        pairs.append(k + "=" + str(vals[k]).replace("&", "_").replace("=", "_"))

    return "&".join(pairs)


def profile_for(email):
    return encode_query_string({
        'email': email,
        'uid': 10,
        'role': 'user',
    })


def encrypt_email_query_string(email):
    key = b'\xa9\xe1\xa2/\x85\xe6\xec\xa3\x0e\x9e\xbc\xebz\x19\xe2\xad'
    pt = str.encode(profile_for(email))
    return aes_ecb_encrypt(pt, key)


def decrypt_email_query_string(ct):
    key = b'\xa9\xe1\xa2/\x85\xe6\xec\xa3\x0e\x9e\xbc\xebz\x19\xe2\xad'
    pt = aes_ecb_decrypt(ct, key).decode("UTF-8")
    return parse_query_string(pt)


ct = encrypt_email_query_string('it@atnr.pro')
profile = decrypt_email_query_string(ct)

print("it works:", ct, profile)

# attacker
ct_role_admin = encrypt_email_query_string("A" * 10 + "admin" + "\04" * 11)[16:32]
ct_for_substitute = encrypt_email_query_string("user@host.com")

final_ct = ct_for_substitute[0:32] + ct_role_admin

# proof
print(decrypt_email_query_string(final_ct))
