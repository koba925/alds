# 7_D.py

class Matrix:

    def __init__(self, n, m):
        self.row = n
        self.col = m
        self.a = [[0 for e in range(m)] for e in range(n)]

    def read(self):
        self.a = [[int(e) for e in input().split()] for i in range(self.row)]
        return self

    def mul(self, other):
        result = Matrix(self.row, other.col)
        for i in range(self.row):
            for j in range(other.col):
                result.a[i][j] = sum([self.a[i][k] * other.a[k][j]
                                     for k in range(self.col)])
        return result

    def print(self):
        for r in self.a:
            print(*r)


n, m, l = [int(e) for e in input().split()]

a = Matrix(n, m).read()
b = Matrix(m, l).read()
a.mul(b).print()
