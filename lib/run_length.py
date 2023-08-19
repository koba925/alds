# def run_length(seq):
#     if len(seq) == 0:
#         return []

#     prev, length, ret = seq[0], 1, []
#     for i in range(1, len(seq)):
#         if seq[i] == prev:
#             length += 1
#         else:
#             ret.append((prev, length))
#             prev = seq[i]
#             length = 1
#     ret.append((prev, length))

#     return ret


def run_length(seq):
    length = len(seq)
    i, ret = 0, []
    while i < length:
        elem, count = seq[i], 0
        while i + count < length and seq[i + count] == elem:
            count += 1
        ret.append((elem, count))
        i += count
    return ret


print(run_length([]))
print(run_length([1]))
print(run_length([1, 1, 1, 3, 2, 2, 4]))
print(run_length([1, 1, 1, 3, 2, 2]))
print(run_length("aaabbc"))
