# AGC029A Irreversible operation

def solve(S):
    answer = 0
    whites = 0
    for i, color in enumerate(S):
        if color == "W":
            answer += (i - whites)
            whites += 1
    return answer

S = input()
print(solve(S))

# print(solve("BBW"))
# print(solve("BWBWBW"))
