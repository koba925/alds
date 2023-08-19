# 14_B.py String Search
# TODO: understand KMP https://daeudaeu.com/kmp/
# TODO: BM

# startswith: AC #18 0.22 Total 1.18
def startwith_search(T, P):
    for i in range(len(T) - len(P) + 1):
        if T.startswith(P, i):
            print(i)

# naive loop: #18 0.70 #20 4.99TLE
def naive_search(T, P):
    for i in range(len(T) - len(P) + 1):
        for j in range(len(P)):
            if T[i + j] != P[j]:
                break
        else:
            print(i)

# while loop: #18 0.50 #20 4.99TLE
def while_search(T, P):
    ilimit = len(T) - len(P) + 1
    jlimit = len(P)

    i = 0
    while i < ilimit:
        j = 0
        while j < jlimit:
            if T[i + j] != P[j]:
                break
            j += 1
        else:
            print(i)
        i += 1

# skip repeating character: AC #18 0.79 #20 0.80 #33 1.45 #34 1.47 Total 1.47
def skip_search(T, P):
    ilimit = len(T) - len(P) + 1
    jlimit = len(P)

    i = 0
    j = 0
    while i < ilimit:
        repeating = True
        ti = T[i]
        nj = j
        while j < jlimit:
            if T[i + j] != P[j]:
                break
            if repeating and P[j] == ti:
                nj += 1
            else:
                repeating = False
            j += 1
        else:
            print(i)
        j = max(0, nj - 1)
        i += 1


# KMP search: AC #18 0.46 #20 0.38 #33 0.93 #34 0.96 Total 0.96
def KMPsearch(T, P):

    def KMPtable():
        kmp = [-1, 0] # kmp[0]=-1, kmp[1]=0は確定 -1じゃないとだめ？っていうかいる？ 

        # "MP"
        for i in range(2, len(P) + 1):
            j = kmp[i - 1]
            while j > 0 and P[i - 1] != P[j]:
                j = kmp[j]
            if P[i - 1] == P[j]:
                j += 1
            kmp.append(j)
        
        # "K"による追加 あまりパフォーマンスは変わらなかった
        # i=0 (P[i]=-1) と i=len(P) (out of range)は除外
        for i in range(1, len(P)):
            if P[i] == P[kmp[i]]:
                kmp[i] = kmp[kmp[i]]

        return kmp

    kmp = KMPtable()
    tlen, plen = len(T), len(P)
    tpos = ppos = 0
    while tpos < tlen:
        if T[tpos] == P[ppos]:
            if ppos == plen - 1:
                print(tpos - ppos)
                tpos += 1
                ppos = kmp[plen] # 0に戻さなくていいの？
                continue
            tpos += 1
            ppos += 1
        else:
            if kmp[ppos] == kmp[0]: # kmp[0]っていつも-1なのでは？
                tpos += 1
                ppos = 0
            else:
                ppos = kmp[ppos]

# Rolling Hash: AC #18 0.63 #20 0.66 #33 1.48 #34 1.57 Total 1.57
def rolling_hash_search(t, p):
    BASE = 100000007
    MAX = 2**63 - 1

    pl, tl = len(p), len(t)
    if pl > tl:
        return

    t_pl = BASE ** pl % MAX

    ph = th = 0
    for i in range(pl):
        ph = (ph * BASE + ord(p[i])) % MAX
        th = (th * BASE + ord(t[i])) % MAX
    
    for i in range(0, tl - pl + 1):
        if ph == th:
            print(i)
        if i + pl < tl:
            th = (th * BASE + ord(t[i + pl]) - ord(t[i]) * t_pl) % MAX


# Rolling Hash 2: AC #18 0.56 #20 0.54 #33 1.35 #34 1.39 Total 1.39
def rolling_hash_search_2(T, P):
    BASE = 100000007
    MAX = 2**63 - 1

    t = [ord(e) for e in T]
    p = [ord(e) for e in P]

    pl, tl = len(p), len(t)
    if pl > tl:
        return

    t_pl = BASE ** pl % MAX

    ph = th = 0
    for i in range(pl):
        ph = (ph * BASE + p[i]) % MAX
        th = (th * BASE + t[i]) % MAX
    
    for i in range(0, tl - pl + 1):
        if ph == th:
            print(i)
        if i + pl < tl:
            th = (th * BASE + t[i + pl] - t[i] * t_pl) % MAX

T = input()
P = input()

# startwith_search(T,P)
# naive_search(T, P)
# while_search(T, P)
# skip_search(T, P)
# KMPsearch(T, P)
#rolling_hash_search(T, P)
rolling_hash_search_2(T, P)
