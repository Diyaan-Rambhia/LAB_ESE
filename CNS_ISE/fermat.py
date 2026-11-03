def fermat(n, a=2):
    if n < 2:
        return False
    if n == 2:
        return True
    return pow(a, n-1, n) == 1

print(fermat(17))