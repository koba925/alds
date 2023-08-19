# C - Five Transportations

def divceil(a, x): return -(-a // x)

N_TRANSPORTS = 5

def solve(n_people, capacities):
    return divceil(n_people, min(capacities)) + N_TRANSPORTS - 1

N = int(input())
A = []
for _ in range(N_TRANSPORTS):
    A.append(int(input()))
print(solve(N, A))
