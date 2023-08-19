# B - ss

def is_even_string(s):
    l = len(s)
    return s[:l//2] == s[l//2:]

def solve(S):
    S = S[:-2]
    while not is_even_string(S):
        S = S[:-2]
    return len(S)

print(solve(input()))
