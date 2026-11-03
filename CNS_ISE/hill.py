def hill(text):
    key = [[3, 3], [2, 5]]
    text = text.upper().replace(" ", "")
    if len(text) % 2:
        text += "X"

    result = ""
    for i in range(0, len(text), 2):
        a = ord(text[i]) - 65
        b = ord(text[i+1]) - 65
        x = (key[0][0]*a + key[0][1]*b) % 26
        y = (key[1][0]*a + key[1][1]*b) % 26
        result += chr(x+65) + chr(y+65)

    return result

print(hill("HELP"))