
def num_digits_1(n): 
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c
        
def num_digits_2(n): 
    return len(str(n))

import timeit

print(timeit.timeit(lambda: num_digits_1(10000000000)))
print(timeit.timeit(lambda: num_digits_2(10000000000)))

