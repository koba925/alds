# 6_D.py
# TODO

# 軽いものを見つけて正しい位置に収まるまで入れ替える → #15でWA w=0が初めから定位置に収まっている
# quick sortに関係ある？ → 重さなんか見てないしなあ
# 探索する？ → さすがに組み合わせが？

def minimum_cost_sort(w):           
    sorted_w = list(sorted(w))
    cost = 0
    next_pos = 0
    while True:
        while w[next_pos] == sorted_w[next_pos]:
            next_pos += 1
            if len(w) <= next_pos:
                return cost
        to_w = sorted_w[next_pos]
        to_pos = w.index(to_w)
        from_w = sorted_w[to_pos]
        from_pos = w.index(from_w)
        if from_pos != to_pos:
            cost += w[from_pos] + w[to_pos]
            w[from_pos], w[to_pos] = w[to_pos], w[from_pos]


n = int(input())
w = [int(e) for e in input().split()]
print(minimum_cost_sort(w))