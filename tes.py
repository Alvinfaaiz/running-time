import struct
import time

def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff


# ===================== SHA-1 ITERATIVE =====================
def sha1_iterative(message: bytes):
    ml = len(message) * 8
    message += b'\x80'
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    message += struct.pack('>Q', ml)

    h0, h1, h2, h3, h4 = (
        0x67452301,
        0xEFCDAB89,
        0x98BADCFE,
        0x10325476,
        0xC3D2E1F0
    )

    for i in range(0, len(message), 64):
        w = list(struct.unpack('>16I', message[i:i+64]))
        for j in range(16, 80):
            w.append(left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1))

        a, b, c, d, e = h0, h1, h2, h3, h4

        for j in range(80):
            if j < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif j < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif j < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff
            e, d, c, b, a = d, c, left_rotate(b, 30), a, temp

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    return f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}"


# ===================== SHA-1 RECURSIVE =====================
def sha1_recursive_round(j, a, b, c, d, e, w):
    if j == 80:
        return a, b, c, d, e

    if j < 20:
        f = (b & c) | ((~b) & d)
        k = 0x5A827999
    elif j < 40:
        f = b ^ c ^ d
        k = 0x6ED9EBA1
    elif j < 60:
        f = (b & c) | (b & d) | (c & d)
        k = 0x8F1BBCDC
    else:
        f = b ^ c ^ d
        k = 0xCA62C1D6

    temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff
    return sha1_recursive_round(
        j + 1,
        temp,
        a,
        left_rotate(b, 30),
        c,
        d,
        w
    )


def sha1_recursive(message: bytes):
    ml = len(message) * 8
    message += b'\x80'
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    message += struct.pack('>Q', ml)

    h0, h1, h2, h3, h4 = (
        0x67452301,
        0xEFCDAB89,
        0x98BADCFE,
        0x10325476,
        0xC3D2E1F0
    )

    for i in range(0, len(message), 64):
        w = list(struct.unpack('>16I', message[i:i+64]))
        for j in range(16, 80):
            w.append(left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1))

        a, b, c, d, e = sha1_recursive_round(
            0, h0, h1, h2, h3, h4, w
        )

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    return f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}"


# ===================== MAIN =====================
if __name__ == "__main__":
    text = input("Masukkan teks: ")
    data = text.encode()

    start = time.perf_counter()
    hash_iter = sha1_iterative(data)
    time_iter = time.perf_counter() - start

    start = time.perf_counter()
    hash_rec = sha1_recursive(data)
    time_rec = time.perf_counter() - start

    print("\n=== HASIL ===")
    print("SHA-1 Iteratif :", hash_iter)
    print("SHA-1 Rekursif :", hash_rec)

    print("\n=== RUNNING TIME ===")
    print(f"Iteratif  : {time_iter:.8f} detik")
    print(f"Rekursif  : {time_rec:.8f} detik")

    print("\n=== PERBANDINGAN ===")
    if time_iter < time_rec:
        print("Iteratif lebih cepat dari Rekursif")
    else:
        print("Rekursif lebih cepat dari Iteratif")
