# ともにAOJでverify済み
import heapq


class Prim():
    # 無向グラフであるという前提に注意
    def __init__(self, N):
        self.edge = [[] for i in range(N)]
        self.N = N

    def add(self, u, v, d):
        """
        :params: u = from, v = to, d = cost
        0-indexedであることに注意、graph.add(u-1, v-1)とする必要がある
        """
        self.edge[u].append([d, v])  # コスト、e_toとなっていることに注意
        self.edge[v].append([d, u])

    def delete(self, u, v):
        self.edge[u] = [_ for _ in self.edge[u] if _[0] != v]
        self.edge[v] = [_ for _ in self.edge[v] if _[0] != u]

    def Prim_search(self):
        """
        :return: 最小全域木のコストの和
        """
        used = [True] * self.N  # True:不使用
        edgelist = []
        for e in self.edge[0]:
            heapq.heappush(edgelist, e)
        used[0] = False
        res = 0
        while len(edgelist) != 0:
            minedge = heapq.heappop(edgelist)
            if not used[minedge[1]]:
                continue
            v = minedge[1]
            used[v] = False
            for e in self.edge[v]:
                if used[e[1]]:
                    heapq.heappush(edgelist, e)
            res += minedge[0]
        return res


class Kruskal_UnionFind():
    # 無向グラフであるという前提に注意
    def __init__(self, N):
        self.edges = []
        self.rank = [0] * N
        self.par = [i for i in range(N)]
        self.counter = [1] * N

    def add(self, u, v, d):
        """
        :param u: 始点
        :param v: 終点
        :param d: コスト
        """
        self.edges.append([u, v, d])

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

    def Kruskal_search(self):
        """
        :return: 最小全域木のコストの和
        """
        edges = sorted(self.edges, key=lambda x: x[2])  # costでself.edgesをソートする
        res = 0
        for e in edges:
            if not self.same(e[0], e[1]):
                self.unite(e[0], e[1])
                res += e[2]
        return res
