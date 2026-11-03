letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def ceaser(text, key):
    result = ""

    for ch in text:
        if ch in letters:
            result += letters[(letters.index(ch) + key) % 26]
        else:
            result += ch

    return result

print(ceaser("Hello", 3))

def decrypt(cipher, key):
    result = ""

    for ch in cipher.lower():
        if ch in letters:
            i = letters.index(ch)
            result += letters[(i - key) % 26]
        else:
            result += ch

    return result

print(decrypt("khoor", 3))