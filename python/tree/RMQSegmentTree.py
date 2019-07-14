# RMQ
class RMQSegmentTree:
    def __init__(self, n, init_value):
        self.n = n
        self.init_val = init_value
        self.size = 2**n.bit_length()
        self.node = [self.init_val] * (2 * self.size)

    def _segfunc(self, x, y):
        # 目的に合わせてここをいじる
        # minならinitValueはfloat('inf), maxなら0のはず
        return min(x, y)

    def update(self, k, a):
        # k番目の値をaに変更
        k += self.size - 1
        self.node[k] = a
        while k >= 0:
            k = (k - 1) // 2
            self.node[k] = self._segfunc(
                self.node[k * 2 + 1], self.node[k * 2 + 2])

    def query(self, a, b):
        # [a, b)の最小値を求める
        # [a, b]ならquery(a, b+1)とする
        l, r = a + self.size, b + self.size
        res = self.init_val
        while l < r:
            if r & 1:
                r -= 1
                res = self._segfunc(res, self.node[r - 1])

            if l & 1:
                res = self._segfunc(res, self.node[l - 1])
                l += 1

            l >>= 1
            r >>= 1
        return res
