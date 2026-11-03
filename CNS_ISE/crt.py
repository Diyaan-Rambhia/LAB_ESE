def crt(a, m):
    M = 1

    for x in m:
        M *= x

    result = 0

    for i in range(len(m)):
        Mi = M // m[i]
        inverse = pow(Mi, -1, m[i])
        result += a[i] * Mi * inverse

    return result % M

# x = 2 mod 3
# x = 3 mod 5
# x = 2 mod 7

print(crt([2, 3, 2], [3, 5, 7]))