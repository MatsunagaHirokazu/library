# -*- coding: utf8 -*-
# https://qiita.com/drken/items/f2ea4b58b0d21621bd51


class Enumeration():
    def __init__(self, N, K, MOD):
        self.factorial = [1] * (N + K)
        self.fact_inv = [1] * (N + K)
        self.MOD = MOD

        for k in range(1, N + K - 1):
            self.factorial[k + 1] = (self.factorial[k] * (k + 1)) % MOD

        self.fact_inv[N + K - 1] = pow(self.factorial[N + K - 1], MOD - 2, MOD)
        for k in range(N + K - 1, 0, -1):
            self.fact_inv[k - 1] = (self.fact_inv[k] * k) % MOD

    def cmb(self, n, r):
        if n < 0 or r < 0 or n < r:
            return 0
        else:
            return (self.factorial[n] * self.fact_inv[r] * self.fact_inv[n - r]) % self.MOD

    def Stirling(self, n, k):
        """
        n個の玉を区別する
        k個の箱を区別しない
        各箱に入る玉の個数は「1個以上」
        """
        res = 0
        for i in range(0, k + 1):
            add = self.cmb(k, i) * ((i ** n) % self.MOD)
            if ((k - i) % 2 == 0):
                res += add
            else:
                res -= add

        res //= self.factorial[k]
        return res

    def Bell(self, n, k):
        """
        n個の玉を区別する
        k個の箱を区別しない
        各箱に入る玉の個数に制限なし
        """
        if k > n:
            k = n
        jsum = [0] * (k + 2)
        for j in range(0, k + 1):
            add = self.fact_inv[j]
            if (j % 2 == 0):
                jsum[j+1] = jsum[j] + add
            else:
                jsum[j+1] = jsum[j] - add
        res = 0
        for i in range(0, k + 1):
            res += ((i ** n) % self.MOD) * \
                self.fact_inv[i] * jsum[k - i + 1]

        return res % self.MOD

    def Bell2(self, n, k):
        """
        Bell数の、Stirling数を用いた実装
        """
        if k > n:
            k = n
        res = 0
        for i in range(0, k + 1):
            res += self.Stirling(n, i)

        return res


def Partition(n):
    """
    n個の玉、n個の箱を区別しない、各箱に入る玉の個数に制限なし　P(n, n)
    つまり、n個の要素を何個かの整数の和として表す方法の数
    分割数の、漸化式を用いたO(n**(3/2))の実装
    """
    P = [0 for i in range(n+1)]
    P[0] = 1
    for i in range(n+1):
        j = 1
        while i - (j * j * 3 - j) / 2 >= 0:
            #print(i, i - (j * j * 3 - j)//2, i - (j * j * 3 + j)//2)
            if (j - 1) % 2 == 0:
                P[i] += P[i - (j * j * 3 - j) // 2]
                if (i - (j * j * 3 + j) // 2 >= 0):
                    P[i] += P[i - (j * j * 3 + j) // 2]
            else:
                P[i] -= P[i - (j * j * 3 - j) // 2]
                if (i - (j * j * 3 + j) // 2 >= 0):
                    P[i] -= P[i - (j * j * 3 + j) // 2]
            j += 1

    if n < 0:
        return 0
    else:
        return P[n]


def Partition2(n, k):
    """
    n個の玉、k個の箱を区別しない
    各箱に入る玉の個数に制限なし
    分割数の、漸化式を用いたO(nk)の実装
    """
    P = [[0 for i in range(k+1)] for i in range(n+1)]
    for i in range(k+1):
        P[0][i] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            P[i][j] = P[i][j-1] + (P[i-j][j] if i >= j else 0)
    if n < 0 or k < 0:
        return 0
    else:
        return P[n][k]
