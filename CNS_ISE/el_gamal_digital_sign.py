letters = "abcdefghijklmnopqrstuvwxyz"

def hash_message(message):
    return sum(letters.index(c) for c in message.lower()) + 1

p = 23
g = 5

private_key = 6
public_key = pow(g, private_key, p)

def sign(message):
    h = hash_message(message)
    k = 7

    r = pow(g, k, p)
    s = (pow(k, -1, p-1) * (h-private_key*r)) % (p-1)

    return r, s

def verify(message, signature):
    r, s = signature

    if not (0 < r < p and 0 <= s < p-1):
        return False

    h = hash_message(message)

    left = pow(g, h, p)
    right = (pow(public_key, r, p) * pow(r, s, p)) % p

    return left == right

s = sign("hello")
print(s)
print(verify("hello", s))