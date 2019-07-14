# -*- coding: utf-8 -*-
# RMQ


class RMQSegmentTree:
    def __init__(self, initList, initValue):
        self.n = len(initList)
        self.initValue = initValue
        self.size = 2 ** self.n.bit_length()
        self.node = [initValue] * (2 * self.size)
        for i in range(self.n):
            self.node[i+self.size-1] = initList[i]
        for i in range(self.size-2, -1, -1):
            self.node[i] = self._segfunc(
                self.node[2 * i + 1], self.node[2 * i + 2])

    def _segfunc(self, x, y):
        # 目的に合わせてここをいじる
        # minならinitValueはfloat('inf), maxなら0のはず
        return min(x, y)

    def update(self, k, a):
        # k番目の値をaに変更
        k += self.size - 1
        self.node[k] = a
        while k >= 0:
            k = (k - 1) // 2
            self.node[k] = self._segfunc(
                self.node[k * 2 + 1], self.node[k * 2 + 2])

    def query(self, a, b):
        # [a, b)の最小値を求める
        # [a, b]ならquery(a, b+1)とする
        l, r = a + self.size, b + self.size
        res = self.initValue
        while l < r:
            if r & 1:
                r -= 1
                res = self._segfunc(res, self.node[r - 1])

            if l & 1:
                res = self._segfunc(res, self.node[l - 1])
                l += 1

            l >>= 1
            r >>= 1
        return res


"""
A = list(map(int, input().split()))
tree = SegmentTree(A, 10**9)  # 初期化
print(tree.node)
print(tree.query(1, 4))
"""
