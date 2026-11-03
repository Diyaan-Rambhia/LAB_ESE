letters = "abcdefghijklmnopqrstuvwxyz"

def hash_message(message):
    return sum(letters.index(c) for c in message.lower()) + 1

p = 23
q = 11
g = 4

private_key = 3
public_key = pow(g, private_key, p)

def sign(message):
    h = hash_message(message) % q
    k = 4

    r = pow(g, k, p) % q
    s = (pow(k, -1, q) * (h + private_key*r)) % q

    return r, s

def verify(message, signature):
    r, s = signature

    if not (0 < r < q and 0 < s < q):
        return False

    h = hash_message(message) % q
    w = pow(s, -1, q)

    u1 = (h*w) % q
    u2 = (r*w) % q

    v = (pow(g, u1, p) * pow(public_key, u2, p) % p) % q

    return v == r

s = sign("hi")
print(s)
print(verify("hi", s))