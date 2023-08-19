# 7_D.py

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reconstruct(pre_list, in_list):
    if len(pre_list) == 0:
        return None

    root_val  = pre_list[0]
    pos = in_list.index(root_val)
    yield from reconstruct(pre_list[1:pos + 1], in_list[:pos])
    yield from reconstruct(pre_list[pos + 1:], in_list[pos + 1:])
    yield root_val

n = int(input())
pre_list = [int(e) for e in input().split()]
in_list = [int(e) for e in input().split()]    
print(*reconstruct(pre_list, in_list))
