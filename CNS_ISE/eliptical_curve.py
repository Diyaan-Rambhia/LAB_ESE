p, a, b = 17, 2, 2
G = (5, 1)

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
        m = (3*x1*x1 + a) * pow(2*y1, -1, p) % p
    else:
        m = (y2-y1) * pow(x2-x1, -1, p) % p

    x3 = (m*m-x1-x2) % p
    y3 = (m*(x1-x3)-y1) % p
    return (x3, y3)

def multiply(k, P):
    result = None
    while k:
        if k % 2:
            result = add(result, P)
        P = add(P, P)
        k //= 2
    return result

def ecc(private_key):
    public_key = multiply(private_key, G)
    print("Private key:", private_key)
    print("Public key:", public_key)

ecc(7)

def shared_secret(private_key, other_public_key):
    return multiply(private_key, other_public_key)

print(shared_secret(3, (10, 6)))