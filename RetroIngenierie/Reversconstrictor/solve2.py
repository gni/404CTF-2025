from encrypt_key import * #j'ai renommé la lib

rev_encode = {encode_password(bytes([i])): chr(i) for i in range(256)}


def xor(a, b):
    return bytes(b1 ^ b2 for b1, b2 in zip(a, b))


k = encrypt_key(
    0x6D39D56F8A40A6BBE43A82A53B2C762EA780C21A32C6B3EF765D3A54F3432432F3E6D39D56F8A40A6BBE43A82A53B2C762EA780C21A32C6B3EF765D3A54F3432432F3E
)

xor_ed = b'\xe9J\x1aB\xe2\xc5\xf3S\'\xd6>\n$\x94\x1a\x07\'F\xc6\xa1\x07\xb7\xcc\xec\xe1\x84\xec\xac\xe4\xd64\x8f\xc3\x12\x04\x16$n\x15\xec\xe1\xaee5\xc7\xecOX"\x98EO\x1f2\xb4\x15\xc4\xed\xf4\xcd$\xd3\xd3u\xc2\xf8\xc6\xae\x06\x08\xcd\xff\xe0(\xe9\xb0\xe7\xde6\x90\xcc\xfd\x02}%\x1a\x1a\xc9#\x10\xc2\x86\x06\x08\xcd\xfe&\xb8K\x0f)\x9a\xb6\xb9\x02\x17\xa0\xd8\xe4]\x98\xf5*\x154<\x06\x875\xbd\x05@\xe6\x88\xe3&6%\xcc\x18\x06\\%\xa4\x1a7!\xfe\xc3\xae\x06\x08\xcd\xff\xe2\x18\xe2x\xe0\x927x\r\xfa\xa6\xbd\xe67\x97\xf7\xe5)f\x94\xc8\xbdv\r\xef\x12\x1bZ\xe8e\xf3S\'\xd6>\n"8\x1be\x9c\xdf\xe8\x9b\x06\xb7\x0b3V\x1f\xedN\x87\xbbI!C>8z%\xc0\xeaM\xb5\xd1p\xd1\x0f|A\xd7B\x03\xc54\xd5T\xb9\xfd\x88;\xbf\x10\x81L\x90L\x0b\xff\xed\xe1\xe5dQ\xc4\x17\xd5\xafUl\xec'

flag_encoded = xor(k, xor_ed)

flag = ""
for i in range(0, len(flag_encoded), 6):
    flag += rev_encode[flag_encoded[i:i+6]]

print(flag)