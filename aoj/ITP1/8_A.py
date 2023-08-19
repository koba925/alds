# 8_A.py

def switch_case(c):
    return c.lower() if c.isupper() else c.upper() if c.islower() else c

s = input()
print("".join([switch_case(c) for c in s]))

