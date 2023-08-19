# 6_B.py

cards = {
    "S": [True] * 13,
    "H": [True] * 13,
    "C": [True] * 13,
    "D": [True] * 13
}

def remove_card(suit, num):
    cards[suit][num - 1] = False

def remains_card(suit, num):
    return cards[suit][num - 1]

def print_card(suit, num):
    print(f"{s} {num}")

n = int(input())
for i in range(n):
    suit, num = input().split()
    num = int(num)
    remove_card(suit, num)

for s in cards.keys():
    for i in range(1, 13 + 1):
        if remains_card(s, i):
            print_card(s, i)

