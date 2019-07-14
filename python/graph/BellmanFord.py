# -*- coding: utf-8 -*-
# 解法1　これでTLEならlistにする
import collections


class BellmanFord():
    def __init__(self):
        self.edges = []

    def add(self, u, v, d, directed=False):
        """
        u = from, v = to, d = cost
        directed = Trueのとき、有向グラフである。
        """
        if directed is False:
            self.edges.append([u, v, d])
            self.edges.append([v, u, d])
        else:
            self.edges.append([u, v, d])

    def BellmanFord_search(self, s):
        """
        次のBellmanFord_negative_boolまで考慮した時には、0-indexedであることに注意
        :param s: 始点
        :return: d[i] 始点sから各点iまでの最短経路
        """
        d = collections.defaultdict(lambda: float('inf'))
        d[s] = 0
        numEdges = len(self.edges)
        while True:
            update = False
            for i in range(numEdges):
                e = self.edges[i]
                # e: 辺iについて [from,to,cost]
                if d[e[0]] != float("inf") and d[e[1]] > d[e[0]] + e[2]:
                    d[e[1]] = d[e[0]] + e[2]
                    update = True
            if not update:
                break
        return d

    def BellmanFord_negative_bool(self, numNodes, zero_indexed=False):
        # 負の閉路の検出, Trueなら負の閉路が存在する
        d = collections.defaultdict(lambda: float('inf'))
        d[0] = 0
        numEdges = len(self.edges)
        for i in range(numNodes):
            for j in range(numEdges):
                e = self.edges[j]
                if d[e[1]] > d[e[0]] + e[2]:
                    d[e[1]] = d[e[0]] + e[2]
                    if i == numNodes-1:
                        return True
        return False

# 解法2


class BellmanFord():
    def __init__(self, N):
        self.N = N
        self.edges = []

    def add(self, u, v, d, directed=False):
        """
        u = from, v = to, d = cost
        directed = Trueのとき、有向グラフである。
        """
        if directed is False:
            self.edges.append([u, v, d])
            self.edges.append([v, u, d])
        else:
            self.edges.append([u, v, d])

    def BellmanFord_search(self, s):
        """
        :param s: 始点
        :return: d[i] 始点sから各点iまでの最短経路
        """
        d = [float('inf') for i in range(self.N)]
        d[s] = 0
        numEdges = len(self.edges)
        while True:
            update = False
            for i in range(numEdges):
                e = self.edges[i]
                # e: 辺iについて [from,to,cost]
                if d[e[0]] != float("inf") and d[e[1]] > d[e[0]] + e[2]:
                    d[e[1]] = d[e[0]] + e[2]
                    update = True
            if not update:
                break
        return d

    def BellmanFord_negative_bool(self, numNodes):
        # 負の閉路の検出, Trueなら負の閉路が存在する
        d = [float('inf') for i in range(self.N)]
        d[0] = 0
        numEdges = len(self.edges)
        for i in range(numNodes):
            for j in range(numEdges):
                e = self.edges[j]
                if d[e[1]] > d[e[0]] + e[2]:
                    d[e[1]] = d[e[0]] + e[2]
                    if i == numNodes-1:
                        return True
        return False
