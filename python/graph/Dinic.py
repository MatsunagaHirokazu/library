# -*- coding: utf-8 -*-
import collections
import queue


class Dinic:
    def __init__(self, N):
        self.N = N
        self.edges = collections.defaultdict(list)
        self.level = [0 for _ in range(self.N)]
        self.iter = [0 for _ in range(self.N)]

    def add(self, u, v, c, directed=True):
        """
        0-indexed
        u = from, v = to, c = cap
        directed = Trueなら、有向グラフである
        """
        if directed:
            self.edges[u].append([v, c, len(self.edges[v])])
            self.edges[v].append([u, 0, len(self.edges[u])-1])
        else:  # maybe needs to be rewritten by list
            self.edges[u].append([v, c, len(self.edges[u])])

    def bfs(self, s):
        self.level = [-1 for _ in range(self.N)]
        self.level[s] = 0
        que = queue.Queue()
        que.put(s)
        while not que.empty():
            v = que.get(s)
            for i in range(len(self.edges[v])):
                e = self.edges[v][i]
                if e[1] > 0 and self.level[e[0]] < 0:
                    self.level[e[0]] = self.level[v] + 1
                    que.put(e[0])

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.iter[v], len(self.edges[v])):
            self.iter[v] = i
            e = self.edges[v][i]
            if e[1] > 0 and self.level[v] < self.level[e[0]]:
                d = self.dfs(e[0], t, min(f, e[1]))
                if d > 0:
                    e[1] -= d
                    self.edges[e[0]][e[2]][1] += d
                    return d
        return 0

    def maxFlow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return flow
            self.iter = [0 for _ in range(self.N)]
            f = self.dfs(s, t, float('inf'))
            while f > 0:
                flow += f
                f = self.dfs(s, t, float('inf'))
