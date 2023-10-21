def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]

    # print("YES" if len([a for a in A if a % 2 == 1]) % 2 == 0 else "NO")
    print("YES" if sum(A) % 2 == 0 else "NO")

# resolve()
# exit()

