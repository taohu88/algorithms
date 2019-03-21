import numpy as np


def drops(n, h):
    numdrops = np.zeros((n+1, h+1), dtype=np.int)

    # n == 1
    for height in range(1, h + 1):
        numdrops[1, height] = height

    for height in range(2):
        for m in range(1, n + 1):
            numdrops[m, height] = height

    if n == 1:
        return numdrops[n, h], numdrops

    if h < 2:
        return numdrops[n, h], numdrops

    for m in range(2, n + 1):
        for height in range(2, h+1):
            min_d = h
            for k in range(1, height+1):
                #egg broken at i
                r = max(numdrops[m-1, k-1], numdrops[m, height-k]) + 1
                if r < min_d:
                    min_d = r
            numdrops[m, height] = min_d

    return numdrops[n, h], numdrops


if __name__ == "__main__":
    n = 2
    h = 100
    d, numdrops = drops(n, h)
    print(f"Drops {n} egges in {h} floors is {d}")

    print(f"Table {numdrops[1:, 1:]}")
