# 1. RMQ
import sys
sys.setrecursionlimit(10**6)


class RMQ:
    def __init__(self, a):
        self.n = len(a)
        self.size = 2 ** (self.n - 1).bit_length()
        self.data = [(float('inf'), float('inf'))
                     for _ in range(2 * self.size - 1)]
        self.initialize(a)

    # Initialize data
    def initialize(self, a):
        for i in range(self.n):
            self.data[self.size + i - 1] = a[i][:]
        for i in range(self.size - 2, -1, -1):
            self.data[i] = min(self.data[i * 2 + 1], self.data[i * 2 + 2])[:]

    # Update ak as x
    def update(self, k, x):
        k += self.size - 1
        self.data[k] = x
        while k > 0:
            k = (k - 1) // 2
            self.data[k] = min(self.data[2 * k + 1], self.data[2 * k + 2])[:]

    # Min value in [l, r)
    def query(self, l, r):
        L = l + self.size
        R = r + self.size
        s = (float('inf'), float('inf'))
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R - 1])[:]
            if L & 1:
                s = min(s, self.data[L - 1])[:]
                L += 1
            L >>= 1
            R >>= 1
        return s


class LCA:
    def __init__(self, n):
        self.itr = 0
        self.edges = [[] for _ in range(n)]
        self.path = [0] * (2 * n - 1)
        self.depth = [0] * (2 * n - 1)
        self.index = [0] * n

    def add(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def initialize(self, root=0):
        self.euler_tour(-1, root, 0, 0)
        dat = list(zip(self.depth, self.path))
        self.rmq = RMQ(dat)

    def get_lca(self, u, v):
        l, r = self.index[u], self.index[v]
        if l > r:
            l, r = r, l
        return self.rmq.query(l, r + 1)[1]

    def euler_tour(self, prev, v, d, k):
        self.index[v] = k
        self.path[self.itr] = v
        self.depth[self.itr] = d
        self.itr += 1
        k += 1
        for dest in self.edges[v]:
            if prev == dest:
                continue
            k = self.euler_tour(v, dest, d + 1, k)
            self.path[self.itr] = v
            self.depth[self.itr] = d
            self.itr += 1
            k += 1
        return k


lca = LCA(N)
# add edges to lca object, and then initialize
lca.initialize()

# 2. Bisect
sys.setrecursionlimit(10 ** 6)


class LCA:
    def __init__(self, n):
        self.edges = [[] for _ in range(n)]
        self.n = n
        self.logn = len(bin(n)[2:])
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.depth = [0] * self.n

    def add(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def initialize(self, root=0):
        self.dfs(root, -1, 0)
        for k in range(self.logn - 1):
            for v in range(self.n):
                p_ = self.parent[k][v]
                if p_ >= 0:
                    self.parent[k + 1][v] = self.parent[k][p_]

    def dfs(self, v, p, dep):
        self.parent[0][v] = p
        self.depth[v] = dep
        for e in self.edges[v]:
            if e != p:
                self.dfs(e, v, dep + 1)

    def get_lca(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        dep_diff = self.depth[v] - self.depth[u]
        for k in range(self.logn):
            if dep_diff >> k & 1:
                v = self.parent[k][v]
        if u == v:
            return u
        for k in range(self.logn - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]


lca = LCA(N)
# add edges to lca object, and then initialize
lca.initialize()
