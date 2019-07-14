# https://tjkendev.github.io/procon-library/python/union_find/pp_union_find.html
# 部分永続Union-Find
from bisect import bisect


class TimeUnionFind:
    def __init__(self, N):
        self.rank = [1] * N
        self.par = [i for i in range(N)]
        self.sz = [1] * N
        self.sizeoftime = [[(0, 1)] for i in range(N)]
        self.T = [float('inf')] * N

    def find(self, x, t):
        while self.T[x] <= t:
            x = self.par[x]
        return x

    def unite(self, x, y, t):
        px = self.find(x, t)
        py = self.find(y, t)
        if px == py:
            return 0
        if self.rank[py] < self.rank[px]:
            self.par[py] = px
            self.T[py] = t
            self.sz[px] += self.sz[py]
            self.sizeoftime[px].append((t, self.sz[px]))
        else:
            self.par[px] = py
            self.T[px] = t
            self.sz[py] += self.sz[px]
            self.sizeoftime[py].append((t, self.sz[py]))
            self.rank[py] = max(self.rank[py], self.rank[px]+1)
        return 1

    def size(self, x, t):
        y = self.find(x, t)
        idx = bisect(self.sizeoftime[y], (t, float('')))-1
        return self.sizeoftime[y][idx]
