import sys
from typing import NamedTuple

class Product(NamedTuple):
    price: int
    feature_number: int
    features: set[int]

def strictly_superior(N: int, M: int, products: list[Product]) -> bool:
    def superior(p_i: Product, p_j: Product) -> bool:
        return (
            p_i.price >= p_j.price and 
            p_i.features <= p_j.features and 
            (p_i.price > p_j.price or p_i.features < p_j.features)
        )

    return any([any([superior(p_i, p_j) for p_j in products]) for p_i in products])

def resolve() -> None:
    N, M = [int(e) for e in sys.stdin.readline().split()]
    products: list[Product] = []
    for _ in range(N):
        P, C, *F = [int(e) for e in sys.stdin.readline().split()]
        products.append(Product(P, C, set(F)))
    print("Yes" if strictly_superior(N, M, products) else "No")

# resolve()
# exit()

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """5 6
10000 2 1 3
15000 3 1 2 4
30000 3 1 3 5
35000 2 1 5
100000 6 1 2 3 4 5 6"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
3 1 1
3 1 2
3 1 2
4 2 2 3"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 10
72036 3 3 4 9
7716 4 1 2 3 6
54093 5 1 6 7 8 10
25517 7 3 4 5 6 7 9 10
96930 8 2 3 4 6 7 8 9 10
47774 6 2 4 5 6 7 9
36959 5 1 3 4 5 8
46622 7 1 2 3 5 6 8 10
34315 9 1 3 4 5 6 7 8 9 10
54129 7 1 3 4 6 7 8 9
4274 5 2 4 7 9 10
16578 5 2 3 6 7 9
61809 4 1 2 4 5
1659 5 3 5 6 9 10
59183 5 1 2 3 4 9
22186 4 3 5 6 8
98282 4 1 4 7 10
72865 8 1 2 3 4 6 8 9 10
33796 6 1 3 5 7 9 10
74670 4 1 2 6 8"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
