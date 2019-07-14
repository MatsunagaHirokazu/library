# 1
class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * self.size

    def update(self, index, value):
        x = index
        while x < self.size:
            if self.tree[x] < value:
                self.tree[x] = value
            else:
                return
            x |= x + 1

    def maximum(self, index):
        # 半開区間[0,index)
        ret = 0
        x = index - 1
        while x >= 0:
            ret = max(ret, self.tree[x])
            x = (x & (x + 1)) - 1
        return ret

# 2


class Bit():
    def __init__(self, N):
        self.size = N
        self.bit = [0] * (self.size+1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

    def __str__(self):
        return str(self.bit)


""" 転倒数の計算方法
N = int(input())
A = list(map(int, input().split()))


ans = 0
tree = Bit(N)
for i in range(N):
    ans += i - tree.cumsum(A[i])
    tree.add(A[i], 1)

print(ans)
"""
