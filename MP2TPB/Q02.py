# Q02.py

# ops = ["+", "-", "*", "//", ""]
ops = ["*", ""]

for n in range(1000, 10000):
    nstr = str(n)
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                expr = nstr[3] + op3 + nstr[2] + op2 + nstr[1] + op1 + nstr[0]
                if expr == nstr:
                    continue
                try:
                    val = eval(expr)
                except:
                    continue
                if n == val:
                    print(f"{n} = {expr}")
