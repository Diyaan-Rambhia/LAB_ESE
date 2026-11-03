p = 17
a = 2
G = (5, 1)

def inverse(x):
    return pow(x % p, -1, p)

def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        m = ((3*x1*x1 + a) * inverse(2*y1)) % p
    else:
        m = ((y2-y1) * inverse(x2-x1)) % p

    x3 = (m*m - x1 - x2) % p
    y3 = (m*(x1-x3) - y1) % p

    return (x3, y3)

def multiply(k, P):
    result = None

    while k > 0:
        if k % 2 == 1:
            result = add(result, P)

        P = add(P, P)
        k //= 2

    return result

def encrypt(message, public_key, k):
    message_point = multiply(message, G)
    c1 = multiply(k, G)
    c2 = add(message_point, multiply(k, public_key))

    return c1, c2

def decrypt(cipher, private_key):
    c1, c2 = cipher
    shared = multiply(private_key, c1)

    if shared is not None:
        shared = (shared[0], (-shared[1]) % p)

    decoded = add(c2, shared)

    for i in range(19):
        if multiply(i, G) == decoded:
            return i

    return "Message not found"

private_key = 7
public_key = multiply(private_key, G)

cipher = encrypt(5, public_key, 3)
print(cipher)
print(decrypt(cipher, private_key))

def decrypt(cipher, private_key):
    c1, c2 = cipher

    shared = multiply(private_key, c1)

    if shared is not None:
        shared = (shared[0], (-shared[1]) % p)

    message_point = add(c2, shared)

    return message_point

print(decrypt(cipher, private_key))