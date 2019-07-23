# cost が0以下でも使える
import collections


class MinCostFlowBellmanford:
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
        prevVertex = collections.defaultdict(int)
        prevEdge = collections.defaultdict(int)

        while flow > 0:
            dist = collections.defaultdict(lambda: float('inf'))
            dist[start] = 0
            update = True
            while update:
                update = False
                for v in range(self.N):
                    if dist[v] == float('inf'):
                        continue
                    for i, (to, cap, cost, _) in enumerate(self.edges[v]):
                        if cap > 0 and dist[to] > dist[v] + cost:
                            dist[to] = dist[v] + cost
                            prevVertex[to] = v
                            prevEdge[to] = i
                            update = True

            if dist[goal] == float('inf'):
                return -1

            d = flow
            v = goal
            while v != start:
                d = min(d, self.edges[prevVertex[v]][prevEdge[v]][1])
                v = prevVertex[v]
            flow -= d
            res += d * dist[goal]
            v = goal
            while v != start:
                e = self.edges[prevVertex[v]][prevEdge[v]]
                e[1] -= d
                self.edges[v][e[3]][1] += d
                v = prevVertex[v]
        return res
