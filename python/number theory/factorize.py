# 方法1 atcoderで使えない
import sympy
sympy.factorint(2016)


# 方法2
def factorize(n: int) -> dict:
    b = 2
    fct = {}
    while b * b <= n:
        while n % b == 0:
            n //= b
            if b in fct.keys():
                fct[b] += 1
            else:
                fct[b] = 1
        b = b + 1
    if n > 1:
        fct[n] = 1
    return fct
