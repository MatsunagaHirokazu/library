# 二項係数をたくさん求めるときはこっちの方が多分速い
def makeTableMod(N, mod=10 ** 9 + 7):
    fac = [1 for i in range(N)]
    finv = [1 for i in range(N)]
    inv = [1 for i in range(N)]
    for i in range(2, N):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
    return fac, finv


def binomialCoefficient(N, r, mod=10 ** 9 + 7):
    if N < r:
        return 0
    else:
        return fac[N] * (finv[r] * finv[N - r] % mod) % mod


fac, finv = makeTableMod(N+1)
mod = 10 ** 9 + 7

# modなし


def makeTable(N):
    fac = [1 for i in range(N)]
    for i in range(2, N):
        fac[i] = fac[i - 1] * i
    return fac


def binomialCoefficient(N, r):
    if N < r:
        return 0
    else:
        return fac[N] // (fac[r] * fac[N - r])
