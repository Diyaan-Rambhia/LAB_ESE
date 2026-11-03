import random

def mono(text, uid):
    random.seed(uid)
    key = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(key)
    table = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", key))
    return "".join(table.get(c, c) for c in text.upper())

print(mono("HELLO", 1234567890))