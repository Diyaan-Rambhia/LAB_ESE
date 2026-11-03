def jacobi(a, n):
    result = 1
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0

def euler(n, a=2):
    if n < 2 or n % 2 == 0:
        return n == 2
    return pow(a, (n-1)//2, n) == jacobi(a, n) % n

print(euler(17))