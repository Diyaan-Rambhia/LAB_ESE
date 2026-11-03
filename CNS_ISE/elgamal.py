def elgamal(p, g, x, k, message):
    y = pow(g, x, p)
    c1 = pow(g, k, p)
    c2 = message * pow(y, k, p) % p

    shared = pow(c1, x, p)
    decrypted = c2 * pow(shared, -1, p) % p

    print("Public key:", (p, g, y))
    print("Private key:", x)
    print("Encrypted:", (c1, c2))
    print("Decrypted:", decrypted)

elgamal(23, 5, 6, 3, 10)