import heapq


def merge_k(xs):
    h = build_heap(xs)
    r = []
    while h:
        v, i = heapq.heappop(h)
        r.append(v)

        if xs[i]:
            heapq.heappush(h, (xs[i].pop(), i))
    return r


def build_heap(xs):
    h = []
    for i, x in enumerate(xs):
        if xs[i]:
            h.append((xs[i].pop(), i))
    heapq.heapify(h)
    return h


if __name__ == "__main__":
    xs = [
        [1, 4, 5],
        [1, 3, 4],
        [2, 6, 8]
        ]
    # reverse it
    xs = [x[::-1] for x in xs]
    r = merge_k(xs)
    print(r)

