# 2_B.py Range Sum Query (RSQ)

from sys import stdin

# AC 2.71s 18136KB
# can be much faster optimizing for sum

class RangeSumQuery:
    def __init__(self, size) -> None:
        def actual_size(size):
            asize = 1
            while asize < size:
                asize *= 2
            return asize

        self.size = size
        self.asize = actual_size(size)
        self.vals = [0] * (self.asize * 2 - 1)

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return i * 2 + 1

    def right_child(self, i):
        return i * 2 + 2

    def add(self, i, x):
        i += self.asize - 1
        self.vals[i] += x
        while i > 0:
            i = self.parent(i)
            self.vals[i] = self.vals[self.left_child(i)] + self.vals[self.right_child(i)]

    # calc sum of [s, t)
    def get_sum(self, s, t):
        def _get_sum(s, t, i, l, r):
            if r <= s or t <= l:
                return 0
            if s <= l and r <= t:
                return self.vals[i]
            vl = _get_sum(s, t, self.left_child(i), l, (l + r) // 2)
            vr = _get_sum(s, t, self.right_child(i), (l + r) // 2, r)
            return vl + vr

        return _get_sum(s, t, 0, 0, self.asize)


n, q = [int(e) for e in stdin.readline().split()]
a = RangeSumQuery(n)

for line in stdin.readlines():
    com, *param = [int(e) for e in line.split()]
    if com == 0:
        a.add(param[0] - 1, param[1])
    elif com == 1:
        print(a.get_sum(param[0] - 1, param[1]))
