"""
要素数、要素を求めることができる
最初にノードの個数を指定する必要がある
uf = UnionFind(range(1, N))など
各メソッドで、ノードを追加しない
"""
import collections


class UnitDict(dict):

    def __init__(self, iterable=None, wrapper=lambda x: x):
        super().__init__(self)
        self.wrapper = wrapper
        if iterable is not None:
            self.update(iterable)

    def __missing__(self, key):
        self[key] = self.wrapper(key)
        return self[key]


class UnionFind(object):

    def __init__(self, nodes=None):
        self.par = UnitDict(wrapper=lambda x: x)
        self.rank = collections.defaultdict(int)
        self.groups = UnitDict(wrapper=lambda x: {x})
        if nodes is not None:
            for node in nodes:
                _, _, _ = self.par[node], self.rank[node], self.groups[node]

    def root(self, node):
        if self.par[node] == node:
            return node
        else:
            r = self.root(self.par[node])
            self.par[node] = r
            return r

    def are_same(self, node1, node2):
        return self.root(node1) == self.root(node2)

    def elements(self, node):
        return self.groups[self.root(node)]

    def size(self, node):
        return len(self.elements(node))

    def unite(self, node1, node2):
        x = self.root(node1)
        y = self.root(node2)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            self.par[y] = x
            self.groups[x].update(self.groups[y])
            self.groups[y].clear()
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def grouper(self):
        roots = [x for x in self.par.keys()]
        groups = []
        for root in roots:
            if list(self.elements(root)) not in groups:
                groups.append(list(self.elements(root)))
        return groups
