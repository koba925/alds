# 7_A.py

def grade(m, f, r):
    if m == -1 or f == -1: return "F"
    t = m + f
    if 80 <= t: return "A"
    if 65 <= t: return "B"
    if 50 <= t: return "C"
    if 30 <= t: 
        if 50 <= r: return "C"
        else: return "D"
    else: return "F" 


while True:
    m, f, r = [int(e) for e in input().split()]
    if m == -1 and f == -1 and r == -1:
        break
    print(grade(m, f, r))
