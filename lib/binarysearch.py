A = [1, 2, 2, 2, 3]

# 通常は https://docs.python.org/3/library/bisect.html を使う
# k以上の値でもっとも左に現れる要素のインデックスを返すので、
# 一致しているかを確認する必要がある

from bisect import bisect_left


def in_array(a, k) -> int:
    l = bisect_left(a, k)
    return l < len(a) and a[l] == k


# 最も左で一致する位置を返す
# 見つからなければ -1 を返す

# def binary_search(e, S):
#     left = -1
#     right = len(S)
#     while left < right - 1:
#         mid = (left + right) // 2
#         if e <= S[mid]:
#             right = mid
#         else:
#             left = mid
#     return right if right < len(S) and S[right] == e else -1
#
# print([binary_search(i, a) for i in range(5)])

# 条件を満たす最も左の位置を返す
# すべて満たせば0
# 全く満たさなければlen(S)

# def binary_search(is_ok, S):

#     def bisect(ng, ok, is_ok):
#         while abs(ok - ng) > 1:
#             mid = (ng + ok) // 2
#             if is_ok(mid):
#                 ok = mid
#             else:
#                 ng = mid
#         return ok
#
#     return bisect(-1, len(S), is_ok)
#
# print([binary_search(lambda n: i <= a[n], a) for i in range(5)])
