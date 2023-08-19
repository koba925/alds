# 11_C.py

class Dice:

    def __init__(self, sides):
        self.sides = sides

    @classmethod
    def read(cls):
        return cls([int(e) for e in input().split()])

    def top(self):
        return self.sides[0]

    def bottom(self):
        return self.sides[5]

    def front(self):
        return self.sides[1]

    def back(self):
        return self.sides[4]

    def left(self):
        return self.sides[3]

    def right(self):
        return self.sides[2]

    def roll(self, d):
        if d == "N":
            tmp = self.sides[0]
            self.sides[0] = self.sides[1]
            self.sides[1] = self.sides[5]
            self.sides[5] = self.sides[4]
            self.sides[4] = tmp
        elif d == "S":
            tmp = self.sides[0]
            self.sides[0] = self.sides[4]
            self.sides[4] = self.sides[5]
            self.sides[5] = self.sides[1]
            self.sides[1] = tmp
        elif d == "E":
            tmp = self.sides[0]
            self.sides[0] = self.sides[3]
            self.sides[3] = self.sides[5]
            self.sides[5] = self.sides[2]
            self.sides[2] = tmp
        elif d == "W":
            tmp = self.sides[0]
            self.sides[0] = self.sides[2]
            self.sides[2] = self.sides[5]
            self.sides[5] = self.sides[3]
            self.sides[3] = tmp
        elif d == "R":
            tmp = self.sides[1]
            self.sides[1] = self.sides[2]
            self.sides[2] = self.sides[4]
            self.sides[4] = self.sides[3]
            self.sides[3] = tmp
        elif d == "W":
            tmp = self.sides[1]
            self.sides[1] = self.sides[3]
            self.sides[3] = self.sides[4]
            self.sides[4] = self.sides[2]
            self.sides[2] = tmp

    def roll2top_front(self, top, front):
        def roll2top(top):
            if self.top() == top:
                return True
            for i in range(3):
                self.roll("S")
                if self.top() == top:
                    return True
            for i in range(3):
                self.roll("W")
                if self.top() == top:
                    return True
            return False

        def roll2front(front):
            for i in range(3):
                if self.front() == front:
                    return True
                self.roll("R")
            return False

        return roll2top(top) and roll2front(front)

    def equals(self, another):
        def challenge():
            for i in range(4):
                if self.sides == another.sides:
                    return True
                self.roll("R")
            return False

        for i in range(4):
            if challenge():
                return True
            self.roll("S")

        for i in range(4):
            if challenge():
                return True
            self.roll("W")

        return False

dice1 = Dice.read()
dice2 = Dice.read()
print("Yes" if dice1.equals(dice2) else "No")
