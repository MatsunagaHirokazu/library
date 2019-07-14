def gcd(a, b):
    """
    自然数a, b の最大公約数を求める
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def ExtendedEuclidianAlgorithms(a, b):
    """
    返り値: 自然数a, bの最小公倍数d, ax+by=gcd(a, b)を満たす(x, y)が、
    (d, x, y)のtuple
    d = 1ならxはaの逆元(inverse element)
    """
    d, c1 = a, b
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while c1 != 0:
        m = d % c1
        q = d // c1
        d, c1 = c1, m
        x0, x1 = x1, (x0 - q * x1)
        y0, y1 = y1, (y0 - q * y1)
    return d, x0, y0


def invmod(a, mod=10 ** 9 + 7):
    # ax ≡ 1 (mod m)、aのmに対する逆元を求める
    _, inv, _ = ExtendedEuclidianAlgorithms(a, mod)
    return inv % mod


def invmod(a, mod):
    # mod が素数の時に成立する, 上の方が早いしmodが素数でなくても成立する
    return pow(a, mod - 2, mod)


def unknown(x, y, mod=10 ** 9 + 7):
    """
    x, yが互いにその時、x*z - a*mod = y となるような唯一のz(0 < z < mod)を求める
    """
    g, a, b = ExtendedEuclidianAlgorithms(x, mod)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return a*y % mod
