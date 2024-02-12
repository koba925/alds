# TK: Range Add Query (RAQ)
# TK: 遅延セグメント木 Lazy Segment Tree

#######################################################################
# using ac-library-python https://github.com/not522/ac-library-python/
# does not run on AOJ
#######################################################################

from atcoder.lazysegtree import LazySegTree

INITVAL = 0

n, q = [int(e) for e in input().split()]

# 総積を求めるときの写像（値は使われない）
def op(data1, data2): return 0
# opの単位元 演算しても値が変わらない 配列の初期値にも使う
e = INITVAL
# 操作時に上のlazyを下のdataに作用させる写像
def mapping(lazy_upper, data_lower): return lazy_upper + data_lower
# 操作時に上のlazyを下のlazyに作用させる写像
def composition(lazy_upper, lazy_lower): return lazy_upper + lazy_lower
# lazy_upperに入れるとmapping・compositionが恒等写像になる値
id_ = 0
# 初期配列 整数nを指定すると初期値がe、長さがnの配列になる
v = n
# 遅延セグメント木の構築
lst = LazySegTree(op, e, mapping, composition, id_, v)

for _ in range(q):
    com, *p = input().split()
    match com:
        case "0": lst.apply(int(p[0]) - 1, int(p[1]), int(p[2]))
        case "1": print(lst.get(int(p[0]) - 1))
