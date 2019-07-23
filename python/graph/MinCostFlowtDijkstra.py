# cost が0以上でないと使えない
from heapq import heappush, heappop
import collections


class MinCostFlowDijkstra:
    def __init__(self, N):
        self.N = N
        self.edges = collections.defaultdict(list)

    def add(self, fro, to, cap, cost, directed=True):
        # edge[fro]: to, cap, cost, rev(逆辺)
        if directed:
            self.edges[fro].append([to, cap, cost, len(self.edges[to])])
            self.edges[to].append([fro, 0, -cost, len(self.edges[fro]) - 1])
        else:  # TODO: must be Verified
            self.edges[fro].append([to, cap, cost, len(self.edges[to])])
            self.edges[to].append([fro, 0, -cost, len(self.edges[fro]) - 1])
            self.edges[to].append([fro, cap, cost, len(self.edges[fro])])
            self.edges[fro].append([to, 0, -cost, len(self.edges[to]) - 1])

    def minCostFlow(self, start, goal, flow):
        res = 0
        potential = collections.defaultdict(int)
        prevVertex = collections.defaultdict(int)
        prevEdge = collections.defaultdict(int)

        while flow > 0:
            dist = collections.defaultdict(lambda: float('inf'))
            dist[start] = 0
            que = []
            heappush(que, (0, start))

            while que:
                k, v = heappop(que)
                if dist[v] < k:
                    continue
                for i, (to, cap, cost, _) in enumerate(self.edges[v]):
                    if cap > 0 and dist[to] > dist[v] + cost + potential[v] - potential[to]:
                        dist[to] = dist[v] + cost + \
                            potential[v] - potential[to]
                        prevVertex[to] = v
                        prevEdge[to] = i
                        heappush(que, (dist[to], to))
            if dist[goal] == float('inf'):
                return -1

            for i in range(self.N):
                potential[i] += dist[i]

            d = flow
            v = goal
            while v != start:
                d = min(d, self.edges[prevVertex[v]][prevEdge[v]][1])
                v = prevVertex[v]
            flow -= d
            res += d * potential[goal]
            v = goal
            while v != start:
                e = self.edges[prevVertex[v]][prevEdge[v]]
                e[1] -= d
                self.edges[v][e[3]][1] += d
                v = prevVertex[v]
        return res
