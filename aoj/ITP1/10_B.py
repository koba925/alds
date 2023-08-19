# 10_B.py

from math import sqrt, sin, cos, radians

a, b, C = [float(e) for e in input().split()]
C = radians(C)

print(a*b*sin(C)/2)
print(a + b + sqrt(a**2 + b**2 - 2*a*b*cos(C)))
print(b*sin(C))
