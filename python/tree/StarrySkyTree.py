# glucoseからもらった
class StarrySkyTree:
    def __init__(self, num):
        leaf = 1 << (num-1).bit_length()
        self.leaf = leaf
        self.data = [0]*leaf*2
        self.lazy = [0]*leaf*2

    def indices(self, l, r):
        L, R = l+self.leaf, r+self.leaf
        lm = (L//(L & -L)) >> 1
        rm = (R//(R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1
            R >>= 1
        while L:
            yield L
            L >>= 1

    def _propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if v == 0:
                continue
            self.lazy[2*i-1] += v
            self.lazy[2*i] += v
            self.data[2*i-1] += v
            self.data[2*i] += v
            self.lazy[i-1] = 0

    def add(self, l, r, x):
        L, R = l+self.leaf, r+self.leaf
        while L < R:
            if L & 1:
                self.lazy[L-1] += x
                self.data[L-1] += x
                L += 1
            if R & 1:
                R -= 1
                self.lazy[R-1] += x
                self.data[R-1] += x
            L >>= 1
            R >>= 1
        for i in self.indices(l, r):
            self.data[i-1] = max(self.data[2*i-1],
                                 self.data[2*i])+self.lazy[i-1]

    def query(self, l, r):  # [l,r)
        self._propagates(*self.indices(l, r))
        L, R = l+self.leaf, r+self.leaf
        ret = 0
        while L < R:
            if L & 1:
                ret = max(ret, self.data[L-1])
                L += 1
            if R & 1:
                R -= 1
                ret = max(ret, self.data[R-1])
            L >>= 1
            R >>= 1
        return ret


"""
import sys
input = sys.stdin.readline
n = int(input())
maxT = 10**5+1
sst = StarrySkyTree(maxT)
L = []
for _ in range(n):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    L.append((s, t))
    sst.add(s, t, 1)
ans = sst.query(0, maxT)
for s, t in L:
    sst.add(s, t, -1)
    ans = min(ans, sst.query(0, maxT))
    sst.add(s, t, 1)
print(ans)
"""
