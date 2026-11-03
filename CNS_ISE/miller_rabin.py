def miller_rabin(n, a=2):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    x = pow(a, d, n)
    if x == 1 or x == n-1:
        return True

    for _ in range(s-1):
        x = pow(x, 2, n)
        if x == n-1:
            return True
    return False

print(miller_rabin(17))