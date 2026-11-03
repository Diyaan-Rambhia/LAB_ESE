def diffie_hellman(p, g, a, b):
    A = pow(g, a, p)
    B = pow(g, b, p)

    key1 = pow(B, a, p)
    key2 = pow(A, b, p)

    print("Alice public key:", A)
    print("Bob public key:", B)
    print("Alice shared key:", key1)
    print("Bob shared key:", key2)

diffie_hellman(23, 5, 6, 15)