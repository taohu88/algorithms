def find_allset(a):
    sz = len(a)
    for i in range(pow(2, sz)):
        yield choose_set(a, i)


def choose_set(a, x):
    mark = 1
    sz = len(a)

    r = []
    for i in range(sz):
        if x & mark:
            r.append(a[i])
        mark <<=1
    return r


if __name__ == "__main__":
    import time
    a = list(range(20))
    start = time.time()

    for i, s in enumerate(find_allset(a)):
        if i % 1000 == 0:
            end = time.time()
            print(f"{i:8d}th took total {end-start:.4f}s with result {s}")

    end = time.time()
    print(f"Total count {i+1} tooks {end-start:.2f}s")
