# 9_B.py

def shuffle(cards):
    m = int(input())
    for i in range(m):
        h = int(input())
        cards = cards[h:] + cards[:h]
    return cards

while True:
    cards = input()
    if cards == "-":
        break
    print(shuffle(cards))
