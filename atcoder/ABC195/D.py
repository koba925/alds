# D - Shipping Center

def solve():

    def solve1(left, right):
        in_box = [False] * num_baggage
        boxes_available = sorted(boxes[:left] + boxes[right + 1:])
        ans = 0
        for box in boxes_available:
            for i, bgg in enumerate(baggage):
                val, weight = bgg
                if not in_box[i] and weight <= box:
                    in_box[i] = True
                    ans += val
                    break
        return ans

    num_baggage, num_boxes, num_queries = [int(e) for e in input().split()]
    
    baggage = []
    for _ in range(num_baggage):
        Wi, Vi = [int(e) for e in input().split()]
        baggage.append((Vi, Wi))
    baggage.sort(reverse=True)

    boxes = [int(e) for e in input().split()]

    for _ in range(num_queries):
        left, right = [int(e) for e in input().split()]
        print(solve1(left - 1, right - 1))

solve()
