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
