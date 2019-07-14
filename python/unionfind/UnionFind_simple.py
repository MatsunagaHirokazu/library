"""
シンプルで速いが、要素数を求めることはできない
graph = UnionFind(N)
"""


class UnionFind():
    def __init__(self, N):
        self.rank = [0] * N
        self.par = [i for i in range(N)]
        self.counter = [1] * N

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            z = self.counter[x] + self.counter[y]
            self.counter[x], self.counter[y] = z, z
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def size(self, x):
        x = self.find(x)
        return self.counter[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def groups(self):
        # return the number of connected nodes (if connected count as 1)
        s = set()
        for i in range(N):
            s.add(self.find(i))
        return len(s)
