# Converts n to base b as a list of integers between 0 and b-1
# Most-significant digit on the left


def convertToBase(n, b):
    if(n < 2):
        return [n]
    temp = n
    ans = []
    while(temp != 0):
        ans = [temp % b] + ans
        temp //= b
    return ans

# Takes integer n and odd prime p
# Returns both square roots of n modulo p as a pair (a,b)
# r^2 \equiv n \mod p を満たすrを返す
# Returns () if no root


def Cipolla(n, p):
    n %= p
    if(n == 0 or n == 1):
        return (n, -n % p)
    phi = p - 1
    if(pow(n, phi//2, p) != 1):
        return ()
    if(p % 4 == 3):
        ans = pow(n, (p+1)//4, p)
        return (ans, -ans % p)
    aa = 0
    for i in range(1, p):
        temp = pow((i*i-n) % p, phi//2, p)
        if(temp == phi):
            aa = i
            break
    exponent = convertToBase((p+1)//2, 2)

    def cipollaMult(a: tuple, c: tuple, w, p):
        return ((a[0]*c[0]+a[1]*c[1]*w) % p, (a[0]*c[1]+a[1]*c[0]) % p)
    x1 = (aa, 1)
    x2 = cipollaMult(x1, x1, aa*aa-n, p)
    for i in range(1, len(exponent)):
        if(exponent[i] == 0):
            x2 = cipollaMult(x2, x1, aa*aa-n, p)
            x1 = cipollaMult(x1, x1, aa*aa-n, p)
        else:
            x1 = cipollaMult(x1, x2, aa*aa-n, p)
            x2 = cipollaMult(x2, x2, aa*aa-n, p)
    return (x1[0], -x1[0] % p)
