def rsa(p, q, message):
    n = p * q
    phi = (p-1) * (q-1)
    e = 7

    while phi % e == 0 or gcd(e, phi) != 1:
        e += 1

    d = pow(e, -1, phi)
    encrypted = pow(message, e, n)
    decrypted = pow(encrypted, d, n)

    print("Public key:", (e, n))
    print("Private key:", (d, n))
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

rsa(11, 13, 9)

def decrypt(cipher, d, n):
    return pow(cipher, d, n)

print(decrypt(2790, 103, 3233))