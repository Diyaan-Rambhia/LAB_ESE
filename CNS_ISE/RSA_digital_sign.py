letters = "abcdefghijklmnopqrstuvwxyz"

def hash_message(message):
    return sum(letters.index(c) for c in message.lower()) + 1

p = 11
q = 13
n = p * q
phi = (p-1) * (q-1)

e = 7
d = pow(e, -1, phi)

def sign(message):
    h = hash_message(message)
    return pow(h, d, n)

def verify(message, signature):
    h = hash_message(message)
    return pow(signature, e, n) == h % n

s = sign("hello")
print(s)
print(verify("hello", s))