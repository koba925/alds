# Q01.py

import timeit

def reverse(s):
    return "".join(list(reversed(s)))

def palindrome(s):
    return s == reverse(s)

def solve():
    n = 11
    while True:
        str10 = str(n)
        str8 = oct(n)[2:]
        str2 = bin(n)[2:]
        if palindrome(str10) and palindrome(str8) and palindrome(str2):
            return (str10, str8, str2)
        n += 2

print(solve())

# print(timeit.timeit(solve, number=1000))

