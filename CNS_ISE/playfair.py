def playfair(text, key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    chars = key + "".join(c for c in alphabet if c not in key)
    grid = [chars[i:i+5] for i in range(0, 25, 5)]

    text = text.upper().replace("J", "I")
    text = "".join(c for c in text if c.isalpha())
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        if a == b:
            pairs.append((a, "X"))
            i += 1
        else:
            pairs.append((a, b))
            i += 2

    result = ""
    for a, b in pairs:
        r1, c1 = next((r, row.index(a)) for r, row in enumerate(grid) if a in row)
        r2, c2 = next((r, row.index(b)) for r, row in enumerate(grid) if b in row)

        if r1 == r2:
            result += grid[r1][(c1+1)%5] + grid[r2][(c2+1)%5]
        elif c1 == c2:
            result += grid[(r1+1)%5][c1] + grid[(r2+1)%5][c2]
        else:
            result += grid[r1][c2] + grid[r2][c1]

    return result

print(playfair("HELLO", "MONARCHY"))

def decrypt(cipher, matrix):
    result = ""

    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]

        for r in range(5):
            for c in range(5):
                if matrix[r][c] == a:
                    r1, c1 = r, c
                if matrix[r][c] == b:
                    r2, c2 = r, c

        if r1 == r2:
            result += matrix[r1][(c1-1) % 5]
            result += matrix[r2][(c2-1) % 5]
        elif c1 == c2:
            result += matrix[(r1-1) % 5][c1]
            result += matrix[(r2-1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result

square = [
    "playf", "irex m".replace(" ", ""),
    "bcdgh", "knoqs", "tuv wz".replace(" ", "")
]
print(decrypt("", square))