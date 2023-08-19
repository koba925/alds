# 10_C.py

def standard_deviation(s):
    average = sum(s) / len(s)
    variance = sum((e - average) ** 2 for e in s) / len(s)
    return variance ** 0.5

while True:
    n = int(input())
    if n == 0: break
    s = [int(e) for e in input().split()]
    print(standard_deviation(s))