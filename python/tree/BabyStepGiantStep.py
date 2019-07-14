import math


def BabyStepGiantStep(g, r, p):
    '''
    Solve for x in r = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = math.ceil(math.sqrt(p - 1))
    tbl = {pow(g, i, p): i for i in range(N)}
    c = pow(g, N * (p - 2), p)
    for j in range(N):
        y = (r * pow(c, j, p)) % p
        if y in tbl:
            if j * N + tbl[y] > 1:
                return j * N + tbl[y]
    return -1
