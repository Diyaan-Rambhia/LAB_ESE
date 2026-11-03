letters = "abcdefghijklmnopqrstuvwxyz"

p = 17
a = 2
G = (5, 1)
n = 19

def hash_message(message):
    return sum(letters.index(c) for c in message.lower()) + 1

def inverse(x, mod):
    return pow(x % mod, -1, mod)

def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1+y2) % p == 0:
        return None

    if P == Q:
        m = ((3*x1*x1+a) * inverse(2*y1, p)) % p
    else:
        m = ((y2-y1) * inverse(x2-x1, p)) % p

    x3 = (m*m-x1-x2) % p
    y3 = (m*(x1-x3)-y1) % p

    return x3, y3

def multiply(k, P):
    result = None

    while k > 0:
        if k % 2 == 1:
            result = add(result, P)

        P = add(P, P)
        k //= 2

    return result

private_key = 7
public_key = multiply(private_key, G)

def sign(message):
    h = hash_message(message)
    k = 3

    point = multiply(k, G)
    r = point[0] % n
    s = (inverse(k, n) * (h + private_key*r)) % n

    return r, s

def verify(message, signature):
    r, s = signature

    if not (0 < r < n and 0 < s < n):
        return False

    h = hash_message(message)
    w = inverse(s, n)

    u1 = (h*w) % n
    u2 = (r*w) % n

    P = add(multiply(u1, G), multiply(u2, public_key))

    return P is not None and P[0] % n == r

s = sign("hi")
print(s)
print(verify("hi", s))