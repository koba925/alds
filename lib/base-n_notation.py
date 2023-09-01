def base_b_to_int(s: str, b: int) -> int:
    return int(s, b)


def base_b_to_int_selfwritten(s: str, b: int) -> int:
    d = "0123456789abcdefghijklmnopqrstuvwxyz"
    n = 0
    for c in s:
        n *= b
        n += d.index(c)
    return n


def int_to_base_b(n: int, b: int) -> str:
    if n == 0:
        return "0"
    d = "0123456789abcdefghijklmnopqrstuvwxyz"
    temp = []
    while n > 0:
        temp.append(d[n % b])
        n //= b
    return "".join(reversed(temp))


for n in range(1000):
    assert int_to_base_b(n, 2) == bin(n)[2:]
    assert int_to_base_b(n, 8) == oct(n)[2:]
    assert int_to_base_b(n, 10) == str(n)
    assert int_to_base_b(n, 16) == hex(n)[2:]
    assert base_b_to_int(bin(n)[2:], 2) == n
    assert base_b_to_int(oct(n)[2:], 8) == n
    assert base_b_to_int(str(n), 10) == n
    assert base_b_to_int(hex(n)[2:], 16) == n
    assert base_b_to_int_selfwritten(bin(n)[2:], 2) == n
    assert base_b_to_int_selfwritten(oct(n)[2:], 8) == n
    assert base_b_to_int_selfwritten(str(n), 10) == n
    assert base_b_to_int_selfwritten(hex(n)[2:], 16) == n
    assert base_b_to_int(int_to_base_b(n, 36), 36) == n
    assert base_b_to_int(int_to_base_b(n, 36), 36) == base_b_to_int_selfwritten(
        int_to_base_b(n, 36), 36
    )
