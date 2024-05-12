def left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF


def md5(message):

    padding_length = 0
    if (len(message) + 64) % 512:
        message += "1"
        padding_length = 512 - ((len(message) + 64) % 512)
        
    message += "0" * padding_length
    print(f"Padding Length  : {padding_length+1}")

    message_words = [int(message[i : i + 32], 2) for i in range(0, len(message), 32)]
    original_message_length = len(message) - 64
    message_words.append(original_message_length)

    K = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]
    print(f"Chaining variables are : {K}")

    def F(x, y, z):
        return (x & y) | (~x & z)

    a, b, c, d = K
    for i in range(0, len(message_words), 16):
        f = F(b, c, d)
        g = (i >> 2) & 0x03
        for j in range(16):
            if i + j < len(message_words):
                temp = (a + f + message_words[i + j] + g) & 0xFFFFFFFF
                a = d
                d = c
                c = b
                b = (b + left_rotate(temp, 7)) & 0xFFFFFFFF
    digest = format(a, "08x")
    digest += format(b, "08x")
    digest += format(c, "08x")
    digest += format(d, "08x")
    return digest

import random

random_message = "".join([random.choice(["0", "1"]) for _ in range(1000)])
print("Random 1000-bit message:", random_message)
first_round_res = md5(random_message)
print("After First Round :", first_round_res)
