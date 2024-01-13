import functools as ft
import math

MOD = 998244353
def add_mod(a, b): return (a + b) % MOD
def sub_mod(a, b): return (a - b) % MOD
def mul_mod(a, b): return (a * b) % MOD
def inv_mod(n): return pow(n, MOD - 2, MOD)
def div_mod(a, b): return a * inv_mod(b) % MOD
def pow_mod(a, b): return pow(a, b, MOD)
# descending factorial power
def dpow_mod(n, k): return ft.reduce(lambda acc, e: mul_mod(acc, e), range(n, n - k, - 1), 1)
def fact_mod(n): return dpow_mod(n, n - 1)
def perm_mod(n, k): return dpow_mod(n, k)
def comb_mod(n, k): return div_mod(dpow_mod(n, k), fact_mod(k))
def sum_mod(A): return ft.reduce(add_mod, A)

def pow_mod_rec(a, b): 
    if b == 0: return 1
    if b % 2 == 0: return pow_mod(a, b // 2) ** 2 % MOD
    return mul_mod(pow(a, b - 1), a)

def pow_mod_loop(a, b):
    ret = 1
    a %= MOD
    while b > 0:
        if b % 2 == 1:
            ret = mul_mod(ret, a)
        a = mul_mod(a, a)
        b //= 2
    return ret

def comb_mod_loop(n, k):
    if k > n: return 0
    r = min(k, n - k)
    a, b = 1, 1
    for i in range(r):
        a = mul_mod(a, sub_mod(n, i))
        b = mul_mod(b, i + 1)
    return div_mod(a, b)

# import timeit
# print(timeit.timeit(lambda: pow_mod(1000000, 1000000)))
# print(timeit.timeit(lambda: pow_mod_lambda(1000000, 1000000)))
# print(timeit.timeit(lambda: pow_mod_loop(1000000, 1000000)))

# import psutil
# print(psutil.virtual_memory())

import unittest

class TestClass(unittest.TestCase):

    def test_pow(self):
        self.assertEqual(pow_mod(3, 4), 3 * 3 * 3 * 3)
        self.assertEqual(pow_mod(3, 0), 1)
        self.assertEqual(pow_mod(0, 3), 0)

    def test_pow_rec(self):
        self.assertEqual(pow_mod_rec(3, 4), pow_mod(3, 4))
        self.assertEqual(pow_mod_rec(123456789, 234567), pow_mod(123456789, 234567))
        self.assertEqual(pow_mod_rec(3, 0), pow_mod(3, 0))
        self.assertEqual(pow_mod_rec(0, 3), pow_mod(0, 3))

    def test_pow_loop(self):
        self.assertEqual(pow_mod_loop(3, 4), pow_mod(3, 4))
        self.assertEqual(pow_mod_loop(123456789, 234567), pow_mod(123456789, 234567))
        self.assertEqual(pow_mod_loop(3, 0), pow_mod(3, 0))
        self.assertEqual(pow_mod_loop(0, 3), pow_mod(0, 3))

    def test_dpow(self):
        self.assertEqual(dpow_mod(10, 3), 10 * 9 * 8)
        self.assertEqual(dpow_mod(3, 3), 3 * 2 * 1)
        self.assertEqual(dpow_mod(3, 0), 1)
        self.assertEqual(dpow_mod(0, 0), 1)

    def test_fact(self):
        self.assertEqual(fact_mod(5), math.factorial(5))
        self.assertEqual(fact_mod(1), math.factorial(1))
        self.assertEqual(fact_mod(0), math.factorial(0))

    def test_perm(self):
        self.assertEqual(perm_mod(10, 3), math.perm(10, 3))
        self.assertEqual(perm_mod(10, 0), math.perm(10, 0))
        self.assertEqual(perm_mod(10, 10), math.perm(10, 10))
        self.assertEqual(perm_mod(0, 1), math.perm(0, 1))
        self.assertEqual(perm_mod(0, 0), math.perm(0, 0))

    def test_comb(self):
        self.assertEqual(comb_mod(10, 3), math.comb(10, 3))
        self.assertEqual(comb_mod(10, 0), math.comb(10, 0))
        self.assertEqual(comb_mod(10, 10), math.comb(10, 10))
        self.assertEqual(comb_mod(0, 1), math.comb(0, 1))
        self.assertEqual(comb_mod(0, 0), math.comb(0, 0))


    def test_comb_loop(self):
        self.assertEqual(comb_mod_loop(10, 3), math.comb(10, 3))
        self.assertEqual(comb_mod_loop(10, 0), math.comb(10, 0))
        self.assertEqual(comb_mod_loop(10, 10), math.comb(10, 10))
        self.assertEqual(comb_mod_loop(0, 1), math.comb(0, 1))
        self.assertEqual(comb_mod_loop(0, 0), math.comb(0, 0))
    
    def test_comb_large(self):
        self.assertEqual()

unittest.main()