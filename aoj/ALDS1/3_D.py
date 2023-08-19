# 3_D.py

class Pool:
    def __init__(self, left=None, area=None):
        self.left = left
        self.area = area

    def __repr__(self) -> str:
        return f"({self.left},{self.area})"

def add_pool(pools, left, area):
    while len(pools) > 0:
        if left < pools[-1].left:
            area += pools[-1].area
            pools.pop()
        else:
            break
    pools.append(Pool(left, area))

x = 0
pools = []
leftbank = []

for c in input():
    if c == "\\":
        leftbank.append(x)
    elif c == "/":
        if len(leftbank) > 0:
            left = leftbank.pop()
            add_pool(pools, left, x - left)
    x += 1

areas = [p.area for p in pools]
print(sum(areas))
print(len(pools), *areas)
