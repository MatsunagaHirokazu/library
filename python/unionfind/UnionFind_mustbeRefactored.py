"""
ノードの数を指定する必要がないタイプ
各メソッドのたびにノードが追加される
"""


class UnionFind:
    def __init__(self, elems=None):
        class KeyDict(dict):
            def __missing__(self, key):
                self[key] = key
                return key

        self.parent = KeyDict()
        self.rank = collections.defaultdict(int)

        if elems is not None:
            for elem in elems:
                _, _ = self.parent[elem], self.rank[elem]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def finds(self, x):
        if self.parent[x] == x:
            del self.parent[x]
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def are_same(self, x, y):
        """
        以前の実装では、are_sameを呼び出すたびにx, yがunionfind木に追加されていたので、find関数を変更し、
        are_same用のfinds関数を実装した
        """
        return self.finds(x) == self.finds(y)

    def grouper(self):
        roots = [(x, self.find(x_par)) for x, x_par in self.parent.items()]
        root = operator.itemgetter(1)
        for _, group in itertools.groupby(sorted(roots, key=root), root):
            yield [x for x, _ in group]
