# B - Qualification simulator

def solve(n_people, n_dom_limit, n_abr_limit, people):
    n_dom_passed, n_abr_passed = 0, 0
    for p in people:
        if p == "a" and n_dom_passed + n_abr_passed < n_dom_limit + n_abr_limit:
            n_dom_passed += 1
            print("Yes")
        elif p == "b" and n_dom_passed + n_abr_passed < n_dom_limit + n_abr_limit and n_abr_passed < n_abr_limit:
            n_abr_passed += 1
            print("Yes")
        else:
            print("No")

N, A, B = [int(e) for e in input().split()]
S = input()
solve(N, A, B, S)
