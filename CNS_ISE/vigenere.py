def vigenere(text, key):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    j = 0

    for ch in text.upper():
        if ch.isalpha():
            shift = letters.index(key[j % len(key)].upper())
            result += letters[(letters.index(ch) + shift) % 26]
            j += 1
        else:
            result += ch

    return result

print(vigenere("HELLO", "KEY"))

letters = "abcdefghijklmnopqrstuvwxyz"

def decrypt(cipher, key):
    result = ""
    j = 0

    for ch in cipher.lower():
        if ch in letters:
            a = letters.index(ch)
            b = letters.index(key[j % len(key)].lower())
            result += letters[(a - b) % 26]
            j += 1
        else:
            result += ch

    return result

print(decrypt("lxfopvefrnhr", "lemon"))