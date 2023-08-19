# B - Card Game for Three (ABC Edit)

def solve(sa, sb, sc):
    s = {"a": sa, "b": sb, "c": sc}
    turn = "a"
    while s[turn] != "":
        t = s[turn][0]
        s[turn] = s[turn][1:]
        turn = t
    return turn.upper()

sa = input()
sb = input()
sc = input()

print(solve(sa, sb, sc))