# 5_C.py

from math import pi, sqrt, sin, cos

class Point2D():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x:.8f} {self.y:.8f}"

    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def scale(self, scale):
        return Point2D(self.x * scale, self.y * scale)

    def rotate(self, rad):
        return Point2D(self.x * cos(rad) - self.y * sin(rad),
                       self.x * sin(rad) + self.y * cos(rad))

    def distance(self, other):
        return other.sub(self).magnitude()

    def add(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def sub(self, other):
        return Point2D(self.x - other.x, self.y - other.y)


def kock_curve(n, p1, p2):

    def rec(n, p1, p2):
        if n == 0:
            return []

        move = p2.sub(p1)
        dist = p1.distance(p2)
        s = p1.add(move.scale(1 / 3))
        t = s.add(move.scale(1 / 3).rotate(pi / 3))
        u = p1.add(move.scale(2 / 3))
        return (rec(n - 1, p1, s) 
                + [s]
                + rec(n - 1, s, t)
                + [t]
                + rec(n - 1, t, u)
                + [u]
                + rec(n - 1, u, p2))

    return ([p1] +rec(n, p1, p2) + [p2])

n = int(input())
print(*kock_curve(n, Point2D(0, 0), Point2D(100, 0)), sep="\n")
