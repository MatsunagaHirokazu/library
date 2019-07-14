# -*- coding: utf-8 -*-
# 区間加算・区間和クエリ

""" AOJでTLEする
class LazyPropagationSegmentTree:
    def __init__(self, initList):
        self.size = len(initList)
        self.N = 2 ** self.size.bit_length()
        self.node = [0] * (2 * self.N - 1)
        self.lazy = [0] * (2 * self.N - 1)
        for i in range(self.size):
            self.node[i + self.N - 1] = initList[i]
        for i in range(self.N - 2, -1, -1):
            self.node[i] = self.node[i * 2 + 1] + self.node[i * 2 + 2]

    def _eval(self, k, l, r):
        # k 番目のノードについて遅延評価を行う
        if self.lazy[k] != 0:
            self.node[k] += self.lazy[k]
            if r - l > 1:
                self.lazy[2 * k + 1] += self.lazy[k] // 2
                self.lazy[2 * k + 2] += self.lazy[k] // 2
            self.lazy[k] = 0

    def add(self, a, b, x, k=0, l=0, r=-1):
        # 0-indexedの[a, b)であることに注意、[a, b]に足すなら.add(a, b+1)
        if (r < 0):
            r = self.N
        self._eval(k, l, r)
        if b <= l or r <= a:
            return
        elif a <= l and r <= b:
            self.lazy[k] += (r - l) * x
            self._eval(k, l, r)
        else:
            self.add(a, b, x, 2 * k + 1, l, (l + r) // 2)
            self.add(a, b, x, 2 * k + 2, (l + r) // 2, r)
            self.node[k] = self.node[2 * k + 1] + self.node[2 * k + 2]

    def getSum(self, a, b, k=0, l=0, r=-1):
        # 0-indexedの[a, b)であることに注意
        if (r < 0):
            r = self.N
        if (b <= l or r <= a):
            return 0

        self._eval(k, l, r)
        if (a <= l and r <= b):
            return self.node[k]
        vl = self.getSum(a, b, 2*k+1, l, (l+r)//2)
        vr = self.getSum(a, b, 2*k+2, (l+r)//2, r)
        return vl+vr


N, Q = map(int, input().split())
tree = LazyPropagationSegmentTree([0 for i in range(N)])
for i in range(Q):
    c = list(map(int, input().split()))
    if len(c) == 4:
        s, t, x = c[1:]
        tree.add(s-1, t, x)
    else:
        s, t = c[1:]
        print(tree.getSum(s-1, t))
"""
