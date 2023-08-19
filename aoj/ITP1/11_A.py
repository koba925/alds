# 11_A.py

from copy import deepcopy
from functools import reduce

class Dice:

    def __init__(self, sides):
        self.sides = sides
        pass

    def move(self, dir):
        dice = deepcopy(self)
        if dir == "N":
            tmp = dice.sides[0]
            dice.sides[0] = dice.sides[1]
            dice.sides[1] = dice.sides[5]
            dice.sides[5] = dice.sides[4]
            dice.sides[4] = tmp
        elif dir == "S":
            tmp = dice.sides[0]
            dice.sides[0] = dice.sides[4]
            dice.sides[4] = dice.sides[5]
            dice.sides[5] = dice.sides[1]
            dice.sides[1] = tmp
        elif dir == "E":
            tmp = dice.sides[0]
            dice.sides[0] = dice.sides[3]
            dice.sides[3] = dice.sides[5]
            dice.sides[5] = dice.sides[2]
            dice.sides[2] = tmp
        elif dir == "W":
            tmp = dice.sides[0]
            dice.sides[0] = dice.sides[2]
            dice.sides[2] = dice.sides[5]
            dice.sides[5] = dice.sides[3]
            dice.sides[3] = tmp
        return dice

    def top(self):
        return self.sides[0]


dice = Dice([int(e) for e in input().split()])
print(reduce(lambda dice, dir: dice.move(dir),  input(), dice).top())

