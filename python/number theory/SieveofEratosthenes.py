import math


def SieveofEratosthenes(N):
    if N < 2:
        raise ValueError('N should be more than 2')
    primeList = []
    limit = math.sqrt(N)
    data = [i + 1 for i in range(1, N)]
    while True:
        p = data[0]
        if limit <= p:
            return primeList + data
        primeList.append(p)
        data = [e for e in data if e % p != 0]
