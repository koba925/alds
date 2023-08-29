# 2次元リストをflatするだけならsumに初期値を指定すれば簡単 ただし遅そう
print(sum([[1, 2], [3, 4], [5, 6]], []))


def flatten_2D(x):
    return [z for y in x for z in y]


print(flatten_2D([[1, 2], [3, 4], [5, 6]]))

# 再帰的にflattenする場合


def flatten_loop(x):
    ret = []
    for y in x:
        if isinstance(y, list):
            ret += flatten(y)
        else:
            ret += [y]
    return ret


# 再帰的にflattenする場合（1行で）
def flatten_sum_comprehension(x):
    return sum([flatten(y) if isinstance(y, list) else [y] for y in x], [])


# 再帰的にflattenする場合（1行＆sumを使わない）2次元リストもOK
def flatten(x):
    return [z for y in x for z in (flatten(y) if isinstance(y, list) else [y])]


print(flatten([[1, 2], [3, 4], [5, 6]]))
print(flatten([1, [set([2]), [(3, 4), "5"]], 6]))
