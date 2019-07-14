# 方法1 これは速い ← そうでもない
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


# 方法2 mod計算込みのもの
def cmb(N, K, MOD):
    factorial = [1] * (N + K)
    for k in range(1, N + K - 1):
        factorial[k + 1] = (factorial[k] * (k + 1)) % MOD

    fact_inv = [1] * (N + K)
    fact_inv[N + K - 1] = pow(factorial[N + K - 1], MOD - 2, MOD)
    for k in range(N + K - 1, 0, -1):
        fact_inv[k - 1] = (fact_inv[k] * k) % MOD

    if N < 0 or K < 0 or N < K:
        return 0
    else:
        return (factorial[N] * fact_inv[K] * fact_inv[N - K]) % MOD
