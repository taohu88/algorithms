import random
from collections import Counter


def reservoir_sample(a):
    r = None
    cnt = 0
    for x in a:
        cnt += 1
        rnd = random.uniform(0.0, 1.0)
        if rnd < 1/cnt:
            r = x
    return r


if __name__ == "__main__":
    random.seed()

    a = [4, 5, 5, 7, 8, 8, 9, 10, 1, 2]
    sz = 10000
    cnt = Counter((reservoir_sample(a) for i in range(sz)))
    print(f"Sample {sz} times with {cnt}")
